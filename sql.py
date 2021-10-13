from psycopg2.extras import RealDictCursor
import database_common


@database_common.connection_handler
def user_get_last_id(cursor: RealDictCursor):
    """ Return last question ID from database. """
    query = """
            SELECT MAX(id)
            FROM "user"
        """
    cursor.execute(query)
    return cursor.fetchall()[0]


@database_common.connection_handler
def user_get_by_id(cursor: RealDictCursor, user_id):
    """ Return last question ID from database. """
    query = """
            SELECT * FROM "user" WHERE id = %(id)s
        """
    arguments = {"id": user_id}
    cursor.execute(query, arguments)
    return cursor.fetchall()[0]


@database_common.connection_handler
def user_add(cursor: RealDictCursor, user_id, new_user):
    """ Add a question to the database. """
    query = """
            INSERT INTO "user" (id, name, surname, mail, password)
            VALUES (%(id)s, %(nm)s, %(sn)s, %(un)s, %(ps)s)
        """
    arguments = {
        "id": user_id,
        "nm": new_user[2],
        "sn": new_user[3],
        "un": new_user[0],
        "ps": new_user[1]
    }
    cursor.execute(query, arguments)


@database_common.connection_handler
def users_get_mail(cursor: RealDictCursor):
    query = """
            SELECT mail
            FROM "user"
            """
    cursor.execute(query)
    return [row["mail"] for row in cursor.fetchall()]


@database_common.connection_handler
def user_get_password(cursor: RealDictCursor, username):
    query = """
            SELECT password
            FROM "user"
            WHERE mail = %(un)s
        """
    arguments = {"un": username}
    cursor.execute(query, arguments)
    return cursor.fetchall()[0]["password"]


@database_common.connection_handler
def user_id_get_by_mail(cursor: RealDictCursor, username):
    query = """
            SELECT id
            FROM "user"
            WHERE mail = %(ml)s
            """
    arguments = {"ml": username}
    cursor.execute(query, arguments)
    return cursor.fetchall()[0]["id"]
