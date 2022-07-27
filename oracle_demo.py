import cx_Oracle as cx      #导入模块
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8' # 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'

if __name__ == '__main__':
    con = cx.connect(user='rcq', password='123456', dsn='101.37.162.212:1521/ORCL2')  #创建连接
    cursor = con.cursor()       #创建游标
    # oracle是大小写敏感的
    # 如果定义表名称或列名称的时候没有用引号引起来
    # oracle会把他们全部转换为大写,这时就会出现错误了
    cursor.execute('select * from "test"')  #执行sql语句
    data = cursor.fetchone()        #获取一条数据
    print(data)     #打印数据
    # cursor.execute("SELECT * FROM all_tables WHERE table_name = 'test'")
    # print(cursor.fetchone())
    cursor.close()  #关闭游标
    con.close()     #关闭数据库连接