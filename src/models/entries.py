from framework.models.base import ModelBase
from framework.models.fields import Foreign

from models.users import Users


class Entries(ModelBase):
	user = Foreign(Users, on_delete=True)
