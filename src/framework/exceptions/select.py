class SelectFieldError(Exception):
	def __init__(self, field_name):
		print('Select field error: {}'.format(field_name))