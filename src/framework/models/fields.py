from framework.models.base import ModelBase

from framework.exceptions.validation import DataTypeValidationError, NullValidationError, MaxLengthValidationError


class FieldBase(object):

	data_type = None

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

		#データ型検証
		if (self.data_type is not None and not self.data_type==type(data)):
			raise DataTypeValidationError(field_name)
			

		#nullを許可しない、かつ、dataがnullの場合
		if (not self.null) and (data is None):
			#auto_incrementアトリビュートがあり、auto_incrementする場合は成功
			if hasattr(self, 'auto_increment') and self.auto_increment:
				pass
			#auto_incrementアトリビュートがない、または、auto_incrementしないもの場合はエラー
			else:
				raise NullValidationError(field_name)
		
		return True
		#uniqueは一旦おいておく

	


	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, value):
		self._value = value




class RelationBase(FieldBase):

	data_type = int

	def __init__(self, rel_model:ModelBase, on_delete:bool, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.rel_model = rel_model
		self.on_delete = on_delete
	
	def __str__(self):
		return str(self.rel_model)

	def field_sql(self):
		
		sql = "INT NOT NULL"

		return sql

	



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

	def validate(self, field_name, data):
		super_validate_result = super().validate(field_name, data)

		if super_validate_result:
			if self.max_length<len(data):
				raise MaxLengthValidationError(field_name)

			return True





class One2One(RelationBase):
	pass


class Foreign(RelationBase):
	pass
	