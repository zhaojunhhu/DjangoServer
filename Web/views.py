#-*- coding:utf-8 -*-
from django.http import HttpResponse
from django.template import loader,Context
from .UdpSend import SendToUdpserver
import json,re

def SendOnu(request):
	data = {"CmdType":"AddOnu","data":{}}
	Mode = request.GET['Mode']
	Mac = request.GET['Mac']
	SSID = request.GET['SSID']
	SSIDPwd = request.GET['SSID-Pwd']
	UserPwd = request.GET['User-Pwd']
	SN = request.GET['SN']
	data["data"]["Mode"] = Mode
	data["data"]["Mac"] = Mac
	data["data"]["SSID"] = SSID
	data["data"]["SSID-Pwd"] = SSIDPwd
	data["data"]["User-Pwd"] = UserPwd
	data["data"]["SN"] = SN
	t = loader.get_template("addonu.html")
	ResponseOfServer = u"连接服务器失败！"
	try:
		Reult = SendToUdpserver(json.dumps(data))
		if Reult=='1001OK':
			ResponseOfServer = u"新增Onu设备成功"
		elif Reult=='2001NOK':
			ResponseOfServer = u"新增Onu设备失败！"
		elif Reult=='None':
			ResponseOfServer = u"连接服务器失败！"
	finally:
		AddOnuInfodata = u"当前提交信息为："+str(json.dumps(data))
		c = Context({"ResponseOfServer":ResponseOfServer,"AddOnuInfodata":AddOnuInfodata})
	return HttpResponse(t.render(c))

def Addonurun(request):
	data = {"CmdType":"OnuRun","OnumacAddr":"0000","data":{}}
	data["OnumacAddr"] = str(request.GET["macAddr"])
	data["data"]["FenFaBootFirst"] =  str(request.GET["A1"])
	data["data"]["FenFaRegisterFirst"] =  str(request.GET["A2"])
	data["data"]["YunYingBoot"] =  str(request.GET["AA1"])
	data["data"]["YunYingRegister"] =  str(request.GET["AA2"])
	data["data"]["YunYingHb"] =  str(request.GET["AA3"])
	data["data"]["YunYingRequestPlug"] =  str(request.GET["AA4"])
	data["data"]["ChaJianAA5"] =  str(request.GET["AA5"])
	data["data"]["ChaJianAA6"] =  str(request.GET["AA6"])
	t = loader.get_template("ceshi.html")
	ResponseOfCeshi = u"连接服务器失败！"
	try:
		Reult = SendToUdpserver(json.dumps(data))
		if Reult=='1001OK':
			ResponseOfCeshi = u"新增Onu测试信息成功"
		elif Reult=='2001NOK':
			ResponseOfCeshi = u"新增Onu测试信息失败！"
		elif Reult=='None':
			ResponseOfCeshi = u"连接服务器失败！"
	finally:
		AddOnuRun =u"当前提交信息为："+str(json.dumps(data))
		c = Context({"ResponseOfCeshi":ResponseOfCeshi,"AddOnuRun":AddOnuRun})
	return HttpResponse(t.render(c))

def AddOnuCmd(request):
	data = {"CmdType":"TestOnu","OnumacAddr":"0000","data":{}}
	Cmdinfo = re.findall("1=(.*)",request.GET['cmdinfo'])
	OnuMacAddr = str(request.GET["macAddr"])
	CmdName = str(Cmdinfo[1])
	CmdDate = str(Cmdinfo[2])
	OnuCmd = CmdName+ CmdDate +'}'
	OnuCmd = OnuCmd.replace('\n','').replace('\r','')
	data["OnumacAddr"] =  OnuMacAddr
	data["data"] = OnuCmd
	t = loader.get_template("wgnlcs.html")
	ResponseOfOnuRun = u"连接服务器失败！"
	try:
		Reult = SendToUdpserver(json.dumps(data))
		if Reult=='1001OK':
			ResponseOfOnuRun = u"新增Onu测试信息成功"
		elif Reult=='2001NOK':
			ResponseOfOnuRun = u"新增Onu测试信息失败！"
		elif Reult=='None':
			ResponseOfOnuRun = u"连接服务器失败！"
	finally:
		AddOnuCmddata =u"当前提交信息为："+str(json.loads((json.dumps(data))))
		c = Context({"ResponseOfOnuRun":ResponseOfOnuRun,"AddOnuCmddata":AddOnuCmddata})
	return HttpResponse(t.render(c))

def test(request):
	t = loader.get_template("test.html")
	c = Context({})
	return HttpResponse(t.render(c))
def main(request):
	t = loader.get_template("main.html")
	c = Context({})
	return HttpResponse(t.render(c))
def addonu(request):
	t = loader.get_template("addonu.html")
	c = Context({})
	return HttpResponse(t.render(c))

def index(request):
	t = loader.get_template("index.html")
	c = Context({})
	return HttpResponse(t.render(c))
def ceshi(request):
	t = loader.get_template("ceshi.html")
	c = Context({})
	return HttpResponse(t.render(c))
def wgnlcs(request):
	t = loader.get_template("wgnlcs.html")
	c = Context({})
	return HttpResponse(t.render(c))