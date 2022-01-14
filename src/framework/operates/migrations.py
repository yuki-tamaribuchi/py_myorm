from framework.operates.creates import CreateTable


from models import all_model_classes

def get_all_model_classes():
	return all_model_classes


def migrate(model_class):
	create_table = CreateTable(model_class)
	create_table.execute_sql()


def migrate_all_model():
	model_classes = get_all_model_classes()
	for model_class in model_classes:
		migrate(model_class)