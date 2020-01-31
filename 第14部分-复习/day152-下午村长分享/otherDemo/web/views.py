#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2019/2/27

import json

from django.shortcuts import render
from django.http import HttpResponse

from utils.polyv import polyv_video


def _get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    # logger.debug("get ip:{} from request.".format(ip))
    return ip


def sentry_demo(request):
    """
    关于 `sentry` 的具体使用, 主要用作于日志收集的管理工具

    访问 `sentry.io` 注册，并创建项目, 在settings添加DSN
    """
    raise ValueError("我错了....")
    return HttpResponse("ok")


def log(request):
    """
    `django` 日志系统

    文档参见: https://docs.djangoproject.com/en/1.11/topics/logging/
    """
    import logging
    logger = logging.getLogger(__name__)
    logger.info("你好")
    logger.info("你好")
    logger.info("你好")
    logger.info("你好")
    logger.info("你好")
    logger.info("你好")
    logger.info("你好")
    logger.info("你好")
    logger.info("你好")
    return HttpResponse("OK")


def send_mail(request):
    """
    发送邮件

    前提：请在配置文件中配置邮箱属性
    """
    import threading
    from django.core.mail import send_mail
    # 关于更多邮件客户端可使用
    # from django.core.mail import EmailMultiAlternatives
    # msg = EmailMultiAlternatives(
    #     "邮件标题", "邮件内容", from_email=settings.DEFAULT_FROM_EMAIL, to=settings.SEND_EMAIL_NOTICE
    # )
    # 如果发送内容为`html`格式的话, 设置这个属性即可
    # msg.content_subtype = "html"
    # msg.send()

    # 如果发送内容为`html`格式的话, 多传 `html_message`

    task = threading.Thread(target=send_mail, args=("你好", "世界", "18803561683@163.com", [
            "404042726@qq.com", "17611061199@163.com", "kangchen112358@aliyun.com"
    ],))
    task.start()
    # result = send_mail(
    #     "你好", "世界", "18803561683@163.com", [
    #         "404042726@qq.com", "17611061199@163.com", "kangchen112358@aliyun.com"
    #     ],
    # )
    # print(result)

    return HttpResponse("Ok")


def play(request):

    vid = "03b56854c0970bde8598a0659e8cafa6_0"

    extra_params = polyv_video.get_verify_data(
        vid, _get_client_ip(request), 'customuserid', 'customid',
    )
    # print(extra_params)

    return render(request, "play.html", context={"vid": vid, "extra_params": extra_params})


def verify(request):
    vid = request.GET.get("vid")
    # 自定义
    code = request.GET.get("code", "")

    # 获取签名使用
    t = request.GET.get("t")
    callback = request.GET.get("callback")

    # 逻辑校验是否可进行观看视频
    # auth_video_play = AuthVideoPlay(request, vid)
    # if auth_video_play.is_valid():
    #     status = 1
    # else:
    #     status = 2

    username = request.user.username or "xxx"

    # 计算可播放的签名
    play_sign = polyv_video.get_play_key(vid, username, code, 1, t)

    resp = polyv_video.get_resp(1, username, play_sign, '放置具体的异常信息')

    if callback:
        resp = "{}({})".format(callback, resp)
    else:
        resp = json.dumps(resp)

    from django.shortcuts import HttpResponse

    return HttpResponse(resp)


def write(request):
    from utils.form import CommentForm

    form = CommentForm()

    return render(request, 'write.html', {"form": form})
