from common_utils import write_to_json, read_json

ALL_ORDERS = 'db/orders.json'

def add_order_details(order_id, film_id, payment_id, n_normal_tickets, n_disc_tickets, total_cost, seats):

    data = {
        'order_id': order_id,
        "film_id": film_id,
        "payment_id": payment_id,
        "n_normal_tickets": n_normal_tickets,
        "n_disc_tickets": n_disc_tickets,
        "total_cost": total_cost,
        "seats": str(list(seats))
    }

    orders = read_json(ALL_ORDERS)
    print(orders)
    print(data)
    orders.append(data)
    write_to_json(ALL_ORDERS, orders)


