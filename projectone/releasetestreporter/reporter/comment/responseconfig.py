# -*- coding: utf-8 -*-
import json


def response_api( code=200,  msg=None, data=None):
    result = {
        'data': data if data is not None else {},
    }
    if code == 200:
        result['msg'] = msg if msg is not None else 'success!'
        result['code'] = code if code is not None else '200'
    else:
        result['msg'] = msg if msg is not None else 'fail'
        result['code'] = code if code is not None else '10000'
    return result
