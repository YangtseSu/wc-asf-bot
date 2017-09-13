#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import itchat

#自己到http://www.tuling123.com申请一个免费api，输入key和userid
TL_KEY = '在这里输入id'

def get_tl_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : TL_KEY,
        'info'   : msg,
        'userid' : 'ASF',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

def get_asf_response(msg):
    ipcUrl = 'http://127.0.0.1:1242/IPC'
    try:
        r = requests.get(ipcUrl, params={'command':msg})
        return r.text
    except:
        return

#这里的username换成自己的名字，中英文随意
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    defaultReply = '<username> 感觉自己萌萌哒'
    if msg['ToUserName'] != 'filehelper': return
    if msg['Text'].startswith('!'):
        reply = get_asf_response(msg['Text'])
    else: 
        reply = '<username> ' + get_tl_response(msg['Text'])
    if reply:
        itchat.send(reply, 'filehelper')
    else:
        itchat.send(defaultReply, 'filehelper')

#如果在终端不能获取正常的二维码，将2改成1
itchat.auto_login(hotReload=True,enableCmdQR=2)
itchat.run()
