/*
撸现金-赚点是点
{支付宝小程序}

一天1-2毛    自动提现 到账支付宝余额

（金币自动提现非秒到-手提秒到）

https://json.dd-gz.com/ 域名的任意链接  抓链接末尾token和userid 的值

用#分开两个值

用 @  分割多账户

例如抓到域名  https://json.dd-gz.com/zhuandianshidian/public/api.php/user/userinfo?  

假如末尾是 token=123&userid=456   

则 青龙变量     用 @  分割多账户

export zdcookie='123#456'    

v2p 圈×变量  zdcookie
*/
const $ = Env('撸现金-赚点是点')
let jsname = "\u8D5A\u70B9\u662F\u70B9",
	ck = ($.isNode() ? process.env.zdcookie : $.getdata("zdcookie")) || "",
	ckArr = [],
	envSplitor = ["@"];
async function checkEnv() {
	if (ck)
		for (let a of ck.split("@")) a && ckArr.push(a);
	else if (console.log("\u672A\u627E\u5230\u8D26\u53F7\u6570\u636E"), ckArr.length < 1) return;
	return console.log(`共找到${ckArr.length}个账号`), !0
}
async function userinfo(a, b) {
	try {
		let e;
		await httpRequest("get", populateUrlObject(`https://json.dd-gz.com/zhuandianshidian/public/api.php/user/userinfo?token=${a}&userid=${b}`, ""));
		let c = httpResult;
		1 == c.state && (this.cash = c.data.money_zc, console.log(jsname + ` 当前金币 ：${this.cash} `), await timeMoney(a, b)), this.cash >= 1e3 && (console.log(jsname + ` 开始提现 ：${1e-4*this.cash} 元`), await addMoney(a, b))
	} catch (d) {
		console.log(d)
	} finally {
		return new Promise(a => {
			a(1)
		})
	}
}
async function addMoney(a, b) {
	try {
		let e;
		await httpRequest("get", populateUrlObject(`https://json.dd-gz.com/zhuandianshidian/public/api.php/user/addMoney?price=${this.cash}&token=${a}&userid=${b}`, ""));
		let c = httpResult;
		1 == c.state && console.log(`兑换成功`)
	} catch (d) {
		console.log(d)
	} finally {
		return new Promise(a => {
			a(1)
		})
	}
}
async function timeMoney(b, c) {
	try {
		let f;
		await httpRequest("get", populateUrlObject(`https://json.dd-gz.com/zhuandianshidian/public/api.php/integral/timeMoney?token=${b}&userid=${c}`, ""));
		let a = httpResult;
		if (1 == a.state) console.log(jsname + ` 开始领取金币 ：${a.data.priceMsg}`);
		else if (0 == a.state) {
			var d = a.msg.replace(/[^\d]/g, "");
			console.log(jsname + ` 开始领取金币 ：还需要等待${d}秒`)
		}
	} catch (e) {
		console.log(e)
	} finally {
		return new Promise(a => {
			a(1)
		})
	}
}

function populateUrlObject(a, b = "") {
	let d = a.replace("//", "/").split("/")[1],
		c = {
			url: a,
			headers: {
				Referer: "https://2021002117637233.hybrid.alipay-eco.com/2021002117637233/0.2.2206021449.52/index.html#pages/userduihuan/tixian/tixian?__appxPageId=6",
				Host: d,
				Connection: "keep-alive",
				"Content-Type": "application/json",
				"Tinyapp-Intercept": "tiny",
				"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18H17 Ariver/1.1.0 AliApp(AP/10.2.56.6000) Nebula WK RVKType(0) AlipayDefined(nt:4G,ws:414|832|2.0) AlipayClient/10.2.56.6000 Language/zh-Hans Region/CN NebulaX/1.0.0"
			},
			timeout: 5e3
		};
	return b && (c.body = b), c
}
async function httpRequest(a, b) {
	return httpResult = null, httpReq = null, httpResp = null, new Promise(c => {
		$.send(a, b, async (d, e, b) => {
			try {
				if (httpReq = e, httpResp = b, d) console.log(`${a}请求失败`), console.log(d);
				else if (b.body) {
					if ("object" == typeof b.body) httpResult = b.body;
					else try {
						httpResult = JSON.parse(b.body)
					} catch (f) {
						httpResult = b.body
					}
				}
			} catch (g) {} finally {
				c()
			}
		})
	})
}

function safeGet(a) {
	try {
		if ("object" == typeof JSON.parse(a)) return !0;
		console.log(a)
	} catch (b) {
		return console.log(b), console.log(`服务器访问数据为空，请检查自身设备网络情况`), !1
	}
}

function add() {
	var a = arguments,
		b = (a.length, 0),
		d = 0;
	for (var c in a) {
		var e = "" + a[c];
		if (-1 != e.indexOf(".")) {
			var f = e.split(".")[1].length;
			b = b < f ? f : b
		}
	}
	var g = Math.pow(10, b);
	for (var c in a) d += a[c] * g;
	return d / g
}

function randomNum(a, b) {
	switch (arguments.length) {
		case 1:
			return parseInt(Math.random() * a + 1, 10);
		case 2:
			return parseInt(Math.random() * (b - a + 1) + a, 10);
		default:
			return 0
	}
}

function Env(a,b){return"undefined"!=typeof process&&JSON.stringify(process.env).indexOf("GITHUB")> -1&&process.exit(0),new class{constructor(a,b){this.name=a,this.notifyStr="",this.startTime=(new Date).getTime(),Object.assign(this,b),console.log(`${this.name} 开始运行：
`)}isNode(){return"undefined"!=typeof module&&!!module.exports}isQuanX(){return"undefined"!=typeof $task}isSurge(){return"undefined"!=typeof $httpClient&&"undefined"==typeof $loon}isLoon(){return"undefined"!=typeof $loon}getdata(b){let a=this.getval(b);if(/^@/.test(b)){let[,c,f]=/^@(.*?)\.(.*?)$/.exec(b),d=c?this.getval(c):"";if(d)try{let e=JSON.parse(d);a=e?this.lodash_get(e,f,""):a}catch(g){a=""}}return a}setdata(c,d){let a=!1;if(/^@/.test(d)){let[,b,e]=/^@(.*?)\.(.*?)$/.exec(d),f=this.getval(b),i=b?"null"===f?null:f||"{}":"{}";try{let g=JSON.parse(i);this.lodash_set(g,e,c),a=this.setval(JSON.stringify(g),b)}catch(j){let h={};this.lodash_set(h,e,c),a=this.setval(JSON.stringify(h),b)}}else a=this.setval(c,d);return a}getval(a){return this.isSurge()||this.isLoon()?$persistentStore.read(a):this.isQuanX()?$prefs.valueForKey(a):this.isNode()?(this.data=this.loaddata(),this.data[a]):this.data&&this.data[a]||null}setval(b,a){return this.isSurge()||this.isLoon()?$persistentStore.write(b,a):this.isQuanX()?$prefs.setValueForKey(b,a):this.isNode()?(this.data=this.loaddata(),this.data[a]=b,this.writedata(),!0):this.data&&this.data[a]||null}send(b,a,f=()=>{}){if("get"!=b&&"post"!=b&&"put"!=b&&"delete"!=b){console.log(`无效的http方法：${b}`);return}if("get"==b&&a.headers?(delete a.headers["Content-Type"],delete a.headers["Content-Length"]):a.body&&a.headers&&(a.headers["Content-Type"]||(a.headers["Content-Type"]="application/x-www-form-urlencoded")),this.isSurge()||this.isLoon()){this.isSurge()&&this.isNeedRewrite&&(a.headers=a.headers||{},Object.assign(a.headers,{"X-Surge-Skip-Scripting":!1}));let c={method:b,url:a.url,headers:a.headers,timeout:a.timeout,data:a.body};"get"==b&&delete c.data,$axios(c).then(a=>{let{status:b,request:c,headers:d,data:e}=a;f(null,c,{statusCode:b,headers:d,body:e})}).catch(a=>console.log(a))}else if(this.isQuanX())a.method=b.toUpperCase(),this.isNeedRewrite&&(a.opts=a.opts||{},Object.assign(a.opts,{hints:!1})),$task.fetch(a).then(a=>{let{statusCode:b,request:c,headers:d,body:e}=a;f(null,c,{statusCode:b,headers:d,body:e})},a=>f(a));else if(this.isNode()){this.got=this.got?this.got:require("got");let{url:d,...e}=a;this.instance=this.got.extend({followRedirect:!1}),this.instance[b](d,e).then(a=>{let{statusCode:b,request:c,headers:d,body:e}=a;f(null,c,{statusCode:b,headers:d,body:e})},b=>{let{message:c,response:a}=b;f(c,a,a&&a.body)})}}time(a){let b={"M+":(new Date).getMonth()+1,"d+":(new Date).getDate(),"h+":(new Date).getHours(),"m+":(new Date).getMinutes(),"s+":(new Date).getSeconds(),"q+":Math.floor(((new Date).getMonth()+3)/3),S:(new Date).getMilliseconds()};for(let c in/(y+)/.test(a)&&(a=a.replace(RegExp.$1,((new Date).getFullYear()+"").substr(4-RegExp.$1.length))),b)new RegExp("("+c+")").test(a)&&(a=a.replace(RegExp.$1,1==RegExp.$1.length?b[c]:("00"+b[c]).substr((""+b[c]).length)));return a}async showmsg(){if(!this.notifyStr)return;let a=this.name+" \u8FD0\u884C\u901A\u77E5\n\n"+this.notifyStr;if($.isNode()){var b=require("./sendNotify");console.log("\n============== \u63A8\u9001 =============="),await b.sendNotify(this.name,a)}else this.msg(a)}logAndNotify(a){console.log(a),this.notifyStr+=a,this.notifyStr+="\n"}msg(d=t,a="",b="",e){let f=a=>{if(!a)return a;if("string"==typeof a)return this.isLoon()?a:this.isQuanX()?{"open-url":a}:this.isSurge()?{url:a}:void 0;if("object"==typeof a){if(this.isLoon()){let b=a.openUrl||a.url||a["open-url"],c=a.mediaUrl||a["media-url"];return{openUrl:b,mediaUrl:c}}if(this.isQuanX()){let d=a["open-url"]||a.url||a.openUrl,e=a["media-url"]||a.mediaUrl;return{"open-url":d,"media-url":e}}if(this.isSurge())return{url:a.url||a.openUrl||a["open-url"]}}};this.isMute||(this.isSurge()||this.isLoon()?$notification.post(d,a,b,f(e)):this.isQuanX()&&$notify(d,a,b,f(e)));let c=["","============== \u7CFB\u7EDF\u901A\u77E5 =============="];c.push(d),a&&c.push(a),b&&c.push(b),console.log(c.join("\n"))}getMin(a,b){return a<b?a:b}getMax(a,b){return a<b?b:a}padStr(e,b,f="0"){let a=String(e),g=b>a.length?b-a.length:0,c="";for(let d=0;d<g;d++)c+=f;return c+a}json2str(b,e,f=!1){let c=[];for(let d of Object.keys(b).sort()){let a=b[d];a&&f&&(a=encodeURIComponent(a)),c.push(d+"="+a)}return c.join(e)}str2json(e,f=!1){let d={};for(let a of e.split("&")){if(!a)continue;let b=a.indexOf("=");if(-1==b)continue;let g=a.substr(0,b),c=a.substr(b+1);f&&(c=decodeURIComponent(c)),d[g]=c}return d}randomString(d,a="abcdef0123456789"){let b="";for(let c=0;c<d;c++)b+=a.charAt(Math.floor(Math.random()*a.length));return b}randomList(a){let b=Math.floor(Math.random()*a.length);return a[b]}wait(a){return new Promise(b=>setTimeout(b,a))}done(a={}){let b=((new Date).getTime()-this.startTime)/1e3;console.log(`
${this.name} 运行结束，共运行了 ${b} 秒！`),(this.isSurge()||this.isQuanX()||this.isLoon())&&$done(a)}}(a,b)}(async()=>{if("undefined"!=typeof $request);else{if(!await checkEnv())return;let a=0;for(let c of ckArr){a+=1,console.log(`
=============账号${a}=============
`);let b=c.split("#"),d=b[0],e=b[1];await userinfo(d,e)}}})().catch(a=>console.log(a)).finally(()=>$.done())
