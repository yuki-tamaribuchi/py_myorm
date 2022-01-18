from framework.exceptions.filter import FieldNotFoundException

def create_filter(model_fields_dict:dict, where_data_dict:dict):
	
	filter_dict = {}

	for k, v in where_data_dict.items():
		if k in model_fields_dict:
			filter_dict[k] = {}
			filter_dict[k]['value'] = v
		else:
			raise FieldNotFoundException(k)
	return filter_dict
