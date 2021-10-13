from flask import session
import bcrypt
import sql


def get_user_id():
    return session['id'] if 'id' in session else None


def is_logged() -> bool:
    """ Checks if user is logged. """
    return True if 'id' in session else False


def valid_login(username: str, password: str) -> bool:
    """ Validates user and password: whether they exist in the database. """
    all_users = sql.users_get_mail()
    user_password = sql.user_get_password(username)
    return True if (username in all_users) and (password_verify(password, user_password)) else False


# ------------------------------ encryption and decryption functions ------------------------------

def password_hash(plaintext_password) -> str:
    """ By using bcrypt, the salt is saved into the hash itself. """
    hashed_bytes = bcrypt.hashpw(plaintext_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def password_verify(plaintext_password, hashed_password) -> bool:
    """ Returns True if plaintext password match with hashed_password, else returns False. """
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plaintext_password.encode('utf-8'), hashed_bytes_password)