import pymysql

class Database:

	def __init__(self, connect_string):
		self.connect_string = connect_string

	def get_connection(self):
		pass
