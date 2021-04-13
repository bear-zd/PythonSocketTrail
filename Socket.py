import socket as ss
import ui_Server as UIS
import ui_client as UIC
from threading import Thread  # 导入线程函数
import sys
from time import sleep

#class Window():
#    CliStatus=-1
#    def __init__(self):
#        self.Server=UIS.Ui_MainWindow()
#        self.Client=

class Client():

    def __init__(self): #构造函数
        App = UIC.QApplication(['Client'])
        self.ClientWindow = UIC.Ui_MainWindow() #创建UI类
        self.CliMainWindow = UIC.QMainWindow() #创建窗口类
        self.ClientWindow.setupUi(self.CliMainWindow) #将UI类绑定在窗口上
        self.CliMainWindow.show() #窗口展示
        self.CliStatus = -1
        AppThread=Thread(target=self.__wait__)
        AppThread.start()
        App.exec()
        App.processEvents()

    def __wait__(self):
        print('Waiting!')
        while 1:
            if self.ClientWindow.pushButton.isDown():
                self.__connect__()
            while self.CliStatus==1:
                if self.CliMainWindow.pushButton_3.isDown():
                    self.__sendMessage__()
                if self.CliMainWindow.pushButton_2.isDown():
                    self.__close__()
                    return

    def __connect__(self): #连接函数
        self.__showMessage__('Connecting...')
        self.Cs=ss.socket() #创建套接字
        Cip=self.ClientWindow.textEdit_4.toPlainText() #获取主机名称
        if Cip=='如果不输入，则默认为本地ip':
            Cip=ss.gethostname()
        Cport=int(self.ClientWindow.textEdit.toPlainText()) #获取端口号
        try:
            self.Cs.connect((Cip,Cport)) #尝试连接
            self.ClientWindow.pushButton.setText('Connected')
            self.CliStatus=1
            self.__showMessage__('Connected')
            #self.Cs.sendall('用户连接'.encode('utf-8'))
            #Thread(target=self.__listen__()).start()
            self.__listen__()
        except ConnectionRefusedError:
            self.__showMessage__('错误的地址或者服务器未开启')


    def __sendMessage__(self): #发送信息
            Message=self.ClientWindow.textEdit_3.toPlainText()
            self.Cs.sendall(Message.encode('utf-8'))
            self.ClientWindow.textEdit_3.setText('')

    def __showMessage__(self,Message): #展示信息
        self.ClientWindow.textBrowser_2.append(Message)

    def __listen__(self): #监听
        while self.CliStatus==1:
            sleep(2)
            RecMessage=self.Cs.recv(1024).decode('utf-8')
            print('One loop')
            if RecMessage!='':
                print(RecMessage)
                self.__showMessage__(RecMessage)
            if self.ClientWindow.pushButton_2.isDown():
                self.__close__()


    def __close__(self):
        self.CliStatus=0
        self.Cs.close()
        sys.exit(self.CliMainWindowApp)




class Server():
    def __init__(self):  # 构造函数
        AppS = UIC.QApplication(['Server'])
        self.ServerWindow = UIS.Ui_MainWindow()  # 创建UI类
        self.SerMainWindow = UIS.QMainWindow()  # 创建窗口类
        self.ServerWindow.setupUi(self.SerMainWindow)  # 将UI类绑定在窗口上
        self.SerMainWindow.show()  # 窗口展示
        #self.ServerWindow.pushButton.clicked.connect(self.__start__) #按钮一绑定open
        #self.ServerWindow.pushButton_2.clicked.connect(self.__close__)  #按钮二绑定close
        #self.ServerWindow.pushButton_3.clicked.connect(self.__send__) #按钮三绑定send
        #self.Serstatus = -1
        AppSThread = Thread(target=self.__wait__)
        AppSThread.start()
        AppS.exec()
        AppS.processEvents()

    def __wait__(self):
        print('Waiting!')
        while self.Serstatus==-1:
            if self.ServerWindow.pushButton.isDown():
                self.__start__()
            if self.ServerWindow.pushButton_2.isDown():
                self.__close__(flag=1)

    def __start__(self):
        self.__showMessage__('Opening...')
        self.Ss = ss.socket()  # 创建套接字
        Sip = ss.gethostname()
        self.ServerWindow.label_2.setText(Sip)
        Sport = int(self.ServerWindow.textEdit.toPlainText())  # 获取端口号
        try:
            self.Ss.bind((Sip, Sport))
            self.Ss.listen()
            self.ServerWindow.pushButton.setText('opened')
            self.__showMessage__('Server opend!')
            Serstatus=1
            self.__listen__()
        except ss.error:
            return

    def __showMessage__(self,Message): #展示信息
        self.ServerWindow.textBrowser_2.append(Message)

    def __listen__(self):
        self.Ss.listen()
        c, addr = self.Ss.accept()  # 建立客户端连接
        self.__showMessage__('连接地址：'+addr[0]+':'+str(addr[1]))
        string = '欢迎访问'
        string = string.encode()
        c.send(string) # 发送消息
        self.__listening__(c)

    def __listening__(self,c):
        while self.Serstatus:
            if self.ServerWindow.pushButton_2.isChecked():
                self.__close__(flag=0)
            #Message = ss.recv(1024)
            #if Message:
            #    self.__showMessage__(Message.decode('utf-8'))
            if self.ServerWindow.pushButton_3.isChecked():
                self.__send__(c)
                print('pushButtonClicked!')



    def __close__(self,flag):
        if flag==1:
            sys.exit(self.SerMainWindowApp)
            return
        else :
            Serstatus = 0
            self.Ss.close()
            sys.exit(self.SerMainWindowApp)
            return

    def __send__(self,com):
        Message = self.ServerWindow.textEdit_2.toPlainText()
        print(Message)
        com.send(Message.encode('utf-8'))
        #self.ServerWindow.textEdit_2.clear()


