import typing as tp
import psycopg2 as psql
import datetime


class DataBaseDao:
    def __init__(self):

        conn = psql.connect(dbname='hata', user='a.polozovyablonskiy',
                            password='1234', host='localhost')
        self.cursor = conn.cursor()
        print(self.cursor)

    def execute_ql(self, str):
        self.cursor.execute(str)
        return self.cursor.fetchall()

    def get_users(self) -> tp.List[tp.Tuple]:
        return self.execute_ql('SELECT id, name FROM users')

    def get_duty_kitchen_future(self) -> tp.List[tp.Any]:
        return self.execute_ql("""SELECT day, t1.name
                                  FROM duty_kitchen_future as t0
                                  LEFT JOIN users as t1 on t0.id_user=t1.id
                                  WHERE  to_date(now()) < day <= to_date(now()) + integer '14%'""")

    def change_able(
            self,
            date_from: datetime.datetime,
            date_to: datetime.datetime
    ) -> None:
        # тут править таблицу user_statuses и duty_kitchen_future под одной транзакцией
        pass

    def curren_duty(
            self,
    ) -> str:
        return "Тебя ебёт?"
