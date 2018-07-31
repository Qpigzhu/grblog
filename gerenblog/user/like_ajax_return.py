# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\7\29 0029 19:31$'

from  django.http import  JsonResponse

#返回错误信息
def ErrorResponse(code,massage):
    data = {}
    data['status'] = 'ERROR'
    data['code'] = code
    data['message'] = massage
    return JsonResponse(data)

#返回成功信息
def SuccessResponse(like_num):
    data = {}
    data['status'] = 'SUCCESS'
    data['like_num'] = like_num
    return JsonResponse(data)

#收藏错误信息
def HouseErrorResponse(code, massage):
        data = {}
        data['status'] = 'ERROR'
        data['code'] = code
        data['message'] = massage
        return JsonResponse(data)
#收藏成功信息
def HouseSuccessResponse(message):
        data = {}
        data['status'] = 'SUCCESS'
        data['message'] = message
        return JsonResponse(data)