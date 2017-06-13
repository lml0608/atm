
import os
def file_db_handle(conn_params):

    print('file db:', conn_params)

    db_path = '%s\%s' % (conn_params['path'], conn_params['name'])


    return db_path

def mysql_db_handle(conn_parms):
    pass

def db_handler(conn_parms):

    if conn_parms['engine'] == 'file_storage':
        #从文件读取
        return file_db_handle(conn_parms)

    if conn_parms['engine'] == 'mysql':
        # 从数据库读取
        return mysql_db_handle(conn_parms)