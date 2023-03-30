from common_utils import write_to_json, Category, read_json, get_datetime_from_string, get_timedelta_from_string
from datetime import datetime, timedelta
import os
import sys
sys.path.append('/db/')


ALL_FILMS = os.path.abspath('db/films_data.json')
sys.path.append(ALL_FILMS)


def create_new_film(category, title, film_datetime, duration, room_id):
    return {
        'category': category.value, # to avoid problems with writing
        'title': title,
        'film_datetime': str(film_datetime), # to avoid problems with writing
        'duration': str(duration), # to avoid problems with writing
        'room_id': room_id
    }


def check_for_collision(data, new_film):

    room_id = new_film['room_id']
    date = get_datetime_from_string(new_film['film_datetime'])
    duration = get_timedelta_from_string(new_film['duration'])
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
def add_new_film(film_datetime, duration, category, title, room_id):

    data = read_json(ALL_FILMS)

    new_film = create_new_film(category, title, film_datetime, duration, room_id)

    check_for_collision(data, new_film)

    data.append(new_film)
    write_to_json(ALL_FILMS, data)


def get_list_of_films():

    data = read_json(ALL_FILMS)
    all_films = {}

    for film in data:

        all_films[film['title']] = all_films.get(film['title'], []) + [{"date": get_datetime_from_string(film['film_datetime']), "room": film['room_id']}]

    print(all_films)
    return all_films



if __name__ == '__main__':
    #try:
    #    add_new_film(2010, 4, 10, 13, 20, 120, Category.ACTION, "Dark Knight", 1)
    #except ValueError as err_msg:
    #    print(err_msg)

    print(datetime.now() + timedelta(seconds=120))

    #get_list_of_films()
    print({"date": 2, "room": 3})