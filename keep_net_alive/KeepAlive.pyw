import requests
import re
import time
import os 
import socket
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread , pyqtSignal, QDateTime , QObject
import threading


header={
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




	#return True

icon = "fist.png"

	

class mainWindow(QObject):
	def __init__(self):
		super(mainWindow,self).__init__()
		self.mainWindowFrame = QtWidgets.QMainWindow(None,QtCore.Qt.FramelessWindowHint) #创建无边框窗口
		self.tuo = self._setupTray()	#设置托盘及菜单
		self._setupUi(self.mainWindowFrame)	#绘制主界面
		self._initUI()	#初始化主界面
		
	def _setupTray(self):
		global icon
		self.tray = QtWidgets.QSystemTrayIcon()
		self.tray.setIcon(QtGui.QIcon(icon))
		self.tray.showMessage("Don\'t worry","I\'m holding",icon=0)
		#self.tray.activated.connect(self.TuoPanEvent) #设置托盘点击事件处理函数
		self.tray.show()
		self.tray_menu = QtWidgets.QMenu(QtWidgets.QApplication.desktop()) #创建菜单
		self.RestoreAction = QtWidgets.QAction(u'还原 ', self, triggered=self.mainWindowFrame.show) #添加一级菜单动作选项(还原主窗口)
		self.QuitAction = QtWidgets.QAction(u'退出 ', self, triggered=app.quit) #添加一级菜单动作选项(退出程序)
		self.HideAction = QtWidgets.QAction(u'隐藏 ', self, triggered=self.mainWindowFrame.hide)
		self.tray_menu.addAction(self.RestoreAction) #为菜单添加动作
		self.tray_menu.addAction(self.HideAction)
		self.tray_menu.addAction(self.QuitAction)
		self.tray.setContextMenu(self.tray_menu) #设置系统托盘菜单
		
	def _setupUi(self, windowFrame):
		windowFrame.setObjectName("keep alive !")
		windowFrame.setWindowModality(QtCore.Qt.WindowModal)
		#windowFrame.resize(200,100)#可拖拽，界面大小
		windowFrame.setFixedSize(200,100)#不可拖拽，界面大小
		self.centralWidget = QtWidgets.QWidget(windowFrame)
		self.centralWidget.setObjectName("centralWidget")
		
		# self.pushButton1 = QtWidgets.QPushButton(self.centralWidget)
		# self.pushButton1.setGeometry(QtCore.QRect(10, 10, 100, 60))
		# self.pushButton1.setObjectName("button1")
		# self.pushButton1.setText("Aha!")
		
		self.label = QtWidgets.QLabel(self.centralWidget)
		self.label.setGeometry(QtCore.QRect(10, 10, 180, 80))	#装饰矩形
		self.label.setFont(QtGui.QFont("Microsoft YaHei"))
		self.label.setStyleSheet("border-width: 3px;border-style: solid;border-color: rgb(191,191,191);")
		self.label.setText("           connected")
		self.label.setObjectName("label")
		#self.label.grabKeyboard()
		#self.label.setFocus()
		#self.setWindowFlags(Qt.Qt.CustomizeWindowHint)
		
		windowFrame.setCentralWidget(self.centralWidget)
		self._retranslateUi(windowFrame)
		QtCore.QMetaObject.connectSlotsByName(windowFrame)
		#self.grabKeyboard()
		
	def _retranslateUi(self, windowFrame):
		_translate = QtCore.QCoreApplication.translate
		windowFrame.setWindowTitle(_translate("mainWindow", "keep alive!"))
		windowFrame.setWindowIcon(QtGui.QIcon(r'C:\Users\Oberon\Desktop\timg.png'))#* 在主界面标题前面插入图片，需要图片和程序在同一路径。
		
	def _initUI(self):
		self.backend = BackendThread()	# 创建线程
		self.backend.update_date.connect(self._handleDisplay)	# 连接信号
		self.thread = QThread()
		self.backend.moveToThread(self.thread)
		self.thread.started.connect(self.backend.run)	# 开始线程
		self.thread.start()

	def _handleDisplay(self, data):	# 将当前时间输出到文本框
		self.label.setText(data)
		
	def _keyPressEvent(self,event):
		if QKeyEvent.key()== Qt.Key_Esc: 
			self.close()
			
	def _closeEvent(self, event):
		event.ignore()  # 忽略关闭事件
		self.hide()
	
	def show(self):
		self.mainWindowFrame.show()
	

class BackendThread(QObject):
  # 通过类成员对象定义信号
	update_date = pyqtSignal(str)
  # 处理业务逻辑
	def labelPrint(self,s):
		#print("print")
		self.update_date.emit(s)
		
	def setParams(self):
		global params
		data = self.readData()
		if data == False:
			return 1
		self.param = params
		try:
			self.param['DDDDD'] = data[0]
			self.param['upass'] = data[1]
		except:
			return 2
		return 0
	
	def run(self):
		a = self.setParams()
		while not a == 0:
			if a == 1:
				self.labelPrint("      file lost")
				a = self.setParams()
			elif a == 2:
				self.labelPrint("invalid file")
				a = self.setParams()
		t_s=time.time()
		while True:
			t_e=time.time()
			if self.campusNetIsOk() :
				if not self.netIsOk()  : #如果没网
					self.labelPrint("    lost connection")	#显示没网
					#self.labelPrint(params['upass'])		#
					self.connectCampusNet()					#尝试联网
					t_s = time.time()
				else:
					pass
			else:
				self.labelPrint("    lost campus net")
			time.sleep(0.5)
			
	def campusNetIsOk(self):		#检查是否连接校园网
		testserver = ('59.67.0.245',80)
		s=socket.socket()
		s.settimeout(1)
		try:
			status = s.connect_ex(testserver)
			if status == 0:
				s.close()
				return True
			else:
				return False
		except Exception as e:
			#print("an error"+str(e))
			return False	

	def readData(self):			#读取用户数据
		p = self.dataIsExist()
		if p == False:
			return False
		with open(p,"r") as f :
			string = f.readlines()
		for i in range(len(string)):
			string[i] = string[i].strip()
		f.close()
		return string
	
	def netIsOk(self):		#检查能否上网
		testserver = ('www.baidu.com',443)
		s=socket.socket()
		s.settimeout(1)
		try:
			status = s.connect_ex(testserver)
			if status == 0:
				s.close()
				return True
			else:
				return False
		except Exception as e:
			#print("an error"+str(e))
			return False
	
	def connectCampusNet(self):		#连接校园网
		global param ,header
		url="http://59.67.0.245/a70.htm" 
		try:
			html=requests.post(url,data=params,headers = header , timeout = 1)
		except:
			self.labelPrint("	lost connection" , end = "")
			time.sleep(0.5)
		try:
			html.text.index("跳转至AC传递的用户原始输入地址")
		except ValueError:
			self.labelPrint("	login failed		 ")
		else:
			pass
			
	def dataIsExist(self):	#判断数据文件是否存在
		path = "_user.data"
		if not os.path.exists(path):
			path = r"C:\Users\Public\Documents\_user.data"
			if not os.path.exists(path):
				return False
			else:
				return path
		else:
			return path
		

		
if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)		#创建QT应用
	
	ui = mainWindow()	#创建主界面
	ui.show()			#显示主界面
	#mainWindow.hide()			#隐藏主界面
	
	sys.exit(app.exec_())	

	
