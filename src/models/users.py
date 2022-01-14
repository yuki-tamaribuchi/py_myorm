from framework.models.base import ModelBase
from framework.models.fields import IntegerField, StringField


class Users(ModelBase):
	id = IntegerField(auto_increment=True, null=False, unique=True)
	username = StringField(max_length=40, null=False, unique=True)
	handle = StringField(max_length=30, null=True, unique=False)