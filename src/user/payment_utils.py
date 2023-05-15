import datetime
import re
from common_utils import write_to_json, read_json


ban_pattern = "[0-9]{16}"
person_pattern = "^[a-z,A-Z]+ [a-z,A-Z]+$"
c_date_pattern = "[0-9]{2}/[0-9]{4}"
cvc_pattern = "[0-9]{3}"
ALL_PAYMENTS = "db/payment_details.json"


def check_if_valid_arguments(ban, person, c_date, cvc):

    pattern = re.compile(ban_pattern)
    if not pattern.match(ban):
        raise Exception("Niewłaściwy numer konta\nFormat : [16-cyfr]")

    pattern = re.compile(person_pattern)
    if not pattern.match(person):
        raise Exception("Błąd w imieniu i nazwisku\nJedynie litery polskiego alfabetu\nFormat [%imie %nazwisko]")

    pattern = re.compile(c_date_pattern)
    if not pattern.match(c_date):
        raise Exception("Bład w ważności karty\nFormat: %miesiac/%rok")

    card_date = datetime.datetime.strptime(c_date, "%m/%Y")
    if card_date < datetime.datetime.now() < card_date:
        raise Exception("Ważność karty wygasła")

    pattern = re.compile(cvc_pattern)
    if not pattern.match(cvc):
        raise Exception("Blad w numerze CVC\nFormat: [3-cyfry]")



def add_payment_details(ban, person, date, cvc, order_id, payment_id):
    '''
    add to db payments details as bank account number, name and surname of card owner etc
    '''
    check_if_valid_arguments(ban, person, date, cvc)
    payments = read_json(ALL_PAYMENTS)
    print(payments)
    data = {
        "ban": ban,
        "person": person,
        "c_data": date,
        "cvc": cvc,
        "order_id": order_id,
        "payment_id": payment_id
    }
    payments.append(data)
    write_to_json(ALL_PAYMENTS, payments)

    return "Płatność zrealizowana poprawnie!"
