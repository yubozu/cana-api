from utils.dbhelper import DBHelper


class Doctor:

    def __init__(self):
        pass

    @staticmethod
    def user(doctor_id):

        scripts = """
               SELECT * FROM history WHERE doctor IN (SELECT name FROM doctor WHERE id = %d)
        """ % doctor_id
        db = DBHelper()
        connect = db.get_connection()
        cursor = connect.cursor()
        cursor.execute(scripts)

        result = cursor.fetchall()
        print(result)

        return result

    @staticmethod
    def get_all_doctor():

        scripts = """
        SELECT * FROM doctor WHERE name IN (SELECT DISTINCT name FROM doctor)    ;
        """

        db = DBHelper()
        connect = db.get_connection()
        cursor = connect.cursor()
        cursor.execute(scripts)

        result = cursor.fetchall()
        print(result)

        return result

