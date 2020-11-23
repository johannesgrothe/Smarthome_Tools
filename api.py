from flask import Flask, redirect, url_for, request
from bridge import MainBridge
from typing import Optional

# https://pythonbasics.org/flask-http-methods/


def run_api(bridge: MainBridge, port: int):
    """Methods that launches the rest api to read, write and update gadgets via HTTP"""

    app = Flask(__name__)

    @app.route('/')
    def root():
        return "<html><body><center><h1>API</h1><h2>{}</h2></body></html>".format(bridge.get_bridge_name())

    @app.route('/gadgets/all', methods=['GET'])
    def get_all_gadgets():
        gadget_list = bridge.get_all_gadgets()

        out_gadget_list: [dict] = []
        for gadget in gadget_list:
            json_gadget = gadget.get_json_representation()
            out_gadget_list.append(json_gadget)

        buf_res = {"gadgets": out_gadget_list, "gadget_count": len(gadget_list)}
        return buf_res

    # @app.route('/gadgets/all', methods=['POST', 'GET'])
    # def login():
    #     if request.method == 'POST':
    #         user = request.form['nm']
    #         return redirect(url_for('success', name=user))
    #     else:
    #         user = request.args.get('nm')
    #         return redirect(url_for('success', name=user))

    app.run(host='localhost', port=port)
