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
		self.sql_data_dict = {}


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
				field_instance_and_insert_data['insert_value'] = self.insert_data.pop(k)

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
		

	def create_sql_data_set_dict(self):
		self.sql_data_dict['table_name'] = self.model_instance.__name__.lower()
		self.sql_data_dict['insert_data'] = {}

		for k, v in self.match_dict.items():
			field_name = k

			field_instance = v['field_instance']

			field_instance.validate(k, v['insert_value'])
			self.sql_data_dict['insert_data'][field_name] = v['insert_value']
		return True


	def get_sql_data_dict(self):
		self.create_fields_dict()
		self.create_match_dict()
		self.create_sql_data_set_dict()


		return self.sql_data_dict