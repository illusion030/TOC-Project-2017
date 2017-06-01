from transitions.extensions import GraphMachine
from html.parser import HTMLParser
from lxml import html
import requests

img = ""
name = ""

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def on_enter_user(self, update):
        global img
        global name
        print("state:user")
        update.message.reply_text(img+"\n歡迎來到"+name+"課程查詢系統\n輸入/change更換人物\n請輸入要查詢的系所號碼(e.g.A9, F7)：")

    def findid(self, update):
        courseid = ["a2", "a3", "a4", "a5", "a6", "aa", "ah", "an",
                    "c0", "a1", "a7", "a9", "ag", "b0", "b1", "k1",
                    "b2", "k2", "b3", "k3", "b5", "k5", "k4", "k7",
                    "k8", "c1", "l1", "c2", "l2", "c3", "l3", "c4",
                    "l4", "cz", "f8", "l7", "la", "vf", "e0", "e1",
                    "n1", "e3", "n3", "e4", "n4", "e5", "n5", "e6",
                    "n6", "e8", "n8", "nc", "e9", "n9", "f0", "p0",
                    "f1", "p1", "f4", "p4", "q4", "f5", "p5", "f6",
                    "p6", "f9", "p8", "n0", "na", "nb", "h1", "r1",
                    "h2", "r2", "h3", "r3", "r7", "h4", "r4", "h5",
                    "r5", "r9", "r0", "r6", "r8", "ra", "rb", "rd",
                    "rz", "i2", "t2", "i3", "t3", "i5", "i6", "t6",
                    "i7", "t7", "i8", "s0", "s1", "s2", "s3", "s4",
                    "s5", "s6", "s7", "s8", "s9", "sa", "sb", "sc",
                    "t1", "t4", "t8", "t9", "ta", "tc", "d2", "u2",
                    "d4", "d5", "u5", "d8", "u7", "u1", "u3", "e2",
                    "n2", "q1", "q3", "q6", "q7", "f7", "nd", "p7",
                    "q5", "p9", "v6", "v8", "v9", "va", "vb", "vc",
                    "vd", "ve", "vg", "vh", "vj", "vk", "vl", "vm",
                    "vn", "e7", "n7", "f2", "p2", "f3", "p3", "pa",
                    "pb", "c5", "l5", "c6", "l6", "z0", "z2", "z3",
                    "z5"]
        text = update.message.text
        global id
        id = text.upper()
        for c in courseid:
            if c == text.lower():
                return True
        return False

    def on_enter_findid(self, update):
        print("state:findid")
        global url 
        url = 'http://course-query.acad.ncku.edu.tw/qry/qry001.php?dept_no='
        url = url + id
        print(url)
        update.message.reply_text("找到系所號碼: "+id+"\n請輸入課程序號(e.g.010, 042)\n輸入/leave離開: ")

    def notfindid(self, update):
        update.message.reply_text("查無此系所號碼")
        return True

    def leave(self, update):
        text = update.message.text
        return text.lower() == "/leave"

    def start(self, update):
        text = update.message.text
        return text.lower() == "/start"

    def on_enter_start(self, update):
        print("state:start")
        global img 
        img = "░░░░░▄▄░░░░░░▄▄▄▄░░░░░ ░░░▐▀▀▄█▀▀▀▀▀▒▄▒▀▌░░░░ ░░░▐▒█▀▒▒▒▒▒▒▒▒▀█░░░░░ ░░░░█▒▒▒▒▒▒▒▒▒▒▒▀▌░░░░ ░░░░▌▒██▒▒▒▒██▒▒▒▐░░░░ ░░░░▌▒▒▄▒██▒▄▄▒▒▒▐░░░░ ░░░▐▒▒▒▀▄█▀█▄▀▒▒▒▒█▄░░ ░░░▀█▄▒▒▐▐▄▌▌▒▒▄▐▄▐░░░ ░░▄▀▒▒▄▒▒▀▀▀▒▒▒▒▀▒▀▄░░ ░░█▒▀█▀▌▒▒▒▒▒▄▄▄▐▒▒▐░░ ░░░▀▄▄▌▌▒▒▒▒▐▒▒▒▀▒▒▐░░ ░░░░░░░▐▌▒▒▒▒▀▄▄▄▄▄▀░░" 
        global name 
        name = "熊怪"
        self.go_back(update)
    
    def change(self, update):
        text = update.message.text
        return text.lower() == '/change'

    def on_enter_change(self, update):
        print("state:change")
        update.message.reply_text('請輸入數字選擇要更換的人物\n1. 熊怪\n2. 狗狗\n3. 貓貓')

    def bear(self, update):
        text = update.message.text
        if text.lower() == '1':
            global img
            img = '░░░░░▄▄░░░░░░▄▄▄▄░░░░░ ░░░▐▀▀▄█▀▀▀▀▀▒▄▒▀▌░░░░ ░░░▐▒█▀▒▒▒▒▒▒▒▒▀█░░░░░ ░░░░█▒▒▒▒▒▒▒▒▒▒▒▀▌░░░░ ░░░░▌▒██▒▒▒▒██▒▒▒▐░░░░ ░░░░▌▒▒▄▒██▒▄▄▒▒▒▐░░░░ ░░░▐▒▒▒▀▄█▀█▄▀▒▒▒▒█▄░░ ░░░▀█▄▒▒▐▐▄▌▌▒▒▄▐▄▐░░░ ░░▄▀▒▒▄▒▒▀▀▀▒▒▒▒▀▒▀▄░░ ░░█▒▀█▀▌▒▒▒▒▒▄▄▄▐▒▒▐░░ ░░░▀▄▄▌▌▒▒▒▒▐▒▒▒▀▒▒▐░░ ░░░░░░░▐▌▒▒▒▒▀▄▄▄▄▄▀░░'
            global name
            name = '熊怪'
            return True
        return False

    def doge(self, update):
        text = update.message.text
        if text.lower() == '2':
            global img
            img = "░░░░░░░░░▄░░░░░░░░░░░░░░▄░░░░\n░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌░░░\n░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐░░░\n░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐░░░\n░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐░░░\n░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌░░░\n░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌░░\n░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐░░\n░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌░\n░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌░\n▀▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐░\n▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌\n▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐░\n░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌░\n░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐░░\n░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌░░\n░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀░░░\n░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀░░░░░\n░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀░░░░░░░░"
            global name
            name = "狗狗"
            return True
        return False

    def cat(self, update):
        text = update.message.text
        if text.lower() == '3':
            global img
            img = '▒▒▒▒▒▒▒█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n▒▒▒▒▒▒▒█░▒▒▒▒▒▒▒▓▒▒▓▒▒▒▒▒▒▒░█\n▒▒▒▒▒▒▒█░▒▒▓▒▒▒▒▒▒▒▒▒▄▄▒▓▒▒░█░▄▄\n▒▒▄▀▀▄▄█░▒▒▒▒▒▒▓▒▒▒▒█░░▀▄▄▄▄▄▀░░█\n▒▒█░░░░█░▒▒▒▒▒▒▒▒▒▒▒█░░░░░░░░░░░█\n▒▒▒▀▀▄▄█░▒▒▒▒▓▒▒▒▓▒█░░░█▒░░░░█▒░░█\n▒▒▒▒▒▒▒█░▒▓▒▒▒▒▓▒▒▒█░░░░░░░▀░░░░░█\n▒▒▒▒▒▄▄█░▒▒▒▓▒▒▒▒▒▒▒█░░█▄▄█▄▄█░░█\n▒▒▒▒█░░░█▄▄▄▄▄▄▄▄▄▄█░█▄▄▄▄▄▄▄▄▄█\n▒▒▒▒█▄▄█░░█▄▄█░░░░░░█▄▄█░░█▄▄█'
            global name
            name = "貓貓"
            return True
        return False

    def findcourse(self, update):
        global count
        global info
        coursenum = update.message.text.lower()
        count = 0
        page = requests.get(url)
        page.encoding = 'utf-8'
        tree = html.fromstring(page.text)
        info = tree.xpath('//tr[@class]/td[3]/text() | //tr[@class]/td[16]/text() | //tr[@class]/td[11]/a/text()')
        for i in info:
            if i == coursenum:
                return True
            count = count + 1
        return False

    def on_enter_findcourse(self, update):
        print('state:findcourse')
        update.message.reply_text("找到課程: "+info[count+1]+"\n餘額為: "+info[count+2]+"\n輸入任意文字離開: ")

    def notfindcourse(self, update):
        update.message.reply_text('查無此課程序號')
        return True

    def alwaysleave(self, update):
        return True

    def on_enter_leave(self, update):
        update.message.reply_text("確認離開?\n輸入/yes離開\n輸入/no返回:\n")
    
    def yes(self, update):
        text = update.message.text
        return text.lower() == "/yes"
    
    def no(self, update):
        text = update.message.text
        return text.lower() == "/no"
