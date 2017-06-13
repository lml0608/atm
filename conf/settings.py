
import os
import sys
import logging


#D:\dev\atm\conf\settings.py
print(os.path.abspath(__file__))
#D:\dev\atm\conf
print(os.path.dirname(os.path.abspath(__file__)))
#D:\dev\atm
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE_DIR)

DATABASE = {
    'engine':'file_storage',
    'name':'accounts',
    'path':"%s\db" % BASE_DIR
}

LOG_LEVEL = logging.INFO

LOG_TYPES = {
    'transaction':'transactions.log',
    'access':'access.log',
}

TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},
}
