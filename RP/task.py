import time
import getpass
import http.cookiejar
import urllib.request
import urllib.parse
import sys


def run():
    username = input('请输入人人网登陆账号：')
    password = getpass.getpass('请输入人人网登陆密码：')
    while True:
        login(username, password)
        print('登陆时间：%s' % time.strftime('%Y-%m-%d %X', time.localtime()))
        print('30分钟后刷新登陆，请勿关闭此窗口！')
        time.sleep(60 * 30)


def login(username, password):
    try:
        cookie = http.cookiejar.CookieJar()
        cookie_processor = urllib.request.HTTPCookieProcessor(cookie)
    except:
        raise
    else:
        opener = urllib.request.build_opener(cookie_processor)
        urllib.request.install_opener(opener)
    url = 'http://www.renren.com/PLogin.do'
    post_data = {
        'email': username,
        'password': password,
        'domain': 'renren.com'
    }
    req = urllib.request.Request(
        url,
        urllib.parse.urlencode(post_data).encode(encoding='UTF8')
    )
    if '新鲜事读取中...' in urllib.request.urlopen(req).read().decode('UTF8'):
        print('登陆成功')
    else:
        print('登陆失败，程序自动关闭')
        input('按回车退出程序！')
        sys.exit()

if __name__ == '__main__':
    run()