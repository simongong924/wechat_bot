# -- coding: utf-8 --
import itchat, time, re, sys, urllib2, json
from urllib import quote,unquote,urlencode
from itchat.content import *


@itchat.msg_register([TEXT])


# def text_reply(msg):
#     if msg['FromUserName'] != u'@10e03e86c71920347e32b6f93f5180d8':
#         if index == 1:
#             m1 = unicode('秒回，是不是很厉害？','utf-8')
#             itchat.send((m1), msg['FromUserName'])
#             m2 = unicode('是不是', 'utf8')
#             itchat.send((m2), msg['FromUserName'])
#         else:
#             m = quote(msg['Text'].encode('utf-8'))
#             # http://api.qingyunke.com/api.php?key=free&appid=0&msg=
#             # url = 'http://sandbox.api.simsimi.com/request.p?key=9470057a-909b-4e6c-a25d-19e0834d6667&lc=zh&ft=1.0&text='+m
#             url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg=' + m
#             print url
#             raw = urllib2.urlopen(url)
#             try:
#                 data = json.loads(raw.read().decode('utf-8'))
#                 # print data['response']
#                 print data['content']
#                 itchat.send((data['content']), msg['FromUserName'])
#             except:
#                 pass
#
#
@itchat.msg_register([PICTURE, RECORDING, VIDEO, SHARING])


def pic_reply(msg):
    import pdb; pdb.set_trace()
    print 'here'
    # itchat.send((unicode('图片不错','utf-8')),msg['FromUserName'])
    #itchat.send('@img@1.jpg', msg['FromUserName'])

if __name__ == '__main__':
    default_encoding = 'utf-8'
    import pdb; pdb.set_trace()
    if sys.getdefaultencoding() != default_encoding:
        itchat.auto_login(enableCmdQR=False, hotReload=True)
        itchat.run()
