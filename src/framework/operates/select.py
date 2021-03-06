from typing import Type

from framework.models.base import ModelBase
from framework.models.fields import FieldBase
from framework.operates.filters import create_filter
from framework.exceptions.select import SelectFieldError

class SelectRecord:
	def __init__(self, model_instance:Type[ModelBase], where_data:dict=None):
		self.model_instance = model_instance
		self.where_data = where_data

		self.model_fields_dict = {}
		self.sql_data_dict = {}

	def create_model_fields_dict(self):
		for k, v in self.model_instance.__dict__.items():
			if issubclass(v.__class__, FieldBase):
				self.model_fields_dict[k] = v
		self.sql_data_dict['model_fields'] = self.model_fields_dict
		return True

	def create_sql_data_dict(self):
		self.sql_data_dict['table_name'] = self.model_instance.__name__.lower()

		if self.where_data is None:
			pass
		else:
			filter_dict = create_filter(self.model_fields_dict, self.where_data)
			self.sql_data_dict['where'] = filter_dict

		return True



	
	def get_sql_data_dict(self):
		self.create_model_fields_dict()
		self.create_sql_data_dict()
		return self.sql_data_dict