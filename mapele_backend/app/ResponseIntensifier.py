# -*- coding: utf8 -*-

# plugin
from flask import Response
import json

# Content Intensifier

# JSON FORMAT增强器
def json_format(func):
    def response():
        content = func()
        res = {"data": content}
        res_str = json.dumps(res)
        return res_str
    return response
# Response Format 增强器
def response_format(func):
    def response():
        content = func()
        res = Response(content)
        return res
    return response

# Response Intensifier

# JSON Content-Type 增强器
def json_content_type(func):
    def response():
        res = func()
        res.headers["Content-Type"] = "application/json"
        return res
    return response
# 跨域访问增强器
def across(func):
    def response():
        res = func()
        res.headers["Access-Control-Allow-Origin"] = "*"
        return res
    return response