import json
import datetime
from enum import Enum
import os


class Category(Enum):
    ACTION = 1
    COMEDY = 2
    DRAMA = 3
    FANTASY = 4
    HORROR = 5
    MYSTERY = 6
    ROMANCE = 7
    THRILLER = 8
    WESTERN = 9



def write_to_json(filename: str, data):
    json_string = json.dumps(data)
    with open(filename, 'w') as outfile:
        json.dump(json_string, outfile)


def read_json(filename: str):

    if os.stat(filename).st_size == 0:
        print("pusty plik")
        return []
    with open(filename) as json_file:

        data = json.load(json_file)
    return json.loads(data)


def get_datetime_from_string(time_str):
    return datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")


def get_timedelta_from_string(time_str):
    dt = datetime.datetime.strptime(time_str, "%H:%M:%S")
    total_sec = dt.hour * 3600 + dt.minute * 60 + dt.second
    return datetime.timedelta(seconds=total_sec)


if __name__ == '__main__':


    films = [{
            'category': Category.ACTION.value,
            'title': 'SkyFall',
            'film_datetime': str(datetime.datetime(2010, 4, 10, 15, 50)),
            'duration': str(datetime.timedelta(minutes=135)),
            'room_id': 1,

    },
        {
        'category': Category.COMEDY.value,
        'title': 'Kac Vegas',
        'film_datetime': str(datetime.datetime(2010, 4, 10, 19, 50)),
        'duration': str(datetime.timedelta(minutes=135)),
        'room_id': 1
        }]

    print(Category(1))
    write_to_json('db/films_data.json', films)
    x = read_json('db/films_data.json')
    print(x[0]['film_datetime'])
    a = datetime.datetime.strptime(x[0]['film_datetime'], "%Y-%m-%d %H:%M:%S")
    print(a)

