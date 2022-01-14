from framework.objects.base import ObjectsBase


class ModelBase(object):

	def __init__(self):
		self.objects = ObjectsBase(self)