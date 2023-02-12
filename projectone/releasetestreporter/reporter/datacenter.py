# -*- coding: utf-8 -*-

from reporter.models import BugInfomation,Reportes

def get_reporter_dic_from_data(report_id):
    report_list = Reportes.objects.filter(id=report_id)
    list_report = change_object_to_dic(report_list)
    report_bug = BugInfomation.objects.filter(id=list_report['bug_id'])
    list_bug = change_object_to_dic(report_bug)
    list_report.update(list_bug)
    return list_report

def change_object_to_dic(filter_list):
    for i in filter_list:
        dict_list = vars(i)
    del dict_list['_state']
    return dict_list



