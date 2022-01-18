from framework.operates.generate_sql import generate
from framework.operates.executes import execute, fetch

from framework.operates.filters import create_filter

from framework.exceptions.filter import DoNotUseFilterWithGetFunctionException

class ObjectsBase(object):
	def __init__(self, model_instance):
		self.model_instance = model_instance
		self.mode = ""
		self.sql = ""

		self.sql_data_dict = {}

	def create(self, **kwargs):
		from framework.operates.insert import InsertRecord

		self.sql_data_dict['sql_mode'] = "insert"

		insert_data = kwargs
		insert = InsertRecord(self.model_instance, insert_data)
		self.sql_data_dict.update(insert.get_sql_data_dict())
		return self


	def update_one(self, *args, **kwargs):
		return self

	def update_many(self, **kwargs):
		return self

	def delete(self, *args, **kwargs):
		pass

	def all(self):
		from framework.operates.select import SelectRecord

		self.sql_data_dict["sql_mode"] = "select"
		self.sql_data_dict["called_function"] = "all"

		select = SelectRecord(self.model_instance)
		self.sql_data_dict.update(select.get_sql_data_dict())
		return self


	def get(self, **kwargs):
		if kwargs == {}:
			from framework.exceptions.select import WhereClauseNotSpecifiedException
			raise WhereClauseNotSpecifiedException(self.model_instance.__name__)
		

		from framework.operates.select import SelectRecord

		where_data = kwargs
		
		self.sql_data_dict['sql_mode'] = "select"
		self.sql_data_dict['called_function'] = "get"

		select = SelectRecord(self.model_instance, where_data)
		sql_data_dict = select.get_sql_data_dict()

		self.sql_data_dict.update(sql_data_dict)


		return self


	def filter(self, **kwargs):
		if "where" in self.sql_data_dict:
			raise DoNotUseFilterWithGetFunctionException

		where_data = kwargs

		if "sql_mode" in self.sql_data_dict:
			pass
		else:
			from framework.operates.select import SelectRecord

			self.sql_data_dict['sql_mode'] = "select"
			self.sql_data_dict["called_function"] = "filter"

			select = SelectRecord(self.model_instance)
			sql_data_dict = select.get_sql_data_dict()

			self.sql_data_dict.update(sql_data_dict)

			filter_dict = create_filter(self.sql_data_dict['model_fields'], where_data)
			self.sql_data_dict["where"] = filter_dict

		
		return self

	def first(self, *args, **kwargs):
		pass

	def last(self, *args, **kwargs):
		pass

	def exist(self, *args, **kwargs):
		pass

	def run(self):
		sql = generate(self.sql_data_dict)

		if self.sql_data_dict["sql_mode"] == "select":
			if self.sql_data_dict["called_function"] == "get":
				result = fetch(sql)
				if len(result) > 1:
					from framework.exceptions.select import ResultNotOneException
					raise ResultNotOneException
				else:
					return result
			else:
				result = fetch(sql)
				return result
		else:
			print(sql)

		#if self.mode == "execute":
		#	return execute(self.sql)
		#elif self.mode == "fetch":
		#	return fetch(self.sql)
		#else:
		#	print("Please set mode \"execute\" or \"fetch\"")
