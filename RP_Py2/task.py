# coding=utf-8
import cookielib
import urllib2
import urllib
import sys


def login():
    reload(sys)
    sys.setdefaultencoding('utf-8')
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
        'email': '***********',
        'password': '************',
        'domain': 'renren.com'
    }
    req = urllib2.Request(
        url,
        urllib.urlencode(post_data).encode(encoding='UTF8')
    )
    if '新鲜事读取中...' in urllib2.urlopen(req).read().decode('UTF8'):
        return '登陆成功'

    else:
        return '登陆失败，程序自动关闭'

if __name__ == '__main__':
    login()