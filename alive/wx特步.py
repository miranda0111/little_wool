# !/bin/env python3
# -*- coding: utf-8 -*
"""
    感谢 一峰一燕 提供脚本以及技术支持

    项目名称: 特步 小程序
    Author: yml
    Date: 2022.7.8
    cron: 19 7 * * *    tebu.py
    new Env("特步");
    ================== 青龙--配置文件 ==================
    变量格式: export tebu_data=" ezr-vuid & ezr-st & ezr-ss & ezr-userid "   ,多账号用 换行 或 @ 分割

    【教程】:  需要自行用手机抓取 wxa-tp.ezrpro.com 域名的包 , ezr-vuid , ezr-st , ezr-ss , ezr-userid 是 headers 中的参数

"""
# ================================= 以下代码不懂不要随便乱动 ====================================
try:
    import requests
    import json
    import sys
    import os
    import re
    import time
except Exception as e:
    print(e)
requests.packages.urllib3.disable_warnings()
# --------------------------------------------------------------------------------------------
Script_Name = "特步"
Name_Pinyin = "tebu"
Script_Change = "特步商城签到 ,第一个 py 脚本"
Script_Version = "0.1.2"
Version_Check = "0.1.2"


# --------------------------------------------------------------------------------------------

def last_version(name, mold):
    url = ''
    if mold == 1:
        url = "https://raw.gh.fakev.cn/yml2213/Python/master/" + name + "/" + name + ".py"
    elif mold == 2:
        url = "http://yml-gitea.ml:2233/yml/JavaScript-yml/raw/branch/master/" + name + ".py"
    try:
        _url = url
        _headers = {}
        response = requests.get(url=_url, headers=_headers, verify=False)
        result = response.text
        r = re.compile(r'Version_Check = "(.*?)"')
        _data = r.findall(result)
        if not _data:
            return "出现未知错误 ,请稍后重试!"
        else:
            return _data[0]
    except Exception as err:
        print(err)


def mac_env(name):
    global ckArr
    pwd = os.path.dirname(os.path.abspath(__file__)) + os.sep
    path = pwd + ".env"
    with open(path, "r+") as f:
        env = f.read()
        if name in env:
            r = re.compile(r'tebu_data="(.*?)"', re.M | re.S | re.I)
            result = r.findall(env)
            # print(data[0])
            if "@" in result[0]:
                _ck = result[0].split("@")
                ckArr = _ck
            elif "\n" in result[0]:
                _ck = result[0].split("\n")
                ckArr = _ck
            else:
                ckArr = result
        else:
            print("检查变量" + name + "是否已填写")


def ql_env(name):
    global ckArr
    if name in os.environ:
        ckArr = []
        _data = os.environ[name]
        if "@" in _data:
            _ck = _data.split("@")
            ckArr = _ck
        elif "\n" in _data:
            _ck = _data.split("\n")
            ckArr = _ck
        else:
            ckArr = _data.split("@")


# mac_env("tebu_data")
ql_env("tebu_data")


class Script:
    def __init__(self, vuid, st, ss, userid):
        self.vuid = vuid
        self.st = st
        self.ss = ss
        self.userid = userid

    def sign_info(self):
        print("开始 签到信息")
        url_signinfo = "https://wxa-tp.ezrpro.com/myvip/Vip/SignIn/GetSignInDtlInfo"
        url_signin = "https://wxa-tp.ezrpro.com/myvip/Vip/SignIn/SignIn"
        payload = json.dumps({
            "ActId": 784,
            "ActRemindStatus": True
        })

        headers = {
            'Host': 'wxa-tp.ezrpro.com',
            'ezr-cop-id': '143',
            'ezr-vuid': self.vuid,
            'ezr-source': 'weapp',
            'ezr-st': self.st,
            'ezr-ss': self.ss,
            'ezr-userid': self.userid,
            'ezr-sv': '1',
            'ezr-brand-id': '254',
            'content-type': 'application/json'
        }
        try:
            response = requests.get(url=url_signinfo, headers=headers, verify=False)
            result = response.json()
            if result["Result"]["VipSignInDtl"]["IsSigInToday"]:
                print("签到: 您今天已经签到了 ,明天再来吧!")
                return
            elif not result["Result"]["VipSignInDtl"]["IsSigInToday"]:
                print("签到: 您今天未签到 ,去签到喽!")
            else:
                print("签到: 获取签到信息失败 ,请检查 变量 是否正确!")
        except Exception as err:
            print(err)

        try:
            response = requests.post(url=url_signin, headers=headers, data=payload, verify=False)
            result = response.json()
            # print(result)
            if result["Success"]:
                print("签到:" + result["Msg"]+" ,获得积分: " + result["Result"]["BonusValue"] + " 个!")
                return
            else:
                print("签到: 获取签到信息失败 ,请检查 变量 是否正确!")
        except Exception as err:
            print(err)


def tip():
    global ckArr
    print("================ 脚本只支持青龙新版 =================")
    print("============ 具体教程以请自行查看顶部教程 =============\n")
    print("🔔 " + Script_Name + " ,开始!")
    origin_version = last_version(Name_Pinyin, 1)
    print("📌 本地脚本: V " + Script_Version +
          "    远程仓库版本: V " + origin_version)
    print("📌 🆙 更新内容: " + Script_Change)
    print("共发现 " + str(len(ckArr)) + " 个账号!")


if __name__ == "__main__":
    global msg_info
    global ckArr
    tip()
    for inx, data in enumerate(ckArr):
        print("=============== 开始第" + str(inx + 1) + "个账号 ===============")
        ck = data.split("&")
        tebu = Script(ck[0], ck[1], ck[2], ck[3])
        tebu.sign_info()