# _*_ coding:utf-8 _*_

from flask import Flask, request
from flask_cors import CORS

import json
from threading import Timer

import op_mysql

app = Flask(__name__, static_url_path='', static_folder='')
# 因为vue和render_template的模板都是用{{  }}，所以会冲突，将 jinja修改为[[  ]]
app.jinja_env.variable_start_string = '[['
app.jinja_env.variable_end_string = ']]'
CORS(app, supports_credentials=True)


@app.route("/inserttask", methods=['GET', 'POST'])
def insert_task():
    mysqlObj = op_mysql.OPMYSQL()
    data_dict = request.json.get("formdata")
    status = mysqlObj.insertTask(data_dict)
    if status == "sucess":
        return "sucess"
    else:
        return "failed"


@app.route("/selecttask", methods=['GET'])
def select_task():
    mysqlObj = op_mysql.OPMYSQL()
    data_dict = request.args.to_dict()
    data = mysqlObj.selectTask(status=data_dict['status'])
    res_dict = {"results": data}

    print(res_dict)
    return res_dict


@app.route("/finshtask", methods=['GET', 'POST'])
def finsh_task():
    mysqlObj = op_mysql.OPMYSQL()
    data_dict = request.json.get("formdata")
    print(data_dict)
    mysqlObj.doing2Done(data_dict)
    return "OK"


# 定时将mysql中到时间的预定计划改为进行中
def pre2doing():
    mysqlObj = op_mysql.OPMYSQL()
    mysqlObj.pre2Doing()
    t = Timer(5, pre2doing)
    t.start()


if __name__ == "__main__":
    pre2doing()
    app.run(host='192.168.0.29', port=5350, debug=True)
