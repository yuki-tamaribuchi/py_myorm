from typing import Type

from framework.models.base import ModelBase
from framework.models.fields import FieldBase
from framework.validates.validation import data_validate
from framework.operates.executes import execute

from framework.exceptions.insert import InsertDataMissingException

class InsertRecord:
	def __init__(self, model_instance:Type[ModelBase], insert_data:dict):
		self.model_instance = model_instance
		self.insert_data = insert_data
		self.fields_dict = {}
		self.match_dict = {}
		self.data_set_dict = {}
		self.sql = ""
		self.sql_holder_data = ()


	def create_fields_dict(self):
		for k, v in self.model_instance.__dict__.items():
			if issubclass(v.__class__, FieldBase):
				self.fields_dict[k] = v
		return True
	

	def create_match_dict(self):
		for k, v in self.fields_dict.items():
			field_instance_and_insert_data={}
			if k in self.insert_data:
				field_instance_and_insert_data['field_instance'] = v
				field_instance_and_insert_data['insert_data'] = self.insert_data.pop(k)

				self.match_dict[k] = field_instance_and_insert_data
			else:
				if hasattr(self.fields_dict[k], 'auto_increment') and self.fields_dict[k].auto_increment == True:
					pass
					#field_instance_and_insert_data['field_instance'] = v
					#field_instance_and_insert_data['insert_data'] = None
					#self.match_dict[k] = field_instance_and_insert_data
				else:
					raise InsertDataMissingException(k)
		return True
		

	def create_data_set_dict(self):
		self.data_set_dict['table_name'] = self.model_instance.__name__.lower()
		self.data_set_dict['data'] = {}

		for k, v in self.match_dict.items():
			field_name = k

			field_instance = v['field_instance']

			field_instance.validate(k, v['insert_data'])
			self.data_set_dict['data'][field_name] = v['insert_data']
		return True
	
	def create_sql(self):
		SQL_TEMPLATE = "INSERT INTO {table_name} ({field_names_sql}) VALUES ({field_values_holder_sql})"


		field_names_arr = [field_name for field_name, _ in self.data_set_dict['data'].items()]
		field_values_arr = [field_value for _, field_value in self.data_set_dict['data'].items()]
		field_values_holder_arr = ["%(" + field_name + ")s" for field_name, _ in self.data_set_dict['data'].items()]
		
		field_names_sql = ", ".join(field_names_arr)
		field_values_holder_sql = ", ".join(field_values_holder_arr)

		sql = SQL_TEMPLATE.format(
			table_name=self.data_set_dict['table_name'],
			field_names_sql=field_names_sql,
			field_values_holder_sql = field_values_holder_sql
		)

		sql_holder_data_dict = {k:v for k, v in zip(field_names_arr, field_values_arr)}

		self.sql = sql
		self.sql_holder_data = sql_holder_data_dict
		return True

	def execute_sql(self):
		self.create_fields_dict()
		self.create_match_dict()
		self.create_data_set_dict()
		self.create_sql()

		execute(self.sql, self.sql_holder_data)
		return True