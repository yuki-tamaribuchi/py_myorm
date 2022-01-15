from framework.models.base import ModelBase

from framework.exceptions.validation import NullValidationError


class FieldBase(object):
	def __init__(self, null:bool=True, unique:bool=False,*args, **kwargs):
		self._value = None
		self.null = null
		self.unique = unique


	def field_sql(self):
		sql = "{null_option}{unique_option}"

		if self.null:
			null_option = ""
		else:
			null_option = "NOT NULL "
		
		if self.unique:
			unique_option = "UNIQUE "
		else:
			unique_option = ""
		
		sql = sql.format(
			null_option=null_option,
			unique_option=unique_option
		)
		return sql

		#数値の場合auto_incrementが含まれていて、かつ、falseでの場合がエラー
		#それ以外は、nullがfalseの場合エラー
		#(hasattr(self, 'auto_increment') and not self.auto_increment and data is None)

	def validate(self, field_name, data):
		print(self.__dict__)

		#nullを許可しない、かつ、dataがnullの場合
		if (not self.null) and (data is None):
			#auto_incrementアトリビュートがあり、auto_incrementする場合は成功
			if hasattr(self, 'auto_increment') and self.auto_increment:
				pass
			#auto_incrementアトリビュートがない、または、auto_incrementしないもの場合はエラー
			else:
				raise NullValidationError(field_name)
		

		#uniqueは一旦おいておく


	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, value):
		self._value = value




class RelationBase(FieldBase):

	def __init__(self, rel_model:ModelBase, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.rel_model = rel_model
	
	def __str__(self):
		return str(self.rel_model)
	



class IntegerField(FieldBase):

	data_type = int

	def __init__(self, auto_increment:bool=False, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.auto_increment = auto_increment

	def field_sql(self):
		super_sql = super().field_sql()


		if self.auto_increment:
			auto_increment_option = "AUTO_INCREMENT "
		else:
			auto_increment_option = ""

		sql = "INT " + super_sql + "{auto_increment_option}".format(
			auto_increment_option=auto_increment_option
		)

		return sql

	

class StringField(FieldBase):

	data_type = str

	def __init__(self, max_length:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.max_length = max_length

	def field_sql(self):
		super_sql = super().field_sql()


		sql = "VARCHAR({max_length}) ".format(
			max_length=self.max_length
		) + super_sql

		return sql



class One2One(RelationBase):
	pass


class Foreign(RelationBase):
	pass
	