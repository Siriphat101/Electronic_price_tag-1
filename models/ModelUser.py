from .entities.User import User


class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password, fname, lname FROM user WHERE username = '{}'""".format(user.username)
            sql = """SELECT id, username, password, fname, lname FROM user WHERE username = %s"""
            cursor.execute(sql, (user.username,))
            row = cursor.fetchone()
            if row is not None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3], row[4])
                return user
            else:
                return None
        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password, fname, lname FROM user WHERE id = '{}'""".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is not None:
                # return User(row[0], row[1], None, row[3], row[4])
                return User(None, None, None, row[3], row[4])

            else:
                return None
        except Exception as e:
            raise Exception(e)
