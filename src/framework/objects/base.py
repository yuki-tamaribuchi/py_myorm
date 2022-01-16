from framework.operates.executes import execute, fetch

class ObjectsBase(object):
	def __init__(self, model_instance):
		self.model_instance = model_instance
		self.mode = ""
		self.sql = ""

	def create(self, **kwargs):
		from framework.operates.insert import InsertRecord

		self.mode="execute"

		insert_data = kwargs
		insert = InsertRecord(self.model_instance, insert_data)
		self.sql = insert.get_sql()
		return self


	def update(self, *args, **kwargs):
		pass

	def delete(self, *args, **kwargs):
		pass

	def all(self):
		from framework.operates.select import SelectRecord

		self.mode = "fetch"
		select = SelectRecord(self.model_instance)
		self.sql = select.get_sql()
		return self

	def get(self, **kwargs):
		from framework.operates.select import SelectRecord

		self.mode = "fetch"
		where_data = kwargs
		select = SelectRecord(self.model_instance, where_data)
		self.sql = select.get_sql()
		return self
		

	def filter(self, *args, **kwargs):
		pass

	def first(self, *args, **kwargs):
		pass

	def last(self, *args, **kwargs):
		pass

	def exist(self, *args, **kwargs):
		pass

	def run(self):
		if self.mode == "execute":
			return execute(self.sql)
		elif self.mode == "fetch":
			return fetch(self.sql)
		else:
			print("Please set mode \"execute\" or \"fetch\"")
