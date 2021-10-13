import sql
import util
import user


def user_add(new_user):
    user_id = util.generate_id('user')
    return sql.user_add(user_id, new_user)
