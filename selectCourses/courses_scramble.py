import json
import requests
#from selenium import webdriver
import os
from PIL import Image ,ImageFilter
import time
import hashlib 
import re
#import pytesseract

start_url = "http://jwxtxs.tust.edu.cn:46110/login"
url = "http://jwxtxs.tust.edu.cn:46110/j_spring_security_check"#j_spring_security_check"
captcha_url = "http://jwxtxs.tust.edu.cn:46110/img/captcha.jpg"
callback_url = "http://jwxtxs.tust.edu.cn:46110/student/courseSelect/thisSemesterCurriculum/ajaxStudentSchedule/callback"
#xuanke_url = "http://jwxtxs.tust.edu.cn:46110/student/courseSelect/selectCourses/waitingfor"
xuanke_url = "http://jwxtxs.tust.edu.cn:46110/student/courseSelect/selectCourse/checkInputCodeAndSubmit"
query_url = "http://jwxtxs.tust.edu.cn:46110/student/courseSelect/selectResult/query"
token_url = "http://jwxtxs.tust.edu.cn:46110/student/courseSelect/courseSelect/index"
clist_url = "http://jwxtxs.tust.edu.cn:46110/student/courseSelect/planCourse/courseList"
queryTeacherJL_url = "http://jwxtxs.tust.edu.cn:46110/student/courseSelect/queryTeacherJL"

login_datas = {
"j_username": "",
"j_password": "",
"j_captcha": "",
}
lesson_code = "G900104310_101"
term_code = "2019-2020-2-1"

clist = {
"fajhh": "3742",
"jhxn": "2019-2020-2-1",
"kcsxdm": "",
"kch": "",
"kcm": "",
"kclbdm":'', 
"xq": "0",
"jc": "0",
}

queryTeacherJL_datas = {
"id": term_code+"_"+lesson_code,
}

xuanke_datas ={
"dealType": "2",
"fajhh": "3742",
"kcIds": lesson_code+"_"+term_code,
#"kcms": "21019,36896,23398,95,49,48,49,",
"sj": "0_0",
"kclbdm":"",
"inputCode":"",
"tokenValue":"",
}
#
#
captcha_headers = {
"Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Connection": "keep-alive",
"Host": "jwxtxs.tust.edu.cn:46110",
"Referer": "http://jwxtxs.tust.edu.cn:46110/login",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
}

query_datas = {
"kcNum": "",
"redisKey": "",
}


start_url = 'http://jwxtxs.tust.edu.cn:46110/'

def get_time():
	date = pytime.strftime("%Y-%m-%d", time.localtime()) 


def md5(str):
	str = str.encode("utf-8")
	m = hashlib.md5()
	m.update(str)
	md5_str = m.hexdigest()
	del m
	return md5_str

def get_captcha_and_cookie(page):
	try:
		image = page.get(captcha_url,headers=captcha_headers)
		f = open("captcha.png","wb")
		f.write(image.content)
		f.close()
		cookie = image.cookies
		#print(cookie)
		#print("get")
	except Exception as e:
		print("try again")
		get_captcha_and_cookie(page)

def DataEncoding(str):#预留加密解密
	return str
def DataDecoding(str):
	return str
def test(html):#保留页面
	file = open("test.html","w")
	try:
		file.write(html.decode())
	except:
		file.write(html)
	file.close()

def query():
	pass
# try:
	# image = requests.get(captcha_url,headers=captcha_headers)
	# f = open(captcha.png,"wb")
	# f.write(image)
	# f.close()
	# requests.post(start_url,datas=login_datas)
# except:
	# pass
# image = requests.get(captcha_url,headers=captcha_headers)
# f = open(r"C:\Users\Oberon\Desktop\captcha.png","wb")
# f.write(image.content)
# f.close()
# requests.post(start_url)#,data=login_datas)
# captcha = Image.open("C:\\Users\\Oberon\\Desktop\\captcha.png")
# captcha.show()

# #captcha.show()

# # colorlist = captcha.getcolors(1000000)
# #print(colorlist)
# #first = colorlist[0]
# # for i,j in colorlist:
	# # if i > first[0]:
		# # second = first
		# # first = colorlist[0]
# pix = captcha.load()
# size = captcha.size
# captcha.filter(ImageFilter.BLUR)
# #captcha.filter(ImageFilter.BLUR)
# captcha.filter(ImageFilter.SHARPEN)
# captcha.show()
# ########################去黑线
# for x in range(size[0]):
	# for y in range(size[1]):
		# pixal = pix[x,y]
		# if (pixal[0]>100 and pixal[1] > 120 and pixal[2]>120) or (pixal[0]<150 and pixal[1] <170 and pixal[2] < 150):
			# captcha.putpixel((x,y),(255,255,255))
# captcha.show()
# ########################去边框
# for x in range(0,10):
	# for y in range(0,10):
		# captcha.putpixel((x,y),(255,255,255))
# for x in range(size[0]-10,size[0]):
	# for y in range(0,10):
		# captcha.putpixel((x,y),(255,255,255))
# for x in range(0,10):
	# for y in range(size[1]-10,size[1]):
		# captcha.putpixel((x,y),(255,255,255))
# for x in range(size[0]-10,size[0]):
	# for y in range(size[1]-10,size[1]):
		# captcha.putpixel((x,y),(255,255,255))
# #######################加粗补空
# for x in range(size[0]):
	# for y in range(size[1]):
		# pixal = pix[x,y]
		# if pixal[0] > 128 and pixal[1] < 100:
			# captcha.putpixel((x,y),(0,0,0))
		# else:
			# try:
				# pix_around = pix[x,y+1]
				# try:
					# pix_around = pix[x,y+1]
					# true = 1
				# except:
					# pass
				# if pix_around != (255,255,255) and true == 1:
					# captcha.putpixel((x,y),(0,0,0))
					
			# except:
				# pass
			# try:
				# pix_around = pix[x,y+2]
				# if pix_around != (255,255,255):
					# captcha.putpixel((x,y),(0,0,0))
			# except:
				# pass
# #######################

# #captcha.filter(ImageFilter.SMOOTH)
# captcha.filter(ImageFilter.SHARPEN)
# captcha.show()

# result = pytesseract.image_to_string(captcha)
# result = input("Input the captcha code")
#captcha.show()
#print("result = "+result)

if __name__ == "__main__":
	#reset()
	status_code = ""
	user_data_check = 1
	schedule_data_check = 1
	check_input = 1
	
	try:#读取课程表数据
		ScheduleData =open("schedule.list","r")
		data_str = ScheduleData.read()
		ScheduleData.close()
		JsonToLesson(data_str)
		os.system("cls")
		PrintClassList(ClassList)
		input()
		schedule_data_check = 0
		print("read schedule , done")
	except Exception as e:
		#print(e)
		pass
	#print(schedule_data_check)

	if schedule_data_check == 1:
		try:#读取用户数据
			user_data = open("database.data","r")
			mima_length = DataDecoding(user_data.read(1))
			xuehao = DataDecoding(user_data.read(8))
			mima = DataDecoding(user_data.read(int(mima_length)))
			user_data_check = 0
			#print(xuehao,mima)
		except Exception as e:
			#print(e)
			print("if you use this first,it might take you more time.")
			print("new user\nplease input your id:")
			xuehao = input() 
			while (int(xuehao) / 10000000 < 1) or (int(xuehao) / 10000000 >= 10):#判断合法学号
				print("input id again")
				xuehao = input()
			print("please input the passwords:")
			mima = input()
		login_datas["j_username"] = xuehao
		login_datas["j_password"] = md5(mima)
		page = requests.session()#
		while True:#不断尝试登录
			if check_input == 0:#重试
				print("please input your id:")
				xuehao = input() 
				while (int(xuehao) / 10000000 < 1) or (int(xuehao) / 10000000 >= 10):#判断合法学号
					print("input id again")
					xuehao = input()
				print("please input the passwords:")
				mima = input()
				login_datas["j_username"] = xuehao
				login_datas["j_password"] = md5(mima)
				
			get_captcha_and_cookie(page)
			captcha = Image.open("captcha.png")
			captcha.show()
			#cr.WatchCaptcha(captcha)
			print("please read the captcha:")
			result = input() 
			login_datas['j_captcha'] = result
			
			#os.remove('captcah.png')
			p = page.post(url,data = login_datas)#提交表单
			#input(p.headers)
			if (p.url == "http://jwxtxs.tust.edu.cn:46110/login?errorCode=badCredentials"):#判断是否登录
				print("try again")
				check_input = 0
			elif (p.url == "http://jwxtxs.tust.edu.cn:46110/login?errorCode=badCaptcha"):	
				print("captcha false")
				check_input = 0
			elif (p.url == "http://jwxtxs.tust.edu.cn:46110/login"):
				check_input = 0
			elif (p.url =="http://jwxtxs.tust.edu.cn:46110/index.jsp"):
				print(p.url)
				print("succeed")
				break
			else:
				check_input = 0
				
		input("xuanke?")
		input()
		#获取选课列表
		
		#if user_data_check == 1:
		 #开始选课
		try:
			p = page.get(token_url) #获得token
			#print(p.text)
			mj = re.search(r"id=\"tokenValue\" value=\".*\"",p.text)
			mjstr = mj.group()
			tokenValue = mjstr[23:-1]
			xuanke_datas["tokenValue"]= tokenValue
			#print(tokenValue)
			# while True:
				# try:
					# mj = re.search(input("pattern:   :"),p.text)
					# print(mj.group())
				# except Exception as e:
					# print(e)
			courses = {""}
		#提交学科表单
			courses = {
"G900100110_101",
# "WL00170110_01",
# 'WL00170220_01',
# 'WL00170320_01',
# 'WL00170420_01',
# 'WL00170520_01',
# 'WL00170610_01',
# 'WL00170720_01',
# 'WL00170810_01',
# 'WL00170920_01',
# 'WL00171010_01',
# 'WL00171120_01',
# 'WL00171210_01',
# 'WL00171320_01',
# 'WL00171420_01',
# 'WL00171510_01',
# 'WL00171610_01',
# 'WL00171620_01',
# 'WL00171710_01',
# 'WL00171720_01',
# "WL00171810_01" 
}
			for i in courses:
				lesson_code = i
				p = page.post(queryTeacherJL_url,data = queryTeacherJL_datas)
				print(p.status_code)
				p = page.post(xuanke_url,data = xuanke_datas)
				print(p.url)
				print(p.status_code)
				#print(p.text)
				bb = json.loads(p.text)
				print(bb)
				
				query_datas["redisKey"] = xuehao+"2"
				query_datas["kcNum"] = '1'
				print(query_datas)
				

				while True:
					#查询选课结果
					pp = page.post(query_url,data = query_datas)
					
					#print(pp.url)
					print(pp.status_code)
					print(pp.text)
					back = pp.text
					back = json.loads(back)
					back = back['isFinish']
					#print(back)
					if back == True:
						print(lesson_code +" xuanke chenggong")
						break
					if input() == "n":
						break
					#print(pp.content)
		
		except Exception as e:
			input(e)