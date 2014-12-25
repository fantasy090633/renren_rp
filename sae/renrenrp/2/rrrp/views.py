# coding=utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from models import User, Log
import action


def index(request):
    """
        首页
    """
    return render_to_response('index.html', {}, context_instance=RequestContext(request))


def user(request, user_id):
    """
        用户信息页面
    """
    user_info = User.objects.get(id=user_id)
    username = user_info.username
    password = user_info.password
    if request.session.get('username', default=None) == username:
        is_login_flag = user_info.flag
        return render_to_response('user.html',
                                  {'username': username, 'password': password, 'is_login_flag': is_login_flag},
                                  context_instance=RequestContext(request))
    else:
        raise Http404()


def login(request):
    """
        登陆请求
    """
    username = request.POST.get('username').strip()
    password = request.POST.get('password').strip()
    result = action.login_renren(username, password)
    if 'Success' == result:
        request.session['username'] = username
        request.session['password'] = password
        try:
            user_info = User.objects.get(username=username)
        except User.DoesNotExist:
            password = request.session['password']
            user_info = User()
            user_info.username = username
            user_info.password = password
            user_info.flag = True
            user_info.save()
        return HttpResponseRedirect(reverse('user', args=(user_info.id,)))
    else:
        return HttpResponse(result)
        # return render_to_response('index.html', {'error_info': '登陆失败'}, context_instance=RequestContext(request))


def addUser(request, username):
    """
        开始/取消刷新人品请求
    """
    if request.session.get('username', default=None) == username:
        user_info = User.objects.get(username=username)
        if user_info:
            user_info.flag = not user_info.flag
            user_info.save()
        return HttpResponseRedirect(reverse('user', args=(user_info.id,)))
    else:
        raise Http404()


def fresh(request):
    """
        定时刷新人品请求
    """
    users = User.objects.all()
    for userObj in users:
        username = userObj.username
        password = userObj.password
        result = action.login_renren(username, password)
        logObj = Log()
        logObj.user = userObj
        logObj.log_info = result
        logObj.save()
    return HttpResponse('Fresh rp success!')


def clearLog(request):
    """
        定时清理成功日志请求
    """
    Log.objects.filter(log_info='Success').delete()
    return HttpResponse('Clear log success!')