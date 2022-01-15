from typing import Type

from framework.operates.executes import execute_select

from framework.models.base import ModelBase
from framework.models.fields import FieldBase

from framework.exceptions.select import SelectFieldError

class SelectRecord:
	def __init__(self, model_instance:Type[ModelBase], select_fields:dict=None, select_condition:dict=None):
		self.model_instance = model_instance
		self.select_fields = select_fields
		self.select_condition = select_condition

		self.model_fields_dict = {}
		self.select_data_dict = {}
		self.sql = ""
		self.result = None

	def create_model_fields_dict(self):
		for k, v in self.model_instance.__dict__.items():
			if issubclass(v.__class__, FieldBase):
				self.model_fields_dict[k] = v
		return True

	def create_select_data_dict(self):
		self.select_data_dict['table_name'] = self.model_instance.__name__.lower()

		self.select_data_dict['fields']={}
		for k, v in self.select_fields.items():
			if k in self.model_fields_dict:
				
				self.select_data_dict['fields'][k]={}
				self.select_data_dict['fields'][k]['field_instance'] = self.model_fields_dict[k]
				self.select_data_dict['fields'][k]['select_value'] = v
			else:
				raise SelectFieldError(k)

		return True

	def create_sql(self):
		SQL_TEMPLATE = "SELECT {field_names} FROM {table_name}"

		field_names_arr = [field_name for field_name in self.select_data_dict['fields']]
		field_names_sql = ", ".join(field_names_arr)
		
		sql = SQL_TEMPLATE.format(
			field_names=field_names_sql,
			table_name=self.select_data_dict['table_name']
		)

		self.sql = sql
		return True


	def execute_sql(self):
		self.results = execute_select(self.sql)

	
	def select_data(self):
		self.create_model_fields_dict()
		self.create_select_data_dict()
		self.create_sql()
		self.execute_sql()
		return self.results