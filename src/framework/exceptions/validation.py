class NullValidationError(Exception):
	def __init__(self, field_name):
		print('Validation Error: {}'.format(field_name))