# -*- coding: utf8 -*-

# flask app
from flask import Flask, request, Response

# response intensifier
from ResponseIntensifier import *
# response interceptor
from ResponseInterceptor import *

# database
from database import mapele_db


app = Flask(__name__)

@app.route("/hello")
def hello():
    # response interceptor

    # response intensifier
    @json_content_type
    # content intensifier
    @response_format
    @json_format
    # content interceptor
    def main():
        return "Hello"
    return main()

application = app
if __name__ == "__main__":
    app.run("0.0.0.0", 10290, debug=True)
