import requests
import re

params={
'DDDDD': '',   
'upass': '',        
'R1': '0',
'R2':'' ,
'R6': '0',
'para': '00',
'0MKKey': '123456',
'R7': '0'
}


header1={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'129',
'Content-Type':'application/x-www-form-urlencoded',
'Host':'59.67.0.245',
'Origin':'http://59.67.0.245',
'Referer':'http://59.67.0.245/a70.htm',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

header2={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Host': '59.67.0.245',
'Referer': 'http://59.67.0.245/a70.htm',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}

#-----------------读取配置文件
def read_config():
	with open("login_config.txt","r") as f:
		xuehao = f.readline()
		mima = f.readline()
		if ( xuehao or mima ) == "":
			return False
		xuehao = xuehao[0:8]
	return (xuehao,mima)


#--------------检查是否已登陆,是则注销
def check():
	url=("http://59.67.0.245/")
	html=requests.get(url)
	try:
		html.text.index("注销页")
	except ValueError:
		return False
	else:
		return True

#-------------登出
def logout():
	url="http://59.67.0.220/F.htm" 
	html = requests.get(url)
	print("logout")

#--------------提交登录
def login():
	url=("http://59.67.0.245/a70.htm")
	html=requests.post(url,data=params,headers = header1)
	
	try:
		html.text.index("跳转至AC传递的用户原始输入地址")
	except ValueError as e:
		print("error " +str(e))
		input()


#-------------获取余额 流量使用
def get_flow_fee():
	url =("http://59.67.0.245/")
	html = requests.get(url,headers = header2)
	flow = re.findall(".*flow='(.*?) '.*",html.text)
	fee = re.findall(".*fee='(.*?)'.*",html.text)
	#print(fee)
	f_flow =int(flow[0])/1024
	f_fee = (int(fee[0]) - int(fee[0])%100)/10000
	if f_fee == 123456.78:
		print("已用流量：%.3f" %f_flow)
	else:
		print("已用流量：%.3f " %f_flow)
		print("余额：",f_fee)  
	input()


#-------------测试保留页面	
def save_page():
	#html=requests.get(url,headers=header)
	#print(html.headers)
	print(html.text)
	f = open("./testpage.txt","w")
	f.writelines(html.text)	
	f.close()
	try:
		html.text.index("跳转至AC传递的用户原始输入地址")
	except ValueError:
		# pass
		print("failed")
	else:
		print("BINGO!\n")

if __name__ == "__main__":		
	config = read_config()
	if config == False:
		input("Invalid Config")
		exit()
	params['DDDDD'] = config[0]
	params['upass'] = config[1]
	print(config[0])
	
	if not check():
		login()
		get_flow_fee()
		exit()
	else:
		logout()
		exit()
