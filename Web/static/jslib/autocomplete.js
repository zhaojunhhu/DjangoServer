var oInputField;  
var oPopDiv;
var oColorsUl;
var searchType;
function initVars(){
	//初始化变量
	oInputField = document.getElementById("macID");
	oPopDiv = document.getElementById("mac_popup");
	oColorsUl = document.getElementById("mac_popup_ul");
}
function findMacs(){
	initVars();  //初始化变量
	if(oInputField.value.length > 0){
		var aResult = new Array();  //用于存放匹配结果
		//根据关键字去后台进行查询
		var mac = $.trim($("#macID").val());
		if(mac!=""){
			$.ajax({
				cache:false,
				url:'list.action',
				type:'post',
				dataType:'json',
				data:{mac:mac},
				success:function(json){
					var macList=json.macList;
					for(var i = 0 ; i < macList.length ; i++ ){
						//必须是从单词的开始处匹配
//						if(keywordList[i].NAME.indexOf(oInputField.value) == 0)
							aResult.push(macList[i].MAC_ADDR); //加入结果
					}
					if(aResult.length > 0){  //如果有匹配的颜色则显示出来
						setColors(aResult);
					}else{                        //否则就清除、用户多输入一个字母
						clearColors();  //就有可能从有匹配到无、到无的时候需要清除
					}
				},
				error:function(XMLHttpRequest, textStatus, errorThrown){
					//alert("keywordAutoComplete error!"+errorThrown+"===="+textStatus);
				}
			});
		}
	}
	else
		clearColors(); //无输入时清除提示框
}


function clearColors(){
	//清除提示内容
	for(var i = oColorsUl.childNodes.length - 1 ; i >= 0 ;i--){
		oColorsUl.removeChild(oColorsUl.childNodes[i]);
	}
	oPopDiv.className = "hide" ;
}

function setColors(the_colors){
	//显示提示框、传入的参数即为匹配出来的结果组成的数组
	clearColors();  //没输入一个字母就先清楚原先的提示、再继续
	oPopDiv.className = "show" ;
	var oLi ;
	for(var i = 0 ; i < the_colors.length ; i++ ){
		//将匹配的提示结果逐一显示给用户
		oLi = document.createElement("li");
		oColorsUl.appendChild(oLi);
		oLi.appendChild(document.createTextNode(the_colors[i]));
		
		oLi.onmouseover = function(){
			this.className = "mouseOver" ;  //鼠标指针经过时高亮
		}
		oLi.onmouseout = function(){
			this.className = "mouseOut" ;   //鼠标指针离开时恢复原样
		}
		oLi.onclick = function(){
			//用户单击某个匹配项时、设置输入框为该项的值
			oInputField.value = this.firstChild.nodeValue;
			clearColors();  //同时清除提示框
		}
	}
}