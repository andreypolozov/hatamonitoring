import typing as tp

import datetime

class DataBaseDao:
    def __init__():
        # self.client = Postgres какой нибудь
        pass

    def get_duty_kitchen_future() -> tp.List:
        # return селект на табличку duty_kitchen_future
        pass

    def change_able(
            date_from: datetime.datetime,
            date_to: datetime.datetime
    ) -> None:
        # тут править таблицу user_statuses и duty_kitchen_future под одной транзакцией
        pass
