import pymysql
import configparser

class DBHelper:

	def __init__(self):
		cf = configparser.ConfigParser()
		cf.read('configs/dev.ini')

		connect_string = {}
		for option in cf.options('mysqld'):
		    connect_string[option] = cf.get('mysqld', option)
		connect_string['port'] = int(connect_string['port'])
		self.connect_string = connect_string

	def get_connection(self):
		return pymysql.connect(**self.connect_string)

	def prepare_database(self):
	    script = """CREATE TABLE IF NOT EXISTS `history`
	    (
	        `id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	        `type` VARCHAR(20) NOT NULL,
	        `filename` VARCHAR(50) NOT NULL,
	        `uuid` VARCHAR(50) NOT NULL,
	        `create_time` VARCHAR(50) NOT NULL
	    )"""

	    connection = self.get_connection()
	    cursor = connection.cursor();

	    cursor.execute(script)