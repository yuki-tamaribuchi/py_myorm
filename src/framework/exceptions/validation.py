class DataTypeValidationError(Exception):
	def __init__(self, field_name):
		print('Data Type validation error: {}'.format(field_name))


class NullValidationError(Exception):
	def __init__(self, field_name):
		print('Null validation error: {}'.format(field_name))


class MaxLengthValidationError(Exception):
	def __init__(self, field_name):
		print('Max length validation error: {}'.format(field_name))