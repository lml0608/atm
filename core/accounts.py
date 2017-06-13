# -*- coding:utf-8 -*-
#__author__:"liubin"

import json
import time
from core import db_handler
from conf import settings
import os

print(1)


def load_current_balance(account_id):
    '''
    返回用户账目和其他信息
    :param account_id: 
    :return: 
    '''
    #找到DB路径
    db_path = db_handler.db_handler(settings.DATABASE)
    print("db_path = " + db_path)

    account_file = "%s\%s.json" % (db_path, account_id)

    print(account_file)

    with open(account_file) as f:

        acc_data = json.load(f)

        #返回json数据
        # {'status': 0, 'password': 'abc', 'pay_day': 22, 'balance': 15974.4, 'expire_date': '2021-01-01', 'credit': 15000, 'enroll_date': '2016-01-02', 'id': 1234}
        return acc_data

def dump_account(account_data):

    db_path = db_handler.db_handler(settings.DATABASE)

    account_file = "%s/%s.json" % (db_path, account_data['id'])


    with open(account_file, 'w') as f:

        acc_data = json.dump(account_data, f)

    return True


print(load_current_balance(1234))

