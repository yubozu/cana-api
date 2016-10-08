from utils.dbhelper import DBHelper


class User:

    def __init__(self, form):
        self.name = form.get("name")
        self.age = form.get("age")
        self.gender = form.get("gender") == "Female"
        self.uuid = form.get("uuid")
        self.db = DBHelper()

    def insert(self):
        scripts = """
            INSERT INTO user (`name`, `uuid`, `gender`, `age`) SELECT * FROM ( SELECT %s, %s, %s, %s) AS tmp WHERE
            NOT EXISTS ( SELECT `uuid` FROM user WHERE uuid = %s) LIMIT 1;
        """

        connect = self.db.get_connection()
        cursor = connect.cursor()
        cursor.execute(scripts, (self.name, self.uuid, self.gender, self.age, self.uuid))

        connect.commit()
        cursor.close()
        connect.close()


