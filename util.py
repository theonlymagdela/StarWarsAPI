from functools import wraps
from flask import jsonify
import sql


def json_response(func):
    """
    Converts the returned dictionary into a JSON response
    :param func:
    :return:
    """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        return jsonify(func(*args, **kwargs))

    return decorated_function


def generate_id(table_name):
    """ Generates a new ID for question or answer. """
    if table_name == 'user':
        last_id = sql.user_get_last_id()
        last_id = int(last_id['max'])

        return last_id + 1
