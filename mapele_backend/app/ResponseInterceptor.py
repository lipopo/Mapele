# -*- coding: utf8 -*-

# 内容拦截

# 本地访问 拦截器 
def is_local(host=None):
    def main(func):
        if host == "127.0.0.1":
            return func
        else:
            def response():
                res = "you are not request in inner network"
                return res
            return response
    return main

# 非GET请求 拦截器
def get_only(method=None):
    def main(func):
        if method == "GET":
            return func
        else:
            def response():
                res = "You can only use GET request"
                return res
            return response
    return main


# Response 拦截

# OPTIONS请求 拦截器
def option_request(method=None, method_accept = None, request = None):
    def main(func):
        if method == "OPTIONS":
            def response():
                res = Response()
                res.headers["Access-Control-Allow-Origin"] = request.headers["Origin"]
                res.headers["Access-Control-Allow-Method"] = request.headers["Access-Control-Request-Method"]
                res.headers["Access-Control-Allow-Headers"] = request.headers["Access-Control-Request-Headers"] 
                return res
            return response
        else:
            return func
    return main
