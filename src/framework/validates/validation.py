from typing import Type

from framework.models.fields import FieldBase

def data_validate(data, field_instance:Type[FieldBase]):
	print(field_instance.__dict__)