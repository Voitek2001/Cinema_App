from common_utils import read_json

curr_order_id = 0
curr_film_id = 0
curr_payment_id = 0
ALL_ORDERS = 'db/orders.json'
ALL_FILMS = 'db/films_data.json'
ALL_PAYMENTS = 'db/payment_details.json'


def init_order_id():
    global curr_order_id
    data = read_json(ALL_ORDERS)
    curr_order_id = len(data)


def get_and_inc_order():
    global curr_order_id
    curr_order_id += 1
    return curr_order_id - 1


def init_film_id():
    global curr_film_id
    data = read_json(ALL_FILMS)
    curr_film_id = len(data)


def get_and_inc_film_id():
    global curr_film_id
    curr_film_id += 1
    return curr_film_id - 1


def init_payment_id():
    global curr_payment_id
    data = read_json(ALL_PAYMENTS)
    curr_payment_id = len(data)


def get_and_inc_payment_id():
    global curr_payment_id
    curr_payment_id += 1
    return curr_payment_id - 1
