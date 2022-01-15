from framework.objects.base import ObjectsBase


class ModelBase(object):

	def __init__(self):
		
		ModelBase.objects = ObjectsBase(self.__class__)