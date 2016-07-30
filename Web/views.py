#-*- coding:utf-8 -*-
from django.http import HttpResponse
from django.template import loader,Context
from .UdpSend import SendToUdpserver
import json,re

####DiangoWeb查询设备录入信息
def FindOnu(request):
	data = {"CmdType":"FindOnu","OnumacAddr":"0000",}
	Mac = request.GET['FindMac']
	data["OnumacAddr"] = Mac
	t = loader.get_template("addonu.html")
	ResponseOfServerfind = ''
	try:
		Reult = SendToUdpserver(json.dumps(data))
		if Reult=='None':
			ResponseOfServerfind = u"连接服务器失败！"
			Reult = ''
		else:
			Reult = json.loads(Reult)
			ResultFindOnu = Reult["Result"]
			if ResultFindOnu == "-2":
				ResponseOfServerfind = u"查询设备信息输入有误！"
				Reult = ''
			elif ResultFindOnu == "-1":
				ResponseOfServerfind = u"当前设备未录入！"
				Reult = ''
			elif ResultFindOnu == "0":
				ResponseOfServerfind = u"查询设备信息如下："
				Reult = Reult["Info"]
				print Reult
	finally:
		c = Context({"ResponseOfServerfind":ResponseOfServerfind,"addonudatasfind":Reult})
	return HttpResponse(t.render(c))

###DiangoWeb新增测试设备请求
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
	ResponseOfServer = ''#连接提示信息
	try:
		Reult = SendToUdpserver(json.dumps(data))
		if Reult=='None':
			ResponseOfServer = u"连接服务器失败！"
			Reult = ''
		else:
			Reult = json.loads(Reult)
			ResultFindOnu = Reult["Result"]
			if ResultFindOnu == "-2":
				ResponseOfServer = u"查询设备信息输入有误！"
				Reult = data["data"]
			elif ResultFindOnu == "0":
				ResponseOfServer = u"查询设备信息录入成功！"
				Reult = data
			elif ResultFindOnu == "1":
				ResponseOfServer = u"查询设备信息修改成功！"
				Reult = data
	finally:
		c = Context({"ResponseOfServer":ResponseOfServer,"AddOnuInfodata":Reult})
	return HttpResponse(t.render(c))

####DiangoWeb异常流程对接测试请求
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
	ResponseOfCeshi = ''
	try:
		Reult = SendToUdpserver(json.dumps(data))
		if Reult=='None':
			ResponseOfCeshi = u"连接服务器失败！"
			Reult = ''
		else:
			Reult = json.loads(Reult)
			ResultFindOnu = Reult["Result"]
			if ResultFindOnu == "0":
				ResponseOfCeshi = u"测试设备请求成功！"
				Reult = data["data"]
			elif ResultFindOnu == "-1":
				ResponseOfCeshi = u"测试设备未录入！"
				Reult = u"错误设备信息："+data["OnumacAddr"]
			elif ResultFindOnu == "-2":
				ResponseOfCeshi = u"测试设备信息有错误！"
				Reult = u"错误设备信息："+data["OnumacAddr"]
	finally:
		c = Context({"ResponseOfCeshi":ResponseOfCeshi,"AddOnuRun":Reult})
	return HttpResponse(t.render(c))

####DiangoWeb网关能力测试请求
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
	ResponseOfOnuRun = ''
	try:
		Reult = SendToUdpserver(json.dumps(data))
		if Reult=='None':
			ResponseOfOnuRun = u"连接服务器失败！"
			Reult = ''
		else:
			Reult = json.loads(Reult)
			ResultFindOnu = Reult["Result"]
			if ResultFindOnu == "0":
				ResponseOfOnuRun = u"测试设备请求成功！"
				Reult = data["data"]
			elif ResultFindOnu == "-1":
				ResponseOfOnuRun = u"测试设备未录入！"
				Reult = u"错误设备信息："+data["OnumacAddr"]
			elif ResultFindOnu == "-2":
				ResponseOfOnuRun = u"测试设备信息有错误！"
				Reult = u"错误设备信息："+data["OnumacAddr"]
	finally:
		c = Context({"ResponseOfOnuRun":ResponseOfOnuRun,"AddOnuCmddata":Reult})
	return HttpResponse(t.render(c))

###DiangoWeb获取测试设备快照
def GetKuaiZhao(request):
	data = {"CmdType":"GetTestOnuInfo","OnumacAddr":"0000"}
	data["OnumacAddr"] = str(request.GET["FindMac"])
	t = loader.get_template("kuaizhao.html")
	ResponseOfServerfind = ''
	try:
		Reult = SendToUdpserver(json.dumps(data))
		if Reult=='None':
			ResponseOfServerfind = u"连接服务器失败！"
			Reult = ''
		else:
			Reult = json.loads(Reult)
			ResultFindOnu = Reult["Result"]
			if ResultFindOnu == "0":
				ResponseOfServerfind = u"测试设备请求成功！"
				Reult = Reult["TestInfo"]["Flag"]
			elif ResultFindOnu == "1":
				ResponseOfServerfind = u"查询设备不属于待测试设备"
				Reult = ''
			elif ResultFindOnu == "-1":
				ResponseOfServerfind = u"测试设备未录入！"
				Reult = u"错误设备信息："+data["OnumacAddr"]
			elif ResultFindOnu == "-2":
				ResponseOfServerfind = u"测试设备信息有错误！"
				Reult = u"错误设备信息："+data["OnumacAddr"]
	finally:
		c = Context({"ResponseOfServerfind":ResponseOfServerfind,"addonudatasfind":Reult})
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
def kuaizhao(request):
	t = loader.get_template("kuaizhao.html")
	c = Context({})
	return HttpResponse(t.render(c))
