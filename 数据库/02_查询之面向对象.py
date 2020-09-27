from pymysql import connect


class Hero(object):

    def __init__(self):
        self.conn = connect(host='localhost', port=3306, user='root', password='ly199051', database='01python',
                       charset='utf8')
        self.curs = self.conn.cursor()

    def __del__(self):
        self.curs.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.curs.execute(sql)
        for temp in self.curs.fetchall():
            print(temp)

    def add_sql(self, sql):
        self.curs.execute(sql)
        self.conn.commit()
        print("------commit-----")

    def add_name(self):
        sql = """insert into heros(name) values ("ddd")"""
        self.add_sql(sql)

    def show_id(self):
        sql = "select id from heros"
        self.execute_sql(sql)

    def show_name(self):
        sql = "select name from heros"
        self.execute_sql(sql)

    @staticmethod
    def print_menu():
        print("查询名字--1")
        print("查询id--2")
        print("新增name--3")
        return input("输入编号")

    def run(self):
        while True:

            num = self.print_menu()
            if num == "1":
                print("=======1")
                self.show_name()
            elif num == "3":
                print("=======3")
                self.add_name()
            else:
                print("=======2")
                self.show_id()


def main():
    hero = Hero()

    hero.run()


if __name__ == '__main__':
    main()
