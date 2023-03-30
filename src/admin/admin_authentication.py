import bcrypt
import sys


def create_hash_from_password(input_password):
    password = bytes(input_password, encoding="ascii")

    with open("admin/admin_password", 'rb') as f:
        hash = f.readline().strip()
        salt = f.readline().strip()

    hashed = bcrypt.hashpw(password, salt)
    return hashed, hash


def authenticate_password(input_password):

    input_hash, curr_pass_hash = create_hash_from_password(input_password)
    if input_hash == curr_pass_hash:
        return True
    return False



def set_new_password(new_password):
    password = bytes(new_password, encoding="ascii")
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password, salt)

    with open("admin_password", 'wb') as f:
        f.write(hash)
        f.write(b"\n")
        f.write(salt)


if __name__ == '__main__':
    set_new_password(str(sys.argv[1]))
