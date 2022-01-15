class InsertDataMissingException(Exception):
	def __init__(self, data_name):
		print('Insert data missing: {}'.format(data_name))