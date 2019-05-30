import pymysql.cursors

class Cmysql():
	def conectar(self):
		_db_host = 'localhost'
		_db_user = 'root'
		_db_password = '12345'
		_db_name = 'classicmodels'
		
		try:
			_connection = pymysql.connect(host = _db_host, 
										 user = _db_user,
										 password = _db_password,
										 db = _db_name,
										 cursorclass = pymysql.cursors.DictCursor)
										 
			return _connection, _connection.cursor()
		
		except pymysql.InternalError as error:
			code, message = error.args
			print ("Error: ", code, message)
