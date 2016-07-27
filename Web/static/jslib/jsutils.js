function addmac(){
	var macAddr = $.trim($("#macAddr").val());
	var sn = $.trim($("#sn").val());
	var ssidName = $.trim($("#ssidName").val());
	var ssidPass = $.trim($("#ssidPass").val());
	var userPass = $.trim($("#userPass").val());
	if(isNullOrEmpty(macAddr)){
		alert("请填写网关MAC");
	}else if(isNullOrEmpty(sn)){
		alert("请填写网关序列号");
	}else if(isNullOrEmpty(ssidName)){
		alert("请填写设备SSID名称");
	}else if(isNullOrEmpty(ssidPass)){
		alert("请填写设备SSID密码");
	}else if(isNullOrEmpty(userPass)){
		alert("请填写设备管理员密码");
	}else{
		try{ 
			$.ajax({
				cache:false,
				url:'addMac.action',
				type:'post',
				dataType:'json',
				data:{macAddr:macAddr,sn:sn,ssidName:ssidName,ssidPass:ssidPass,userPass:userPass},
				success:function(json){
					var dataJson = eval("("+json.dataJson+")");////包数据解析为json 格式
					if(dataJson!=null){
						if(dataJson.result=='0'){
							if(confirm(dataJson.resultMsg+"是否继续添加！")){
								window.location.href="mac_add.jsp";
							}else{
								window.location.href="macList.action";
							}
						} else {
							alert(dataJson.resultMsg);
						}
					}else{
						alert('系统没有返回');
					}
				},
				error:function(XMLHttpRequest, textStatus, errorThrown){
					alert('zhiding errorThrown+"===="+textStatus');
				}
			});
		}catch(e){alert(e.message)}
	}
}
function updatemac(){
	var id = $.trim($("#id").val());
	var macAddr = $.trim($("#macAddr").val());
	var sn = $.trim($("#sn").val());
	var ssidName = $.trim($("#ssidName").val());
	var ssidPass = $.trim($("#ssidPass").val());
	var userPass = $.trim($("#userPass").val());
	if(isNullOrEmpty(macAddr)){
		alert("请填写网关MAC");
		alert(macAddr);
	}else if(isNullOrEmpty(sn)){
		alert("请填写网关序列号");
	}else if(isNullOrEmpty(ssidName)){
		alert("请填写设备SSID名称");
	}else if(isNullOrEmpty(ssidPass)){
		alert("请填写设备SSID密码");
	}else if(isNullOrEmpty(userPass)){
		alert("请填写设备管理员密码");
	}else{
		try{ 
			$.ajax({
				cache:false,
				url:'updateMac.action',
				type:'post',
				dataType:'json',
				data:{id:id,macAddr:macAddr,sn:sn,ssidName:ssidName,ssidPass:ssidPass,userPass:userPass},
				success:function(json){
					var dataJson = eval("("+json.dataJson+")");////包数据解析为json 格式
					if(dataJson!=null){
						if(dataJson.result=='0'){
							alert(dataJson.resultMsg);
							window.location.href="macList.action";
						} else {
							alert(dataJson.resultMsg);
						}
					}else{
						alert('系统没有返回');
					}
				},
				error:function(XMLHttpRequest, textStatus, errorThrown){
					alert('zhiding errorThrown+"===="+textStatus');
				}
			});
		}catch(e){alert(e.message)}
	}
}

function delmac(index){
	var id = $.trim($("#id_"+index).val());
	var macAddr = $.trim($("#macAddr_"+index).val());
	try{
		$.ajax({
			cache:false,
			url:'delMac.action',
			type:'post',
			dataType:'json',
			data:{id:id,macAddr:macAddr},
			success:function(json){
				var dataJson = eval("("+json.dataJson+")");////包数据解析为json 格式
				if(dataJson!=null){
					if(dataJson.result=='0'){
						alert(dataJson.resultMsg);
						window.location.href="macList.action";
					} else {
						alert(dataJson.resultMsg);
					}
				}else{
					alert('系统没有返回');
				}
			},
			error:function(XMLHttpRequest, textStatus, errorThrown){
				alert('zhiding errorThrown+"===="+textStatus');
			}
		});
	}catch(e){alert(e.message)}
}

function getMacList(){
	try{ 
		$.ajax({
			cache:false,
			url:'list.action',
			type:'post',
			dataType:'json',
			success:function(json){
				var macList=json.macList;
				if(macList!=null){
					for(var i in macList){
						$("#macListID").append("<option value='"+macList[i].MAC_ADDR+"' selected>"+macList[i].MAC_ADDR+"</option>");
					}
				}
			},
			error:function(XMLHttpRequest, textStatus, errorThrown){
				alert("GET MAC LIST error!"+errorThrown+"===="+textStatus);
			}
		});
	}catch(e){alert(e)}
}

function tableswitch(index){
	if(index==1){
		$("#operate_id").show();
		$("#route_id").hide();
		$("#div_operate_id").removeClass().addClass("ce-button");
		$("#div_route_id").removeClass().addClass("ce-none");
	}else{
		$("#operate_id").hide();
		$("#route_id").show();
		$("#div_operate_id").removeClass().addClass("ce-none");
		$("#div_route_id").removeClass().addClass("ce-button");
	}
}

//调用反向触发网关连接到插件中心、反向触发重新注册
function trigger_gateway(type){
	try{ 
		var mac= $("#mac").val();
		$.ajax({
			cache:false,
			url:'triggerAction.action',
			type:'post',
			dataType:'json',
			data:{macAddr:mac,type:type},
			success:function(json){
				var dataJson = eval("("+json.dataJson+")");////包数据解析为json 格式
				if(dataJson!=null){
					alert(dataJson.resultMsg);
				}else{
					alert('系统没有返回');
				}
			},
			error:function(XMLHttpRequest, textStatus, errorThrown){
				alert("GET MAC LIST error!"+errorThrown+"===="+textStatus);
			}
		});
	}catch(e){alert(e)}
}
//
function trigger_gateway_disconnect(){
	try{ 
		var mac= $("#mac").val();
		$.ajax({
			cache:false,
			url:'disconnect.action',
			type:'post',
			dataType:'json',
			data:{macAddr:mac},
			success:function(json){
				var dataJson = eval("("+json.dataJson+")");////包数据解析为json 格式
				if(dataJson!=null){
					alert(dataJson.resultMsg);
				}else{
					alert('系统没有返回');
				}
			},
			error:function(XMLHttpRequest, textStatus, errorThrown){
				alert("GET MAC LIST error!"+errorThrown+"===="+textStatus);
			}
		});
	}catch(e){alert(e)}
}

function checkSubmit(){
	var mac= $("#macID").val();
	if(isNullOrEmpty(mac)){
		alert("请选择测试的网关MAC");
		return false;
	}else{
		return true;
	}
}

function isNullOrEmpty(strVal) {
	if (strVal == '' || strVal == null || strVal == undefined) {
		return true;
	} else {
		return false;
	}
}

if(typeof FileReader == 'undefined'){	//判断浏览器是否支持FileReader接口
	var div=document.getElementById("dd");
	div.innerHTML='你的浏览器不支持FileReader接口！';
	document.getElementById("file").setAttribute("disabled","disabled");
	document.getElementById("filea").setAttribute("disabled","disabled");
	document.getElementById("fileb").setAttribute("disabled","disabled");
}

function bShow(){
	var file=document.getElementById("fileb").files[0];
	if(file){
		var reader=new FileReader();
		reader.onload=function(e){
			var conb=document.getElementById("contentb");
			conb.innerHTML=e.target.result;
		}
	}
	reader.readAsText(file);
 }