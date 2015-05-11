## 使用

需要weibo包依赖:

```
pip install weibo
```

## 截图

![](https://github.com/taizilongxu/weibo_robot/raw/master/pic/1.png)

![](https://github.com/taizilongxu/weibo_robot/raw/master/pic/2.png)

## 需要写入的参数

```python
APP_KEY = '' # app key
APP_SECRET = '' # app secret
CALLBACK_URL = '' # callback url
AUTH_URL = 'https://api.weibo.com/oauth2/authorize'
USERID = '' # userid
PASSWD = '' #password
```

其中前3项需要自己注册新浪的API然后填入进程序,注意要和USERID是一个账号,否则后面的认证就会失败.

后两项是账号和密码.

## 运行依赖

* Python 2.7
* weibo
