import datetime
from PyQt5 import QtCore

def filter_films_by_date(start, end, films):
    end += datetime.timedelta(days=1)
    for film in films:
        films[film] = [seans for seans in films[film] if start <= seans['date'] < end]


def create_relational_table_with_filters(films, orders, data_start, data_end, categories_filter=None,
                                         films_filter=None):
    films = [film for film in films if data_start <= film['date'].date() <= data_end]
    if films_filter is not None:
        films = [film for film in films if film['title'] in films_filter]
    if categories_filter is not None:
        films = [film for film in films if film['category'] in categories_filter]
    films = {film['film_id']: film for film in films}

    relational_table = []
    for order in orders:
        if order['film_id'] in films:
            film = films[order['film_id']]
            data = {'category': film['category'], 'title': film['title'], 'date': film['date'],
                    'room_id': film['room_id'], 'price': film['price'],
                    'n_normal_tickets': order['n_normal_tickets'], 'n_disc_tickets': order['n_disc_tickets'],
                    'total_cost': float(order['total_cost'])}
            relational_table.append(data)
    return relational_table


def group_by_film_and_date(relational_table, start_date, end_date):
    data = {}

    for elem in relational_table:
        if elem['title'] not in data:
            data[elem['title']] = {date: [] for date in [start_date + datetime.timedelta(days=n) for n in
                                                         range((end_date - start_date).days + 1)]}
        data[elem['title']][elem['date'].date()].append((elem['n_normal_tickets'], elem['n_disc_tickets']))
    return data


def group_by_category_and_date(relational_table, start_date, end_date):
    data = {}

    for elem in relational_table:
        if elem['category'] not in data:
            data[elem['category']] = {date: [] for date in [start_date + datetime.timedelta(days=n) for n in
                                                            range((end_date - start_date).days + 1)]}
        data[elem['category']][elem['date'].date()].append((elem['n_normal_tickets'], elem['n_disc_tickets']))
    return data


def count_tickets(data, normal=True, discounted=True):
    data2 = {}
    for title, dates in data.items():
        data2[title] = {}
        for date, tickets in dates.items():
            norm, disc = 0, 0
            for ticket in tickets:
                norm += ticket[0]
                disc += ticket[1]
            sum = 0
            if normal:
                sum += norm
            if discounted:
                sum += disc
            data2[title][date] = sum
    return data2


def pydate_to_qdate(date):
    return QtCore.QDateTime(QtCore.QDate(date.year, date.month, date.day))

