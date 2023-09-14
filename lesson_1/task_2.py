from datetime import datetime


def happy_ny():
    current_date = datetime.now()

    assert current_date >= datetime(year=2023, month=1, day=1, hour=0, minute=0, second=0), '2023 еще не наступил'


if __name__ == '__main__':
    happy_ny()