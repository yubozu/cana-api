from utils.dbhelper import DBHelper


class User:

    def __init__(self, form):
        self.name = form.get("name")
        self.age = form.get("age")
        self.gender = form.get("gender") == "Female"
        self.uuid = form.get("uuid")
        self.clinical_id = form.get("clinical_id")
        self.study_id = form.get('study_id')
        self.identification_number = form.get('identification_number')
        self.db = DBHelper()

    def insert(self):
        scripts = """
            INSERT INTO user (`name`, `uuid`, `gender`, `age`, `clinical_id`, `study_id`, `identification_number`)
            SELECT * FROM ( SELECT %s, %s, %s, %s, %s, %s, %s) AS tmp WHERE
            NOT EXISTS ( SELECT `uuid` FROM user WHERE uuid = %s) LIMIT 1;
        """

        connect = self.db.get_connection()
        cursor = connect.cursor()
        cursor.execute(scripts, (self.name, self.uuid, self.gender, self.age, self.clinical_id, self.study_id,
                                 self.identification_number, self.uuid))

        connect.commit()
        cursor.close()
        connect.close()


