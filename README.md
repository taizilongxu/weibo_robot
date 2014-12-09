---
layout: post
title:  "Python实现微博终端机器人"
category: python
tags: python
---

为了满足需要,做了这个程序~~没事玩玩的(最主要的是可以远程关机),手机或其他终端发送一个微博,主机就可以接受到命令,运行命令.项目地址https://github.com/taizilongxu/weibo_robot

利用这个代码,可以实现自动化发送,评论,还可以收集微博的各种信息,也可以无限扩展啊

![](https://github.com/taizilongxu/weibo_robot/raw/master/pic/1.png)

!w[](https://github.com/taizilongxu/weibo_robot/raw/master/pic/2.png)

##需要写入的参数

```python
APP_KEY = '' # app key
APP_SECRET = '' # app secret
CALLBACK_URL = '' # callback url
AUTH_URL = 'https://api.weibo.com/oauth2/authorize'
USERID = '' # userid
PASSWD = '' #password
```

其中前3项需要自己注册新浪的API然后填入进程序,注意要和USERID是一个账号,否则后面的认证就会失败.

后两项就是账号和密码了.

##运行

在开机启动时自动启动脚本,然后~~~就可以了

##过程难点

新浪的API需要返回一个code,网上大多数程序都是手动打开网页再获取code填入程序(这样一点也不科学!!)

参考了[Python：模拟登录以获取新浪微博OAuth的code参数值](http://blog.segmentfault.com/hongfei/1190000000343851)这篇文章,可以自动输入code了(哦也)

##运行依赖

Python 2.7
weibo
urllib2
urllib
time
subprocess
