# !/bin/env python3
# -*- coding: utf-8 -*
"""
    new Env("预言")
    Name: 预言  网页     虚拟币,自己零撸  被坑了钱别找我
    Author: yml
    Date: 2022.8.17
    cron: 4 7,12 * * *    prophecy.py

    邀请链接: https://wprophecy.com/#/register?refId=f02c05c4b481c3a1&redirectTo=/app/home&fullscreen=Y
    邀请码: f02c05c4b481c3a1    感谢支持


    8.17    每日签到, 每天随机预言无战争   最大礼金投入
    ================== 青龙--配置文件 ==================
    变量格式: export prophecy_data=" rem_token @ rem_token "    多账号用 换行 或 @ 分割

    教程:  电脑浏览器f12 抓取 wprophecy.com  域名的包, cookie中 rem_token  只要这一个就行

    脚本：https://raw.githubusercontent.com/yml2213/Python/master/prophecy/prophecy.py    

new Env("预言")
    Name: 预言  网页     虚拟币,自己零撸  被坑了钱别找我
    Author: yml
    Date: 2022.8.17
    cron: 4 7,12 * * *    prophecy.py

    邀请链接: https://wprophecy.com/#/register?refId=f02c05c4b481c3a1&redirectTo=/app/home&fullscreen=Y
    邀请码: f02c05c4b481c3a1    感谢支持


    8.17    每日签到, 每天随机预言无战争   最大礼金投入
    ================== 青龙--配置文件 ==================
    变量格式: export prophecy_data=" rem_token @ rem_token "    多账号用 换行 或 @ 分割

    教程:  电脑浏览器f12 抓取 wprophecy.com  域名的包, cookie中 rem_token  只要这一个就行

脚本在泄露出去，那以后就只有偷撸了
"""
# ================================= 以下代码不懂不要随便乱动 ====================================
try:
    import requests
    import json
    import sys
    import os
    import re
    import time
    import random
except Exception as e:
    print(e)
requests.packages.urllib3.disable_warnings()
# --------------------------------------------------------------------------------------------
Script_Name = "预言"
Name_Pinyin = "prophecy"
Script_Change = "每日签到, 每天随机预言无战争   最大礼金投入"
Script_Version = "0.1.2"
# --------------------------------------------------------------------------------------------


def _env():   # 环境配置
    # mac_env(f"{Name_Pinyin}_data")
    ql_env(f"{Name_Pinyin}_data")


def start():
    for inx, data in enumerate(ckArr):
        msg("=============== 开始第" + str(inx + 1) + "个账号 ===============")
        ck = data.split("&")
        # print(ck[0])
        # print(ck[1])
        prophecy = Script(ck[0])
        prophecy.csrf_token("获取token")
        prophecy.user_info("用户信息")
        prophecy.do_sign("签到")


class Script:
    def __init__(self, rem_token):
        self.rem_token = rem_token

    def url(self, name):  # hostname + xxxx
        url = f"https://wprophecy.com/{name}"
        return url

    def get_cookie(self):
        global cookie_y, token_y
        url = 'https://wprophecy.com/getCSRFToken'
        payload = {}
        headers = {
            'cookie': f'REM_TOKEN={self.rem_token}',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36'
        }
        try:
            res = requests.request("GET", url, headers=headers, data=payload)
            result = res.json()
            token_y = result['data']['CSRF-TOKEN']
            cookies = res.cookies
            cookie = requests.utils.dict_from_cookiejar(cookies)
            cookie_data = cookie['WAR_PROPHECY']
            cookie_y = f"WAR_PROPHECY={cookie_data}; REM_TOKEN={self.rem_token}"
            # print(cookie_y)
            # print(token_y)
        except Exception as err:
            print('获取cookie失败:\n{0}'.format(err))

    def headers_one(self):
        headers = {
            'accept': 'application/json, text/plain, */*',
            'cookie': self.get_cookie()
        }
        # print(headers)
        return headers

    def headers(self):
        global cookie_y, token_y
        headers = {
            'accept': 'application/json, text/plain, */*',
            'cookie': cookie_y,
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36',
            'CSRF-TOKEN': token_y
        }
        # print(headers)
        return headers

    def headers2(self):
        global cookie_y, token_y
        headers2 = {
            'accept': 'application/json, text/plain, */*',
            'cookie': cookie_y,
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36',
            'CSRF-TOKEN': token_y,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        # print(headers2)
        return headers2

    def csrf_token(self, name="更新 csrf-token"):  # 获取 csrf-token
        try:
            response = requests.get(url=self.url(
                "getCSRFToken"), headers=self.headers_one(), verify=False)
            result = response.json()

            if result['status'] == 1:
                msg(f"{name}: 成功!")
                token = result['data']['CSRF-TOKEN']
                # print(token)
                return token
            else:
                msg(f"{name}: 失败, 请稍后再试!")
                print(result)
        except Exception as err:
            print(err)

    def do_sign(self, name):  # 执行签到奖励
        try:
            payload = {}
            response = requests.post(url=self.url("user/login/reward/claim"), headers=self.headers(), data=payload,
                                     verify=False)
            result = response.json()
            # print(result)
            if result['status'] == 1:
                msg(f"{name}: 成功, 获得100礼金!")
                time.sleep(3)
                self.do_prophecy()
            elif result['status'] == 0:
                msg(f"{name}: {result['error']}, 已申请过奖励!")
            else:
                msg(f"{name}: 失败, 请稍后再试!")
                print(result)
        except Exception as err:
            print(err)

    def user_info(self, name="用户信息"):  # 用户信息
        try:
            response = requests.get(url=self.url(
                "user/appuser/info"), headers=self.headers())
            result = response.json()
            # print(result)
            if result['status'] == 1:
                phone = result['data']['data']['contactNo']
                msg(f"{name}: 成功!\n欢迎:{phone[:3]}****{phone[-4:]}, 余额: {float(result['data']['data']['wallet']['balance'])} USDT, 邀请码: {result['data']['data']['referralCode']}")
                time.sleep(3)
            elif result['status'] == 0:
                msg(f"{name}: 失败, 请检查变量&脚本更新到最新再试试")
            else:
                msg(f"{name}: 失败, 请稍后再试!")
                print(result)
        except Exception as err:
            print(err)

    def max_bet(self, name="最大投入"):  # 最大投入
        try:
            response = requests.get(url=self.url(
                "betting/max/bet/256/N"), headers=self.headers())
            result = response.json()
            # print(result)
            if result['status'] == 1:
                msg(f"{name}: 成功!")
                # print(result['data'])
                return result['data']
            elif result['status'] == 0:
                msg(f"{name}: 失败, 请检查变量&脚本更新到最新再试试")
            else:
                msg(f"{name}: 失败, 请稍后再试!")
                print(result)
        except Exception as err:
            print(err)

    def prophecy_list(self, name="预言列表获取id"):  # 预言列表-返回id
        try:
            response = requests.get(url=self.url(
                "betting/items?filter=%7B%22language%22%3A%22zh-hans%22%2C%22isActiveRound%22%3A%7B%22in%22%3A%5B%22Y%22%5D%7D%7D"),
                headers=self.headers())
            result = response.json()
            # print(result)
            if result['status'] == 1:
                num = result['data']['itemsCount']
                msg(f"共找到{num}个活动预言, 随机选择一个进行预言")
                random_num = random.randint(0, num - 1)
                items = result['data']['items']
                # print(items[random_num]['roundId'])
                round_id = items[random_num]['roundId']
                time.sleep(2)
                # print(round_id)
                return round_id
            elif result['status'] == 0:
                msg(f"{name}: 失败, 请检查变量&脚本更新到最新再试试")
            else:
                msg(f"{name}: 失败, 请稍后再试!")
                print(result)
        except Exception as err:
            print(err)

    def do_prophecy(self, name="执行预言"):  # 执行预言
        try:
            bet_num = self.max_bet()
            round_id = self.prophecy_list()
            # print(round_id)
            # print(bet_num)
            payload = f'amountNoWar={bet_num}&roundId={round_id}'
            print(payload)
            response = requests.post(url=self.url("betting/create"), headers=self.headers2(), data=payload,
                                     verify=False)
            result = response.json()
            # print(result)

            if result['status'] == 1:
                msg(f"预言无战争,成功!")
            elif result['status'] == 0:
                msg(f"{name}: 失败, 请检查变量&脚本更新到最新再试试")
            else:
                msg(f"{name}: 失败, 请稍后再试!")
                print(result)
        except Exception as err:
            print(err)


# ====================================================================
def last_version(name, mold):
    url = ''
    if mold == 1:
        url = f"https://raw.gh.fakev.cn/yml2213/Python/master/{name}/{name}.py"

    elif mold == 2:
        url = f"http://yml-gitea.ml:2233/yml/Python/raw/branch/master/{name}.py"
    try:
        _url = url
        _headers = {}
        response = requests.get(url=_url, headers=_headers, verify=False)
        result = response.text
        r = re.compile(r'Script_Version = "(.*?)"')
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
            r = re.compile(r'prophecy_data="(.*?)"', re.M | re.S | re.I)
            result = r.findall(env)
            # print(data[0])
            if "@" in result[0]:
                _ck = result[0].split("@")
                ckArr = _ck
            elif "\n" in result[0]:
                _ck = result[0].splitlines()
                ckArr = _ck
            else:
                ckArr = result
        else:
            print(f"检查变量 {name} 是否已填写")


def ql_env(name):
    global ckArr
    if name in os.environ:
        ckArr = []
        _data = os.environ[name]
        if "@" in _data:
            _ck = _data.split("@")
            ckArr = _ck
        elif "\n" in _data:
            _ck = _data.splitlines()
            ckArr = _ck
        else:
            ckArr = _data.split("@")


# 通知服务
class Msg(object):
    def __init__(self, m=''):
        self.str_msg = m
        self.message()

    # noinspection PyMethodMayBeStatic
    def get_sendnotify(self):
        if not os.path.exists("sendNotify.py"):
            cur_path = os.getcwd()
            print(f"未找到通知依赖文件,将于脚本执行目录({cur_path})新建:sendNotify.py ")
            try:
                url = 'https://raw.gh.fakev.cn/yml2213/Python/master/sendNotify.py'
                response = requests.get(url)
                with open('sendNotify.py', "w+", encoding="utf-8") as f:
                    f.write(response.text)
            except Exception as err:
                print(err)
        else:
            print("文件已存在,跳过")

    def message(self):
        global msg_info
        print(self.str_msg)
        try:
            msg_info = f"{msg_info}\n{self.str_msg}"
        except Exception as err:
            # print(err)
            msg_info = "{}".format(self.str_msg)
        sys.stdout.flush()

    def main(self):
        global send
        cur_path = os.getcwd()
        if os.path.exists(cur_path + "/sendNotify.py"):
            try:
                from sendNotify import send
            except Exception as err:
                self.get_sendnotify()
                print(err)
                try:
                    from sendNotify import send
                except Exception as err:
                    print(err)
                    print("加载通知服务失败~")
        else:
            self.get_sendnotify()
            try:
                from sendNotify import send
            except Exception as err:
                print(err)
                print("加载通知服务失败~")


Msg().main()


def msg(data):
    Msg(data)


def tip():
    print("================ 脚本只支持青龙面板 =================")
    print("============ 具体教程以请自行查看顶部教程 =============\n")
    msg(f"🔔 {Script_Name} ,开始! ")
    origin_version = last_version(Name_Pinyin, 1)
    msg(f"📌 本地脚本: {Script_Version}      远程仓库版本: V {origin_version}")
    msg(f"📌 🆙 更新内容: {Script_Change}")
    msg(f"共发现 {str(len(ckArr))} 个账号")


if __name__ == "__main__":
    global ckArr, msg_info, cookie_y, token_y
    _env()
    tip()
    start()
    send(f"{Script_Name}", msg_info)