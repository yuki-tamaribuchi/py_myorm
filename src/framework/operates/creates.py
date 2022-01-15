from typing import Type

from framework.models.base import ModelBase
from framework.models.fields import FieldBase, RelationBase

from framework.operates.executes import execute


class CreateTable:
	def __init__(self, model:ModelBase):
		self.model = model
		self.table_arch_dict = {}
		self.sql = ""
	


	def create_table_arch_dict(self):
		table_name = self.model.__name__.lower()

		fields_dict = {}
		for k, v in self.model.__dict__.items():
			if issubclass(v.__class__, FieldBase):
				if issubclass(v.__class__, RelationBase):
					fields_dict[k + "_id"] = v
				else:
					fields_dict[k] = v
		
		self.table_arch_dict = {
			'name':table_name,
			'fields': fields_dict
		}

		return True



	def create_sql(self):
		SQL_TEMPLATE = """
		CREATE TABLE {name} (
		{fields_definition}
		);
		"""

		fields_definition_sql_arr = []
		for k, v in self.table_arch_dict['fields'].items():
			sql = k + " " + v.field_sql()
			fields_definition_sql_arr.append(sql)
		
		fields_definition = ",\n".join(fields_definition_sql_arr)
			


		sql = SQL_TEMPLATE.format(
			name=self.table_arch_dict['name'],
			fields_definition=fields_definition
		)

		self.sql = sql

	

	def execute_sql(self):
		self.create_table_arch_dict()
		self.create_sql()

		execute(self.sql)
		return True