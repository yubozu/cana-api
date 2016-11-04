from utils.dbhelper import DBHelper


class Doctor:

    def __init__(self):
        pass

    @staticmethod
    def user(doctor_id):

        scripts = """
               SELECT * FROM history WHERE doctor IN (SELECT doctor FROM history WHERE id = %d)
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
        SELECT MIN(id), group_concat( DISTINCT doctor ) from history GROUP BY doctor  ;
        """

        db = DBHelper()
        connect = db.get_connection()
        cursor = connect.cursor()
        cursor.execute(scripts)

        result = cursor.fetchall()
        print(result)

        return result

