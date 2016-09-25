import pymysql
from utils.dbhelper import DBHelper

class History:

	def __init__(self, form, filename):
		self.history_type = form.get("type")
		self.filename = filename
		self.user_uuid = form.get("uuid")
		self.create_time = form.get("date")
		self.db = DBHelper()

	def insert(self):
		scripts = """
			INSERT INTO history (`type`, `filename`, `uuid`, `create_time`) VALUES (%s, %s, %s, %s)
		"""

		connect = self.db.get_connection()
		cursor = connect.cursor();
		cursor.execute(scripts, (self.history_type, self.filename, self.user_uuid, self.create_time))

		connect.commit()
		cursor.close()
		connect.close()


