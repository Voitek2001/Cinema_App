from common_utils import write_to_json, Category, read_json, get_datetime_from_string, get_timedelta_from_string
from datetime import datetime, timedelta
from ID_generator import get_and_inc_film_id
import os
import sys
import string
sys.path.append('/db/')


ALL_FILMS = os.path.abspath('db/films_data.json')
sys.path.append(ALL_FILMS)
ALL_ORDERS = os.path.abspath('db/orders.json')
sys.path.append(ALL_ORDERS)


def create_new_film(category, title, film_datetime, duration, room_id, price):
    return {
        'category': category.value, # to avoid problems with writing
        'title': title,
        'film_datetime': str(film_datetime), # to avoid problems with writing
        'duration': str(duration), # to avoid problems with writing
        'room_id': room_id,
        'film_id': get_and_inc_film_id(),
        "price": {"normal": price, "discounted": str(int(int(price)*0.8))}
    }


def check_for_collision(data, room_id, date, duration):

    # room_id = new_film['room_id']
    # date = get_datetime_from_string(new_film['film_datetime'])
    # duration = get_timedelta_from_string(new_film['duration'])
    for film in data:
        if room_id != film['room_id']:
            continue
        start_film = get_datetime_from_string(film['film_datetime'])
        duration_film = get_timedelta_from_string(film['duration'])

        if not (date + duration < start_film or date > start_film + duration_film):
            raise ValueError(f"Podany film nie może zostać dodany ponieważ koliduje z innymi.\nPrzejrzyj dokładnie "
                             f"terminarz innych filmów!\n")

##[KOLIZJA Z FILMEM {film['title']} O GODZINIE "
#                             f"{film['film_datetime']}, TRWAJACYM {film['duration']} W SALI {film['room_id']}]
#
def add_new_film(film_datetime, duration, category, title, room_id, ticket_price):

    data = read_json(ALL_FILMS)

    check_for_collision(data, room_id, film_datetime, duration)

    new_film = create_new_film(category, title, film_datetime, duration, room_id, ticket_price)

    data.append(new_film)
    write_to_json(ALL_FILMS, data)


def get_list_of_films():

    data = read_json(ALL_FILMS)
    all_films = {}

    for film in data:

        all_films[film['title']] = all_films.get(film['title'], []) + [{"date": get_datetime_from_string(film['film_datetime']), "room": film['room_id'], "price": film['price'], "film_id": film['film_id']}]

    print(all_films)
    return all_films


def get_list_of_orders():

    data = read_json(ALL_ORDERS)
    all_orders = {}

    for order in data:
        order['seats'] = seats_list_from_string(order['seats'])
        all_orders[order['order_id']] = order

    print(all_orders)
    return all_orders


def seats_list_from_string(str):
    numbers = str.translate(str.maketrans('', '', string.punctuation)).split()
    list = []
    for i in range(0, len(numbers), 2):
        list.append((int(numbers[i]), int(numbers[i+1])))
    return list


if __name__ == '__main__':
    #try:
    #    add_new_film(2010, 4, 10, 13, 20, 120, Category.ACTION, "Dark Knight", 1)
    #except ValueError as err_msg:
    #    print(err_msg)

    print(datetime.now() + timedelta(seconds=120))

    #get_list_of_films()
    print({"date": 2, "room": 3})