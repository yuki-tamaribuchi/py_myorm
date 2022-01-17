class SelectFieldError(Exception):
	def __init__(self, field_name):
		print('Select field error: {}'.format(field_name))

class WhereClauseNotSpecifiedException(Exception):
	def __init__(self, model_name):
		print('Where clause was not specified: {}'.format(model_name))

class ResultNotOneException(Exception):
	def __init__(self):
		print("Results are not one. Please add more where clause or use filter function.")