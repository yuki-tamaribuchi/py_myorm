SELECT_TEMPLATE = "SELECT {options} {columns} FROM {table} {join} {where} {order_by} {having} {limit}"
INSERT_TEMPLATE = "INSERT INTO {table} ({columns}) VALUES ({values})"
UPDATE_TEMPLATE = "UPDATE {table} SET {sets} {where}"
DELETE_TEMPLATE = "DELETE FROM {table} {where} {order_by} {limit}"

def generate(sql_data_dict):
	if sql_data_dict['sql_mode'] == "select":
		template = SELECT_TEMPLATE

		if "options" in sql_data_dict:
			options = sql_data_dict['options']
		else:
			options = ""
		
		if "table_name" in sql_data_dict:
			table = sql_data_dict['table_name']
		else:
			print('Please specify table')

		if "columns" in sql_data_dict:
			columns = ", ".join(sql_data_dict['columns'])
		else:
			columns = "*"

		if "join" in sql_data_dict:
			pass
		else:
			join = ""

		field_names_arr = []
		field_values_arr = []
		if "where" in sql_data_dict:
			for field_name in sql_data_dict["where"]:
				field_names_arr.append(field_name)
				field_values_arr.append("\"" + sql_data_dict["where"][field_name]["value"] + "\"")
				field_name_and_value_arr = ["{} = {}".format(name, value) for name, value in zip(field_names_arr, field_values_arr)]
				where = "WHERE " + " AND ".join(field_name_and_value_arr)
		else:
			where = ""

		order_by = ""
		having = ""
		limit = ""

		sql = template.format(
			options=options,
			columns=columns,
			table=table,
			join=join,
			where=where,
			order_by=order_by,
			having=having,
			limit=limit
		)

		return sql
			