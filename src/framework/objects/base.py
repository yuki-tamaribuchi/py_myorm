class ObjectsBase(object):
	def __init__(self, model_instance):
		self.model_instance = model_instance

	def create(self, **kwargs):
		from framework.operates.insert import InsertRecord

		insert_data = kwargs
		insert = InsertRecord(self.model_instance, insert_data)
		insert.execute_sql()


	def update(self, *args, **kwargs):
		pass

	def delete(self, *args, **kwargs):
		pass

	def all(self, *args, **kwargs):
		pass

	def get(self, *args, **kwargs):
		pass

	def filter(self, *args, **kwargs):
		pass

	def first(self, *args, **kwargs):
		pass

	def last(self, *args, **kwargs):
		pass

	def exist(self, *args, **kwargs):
		pass