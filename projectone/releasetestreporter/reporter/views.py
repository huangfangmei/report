import json

from django.shortcuts import render
from django.http import JsonResponse
from reporter.comment.responseconfig import *
from reporter.datacenter import *
from json import *
# Create your views here.
def get(request):
    return JsonResponse({'name': 'python'})

def get_reporter_list(request):
    """查询某一测试报告全部信息"""
    report_id = request.GET.get('report_id')
    report_list = get_reporter_dic_from_data(report_id)
    data = response_api(data=report_list)
    return JsonResponse(data)

