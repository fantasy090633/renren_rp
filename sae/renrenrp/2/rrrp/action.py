# coding=utf-8
import cookielib
import urllib2
import urllib


def login_renren(username, password):
    """
        根据用户名和密码登陆
        Args:
            username:用户名
            password:密码
        Return:
            登陆信息
    """
    try:
        cookie = cookielib.CookieJar()
        cookie_processor = urllib2.HTTPCookieProcessor(cookie)
    except:
        raise
    else:
        opener = urllib2.build_opener(cookie_processor)
        urllib2.install_opener(opener)
    url = 'http://www.renren.com/PLogin.do'
    post_data = {
        'email': username,
        'password': password,
        'domain': 'renren.com',
    }
    # Request (url [data,headers [,origin_req_host ,[unverifiable]]]]), 传入data参数, 请求自动变POST
    # 因为用户名密码为英文, 所以不需要.encode(encoding='UTF8')
    req = urllib2.Request(url, urllib.urlencode(post_data))
    # urlopen (url [,data ,[timeout]]), url可以为url地址，也可以是Request对象
    try:
        html = urllib2.urlopen(req).read()
        if '新鲜事读取中...' in html:
            return 'Success'
        else:
            return html
    except Exception as e:
        return e