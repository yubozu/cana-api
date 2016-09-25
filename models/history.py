import pymysql
from utils.dbhelper import DBHelper

class History:

	def __init__(self, form, filename):
		self.id = form["id"]
		self.history_type = form["type"]
		self.filename = filename
		self.user_uuid = form["uuid"]
		self.create_time = form["date"]
		self.db = DBHelper()

	def insert_history(history):
		scripts = """
			INSERT INTO history (`id`, `type`, `filename`, `uuid`, `create_time`) VALUES (%s, %s, %s, %s, %s)
		"""

		connect = self.db.get_connection()
		cursor = connect.cursor();
		cursor.execute(scripts, (self.id, self.history_type, self,filename, self.user_uuid, self.create_time))
		




