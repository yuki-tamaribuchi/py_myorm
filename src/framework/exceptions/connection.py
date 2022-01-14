class DatabaseCreatedException(Exception):
	def __init__(self, database):
		print('Database {} was created.'.format(database))
	