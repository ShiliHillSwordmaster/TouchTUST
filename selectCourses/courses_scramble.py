import json
import requests
#from selenium import webdriver
import os
from PIL import Image ,ImageFilter
import time
import hashlib 
import re
#import pytesseract

#课程列表
courses = {
# "WL00170110_01",
# "WL00170220_01",
# "WL00170320_01",
   # }
# # "G900100110_101",
#'WL00170420_01',
'WL00170520_01',
'WL00170610_01',
'WL00170720_01',
'WL00170810_01',
'WL00170920_01',
'WL00171010_01',
'WL00171120_01',
'WL00171210_01',
'WL00171320_01',
'WL00171420_01',
'WL00171510_01',
'WL00171610_01',
'WL00171620_01',
'WL00171710_01',
'WL00171720_01',}
# # "WL00171810_01" 
# }

lesson_code = "G900104310_101"  #课程编号
term_code = "2019-2020-2-1"    #学期编号


start_url = "http://jwxtxs.tust.edu.cn:46110/login"
url = "http://jwxtxs.tust.edu.cn:46110/j_spring_security_check"#j_spring_security_check"
captcha_url = "http://jwxtxs.tust.edu.cn:46110/img/captcha.jpg"
callback_url = "http://jwxtxs.tust.edu.cn:46110/student/courseSelect/thisSemesterCurriculum/ajaxStudentSchedule/callback"
waitingfor_url = "http://jwxtxs.tust.edu.cn:46110/student/courseSelect/selectCourses/waitingfor"
xuanke_url = "http://jwxtxs.tust.edu.cn:46110/student/courseSelect/selectCourse/checkInputCodeAndSubmit"
query_url = "http://jwxtxs.tust.edu.cn:46110/student/courseSelect/selectResult/query"
token_url = "http://jwxtxs.tust.edu.cn:46110/student/courseSelect/courseSelect/index"
clist_url = "http://jwxtxs.tust.edu.cn:46110/student/courseSelect/planCourse/courseList"
queryTeacherJL_url = "http://jwxtxs.tust.edu.cn:46110/student/courseSelect/queryTeacherJL"
getSectionAndTime_url = "http://jwxtxs.tust.edu.cn:46110/ajax/getSectionAndTime"
courseSelect_url = "http://jwxtxs.tust.edu.cn:46110/student/courseSelect/courseSelect/index"
planCourse_url = "http://jwxtxs.tust.edu.cn:46110/student/courseSelect/planCourse/index"

login_datas = {
"j_username": "",
"j_password": "",
"j_captcha": "",
}


clist = {
"fajhh": "",
"jhxn": term_code,
"kcsxdm": "",
"kch": "",
"kcm": "",
"kclbdm":'', 
"xq": "0",
"jc": "0",
}

getSectionAndTime_datas = {
'planNumber': '',
'ff': 'j',
}

queryTeacherJL_datas = {
"id": term_code+"_"+lesson_code,
}

waitingfor_datas ={
"dealType": "",
"fajhh": "",
"kcIds": lesson_code+"_"+term_code,
#"kcms": "21019,36896,23398,95,49,48,49,",
"sj": "",
"kclbdm":"",
}

xuanke_datas ={
"dealType": "",
"fajhh": "",
"kcIds": lesson_code+"_"+term_code,
#"kcms": "21019,36896,23398,95,49,48,49,",
"sj": "",
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
		if image.text == "":
			print("captcha failed")
			input()
			return False
		print("captcha: "+str(image.status_code))
		
		input()
		f = open("captcha.png","wb")
		f.write(image.content)
		f.close()
		cookie = image.cookies
		#print(cookie)
		#print("get")
	except Exception as e:
		print("try again"+str(e))
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
	


if __name__ == "__main__":
	#reset()
	status_code = ""
	user_data_check = 1
	schedule_data_check = 1
	check_input = 1
	

	if True:
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
				
			#获取验证码图片
			if get_captcha_and_cookie(page) == False:
				print("error")
				exit()
			captcha = Image.open("captcha.png")
			captcha.show()#显示图片
			
			#cr.WatchCaptcha(captcha)
			print("please read the captcha:") #读取验证码
			result = input() 
			login_datas['j_captcha'] = result
			
			#os.remove('captcah.png')
			p = page.post(url,data = login_datas)#提交登录表单
			#input(p.headers)
			
			#判断是否登录
			if (p.url == "http://jwxtxs.tust.edu.cn:46110/login?errorCode=badCredentials"):
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
			#登录结束
			
		input("xuanke?")
		input()
		#
		
		#if user_data_check == 1:
		 #开始选课
		try:
			#获得方案计划号
			p = page.get(courseSelect_url)
			fajhh = re.search("fajhh=.*\'",p.text)
			fajhh = fajhh.group()
			# print(fajhh)
			fajhh = fajhh[-5:-1]
			print('fajhh:'+fajhh)
			p = page.get(planCourse_url+"?fajhh="+fajhh,data = {"fajhh":fajhh,}) #get fajhh
			print("planCourse_index: "+str(p.status_code))
			# print(p.text)
			dealType = re.search("dealType\" value=\".*\"",p.text)
			dealType = dealType.group()
			dealType = dealType[-2:-1]
			print('dealType:'+dealType)
			
			sj = re.search("sj\" value=\".*\"",p.text)
			sj = sj.group()
			sj = sj[-4:-1]
			print('sj:'+sj)
			
			
			p = page.get(token_url) #获得token
			#print(p.headers)
			#print(p.text)
			mj = re.search(r"id=\"tokenValue\" value=\".*\"",p.text)
			mjstr = mj.group()
			print("mjstr: "+mjstr)
			tokenValue = mjstr[23:-1]
			print("tokenValue: "+tokenValue)
			
			
			#准备选课表单内容
			xuanke_datas["tokenValue"]= tokenValue
			xuanke_datas["fajhh"] = fajhh
			xuanke_datas['dealType'] = dealType
			xuanke_datas['sj'] = sj
			waitingfor_datas["fajhh"] = fajhh
			waitingfor_datas['dealType'] = dealType
			waitingfor_datas['sj'] = sj
			
			
			#p = page.post(getSectionAndTime_url,data =getSectionAndTime_datas )
			#print(p.url)
			#print(p.headers)
					
			
		
			for i in courses:
				lesson_code = i
				queryTeacherJL_datas["id"] = term_code+"_"+lesson_code
				
				#模拟勾选
				p = page.post(queryTeacherJL_url,data = queryTeacherJL_datas) 
				print("queryTeacherJL:" + str(p.status_code))
				#print("queryTeacherJL_datas: "+str(queryTeacherJL_datas))
				
				kcIds = lesson_code+"_"+term_code
				xuanke_datas["kcIds"] = kcIds
				print(kcIds)
				
				searchtj = lesson_code[0:10]
				xuanke_datas["searchtj"] = searchtj
				print(searchtj)
				
				#提交选课表单
				p = page.post(xuanke_url,data = str(xuanke_datas))
				#print("xuanke_datas: "+str(xuanke_datas))
				print("xuanke:" + str(p.status_code))
				#print(p.text)
				bb = json.loads(p.text)
				print("response_ "+str(bb))
				
				query_datas["redisKey"] = xuehao+dealType
				query_datas["kcNum"] = '1'
				#print("query_datas: "+str(query_datas))
				
				#提交表单等待结果
				p = page.post(waitingfor_url,data = waitingfor_datas)
				#print("waitingfor_datas: "+str(waitingfor_datas))
				print("waiting ..."+str(p.status_code))
				
				
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