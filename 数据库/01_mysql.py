from pymysql import *


def main():

    # 创建连接
    conn = connect(host='localhost', port=3306,user='root', password='ly199051', database='01python',charset='utf8')
    # 创建游标
    cursors1 = conn.cursor()

    # 对数据库的操作---start
    count = cursors1.execute("select * from heros")
    print(count)
    # print(cursors1.fetchone())
    # print(cursors1.fetchone())
    # print(cursors1.fetchone())
    print(cursors1.fetchmany(1))
    print(cursors1.fetchall())
    # 对数据库的操作---end

    # 关闭游标
    cursors1.close()
    # 关闭连接
    conn.close()


if __name__ == '__main__':
    main()