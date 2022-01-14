import mysql.connector
from mysql.connector import errorcode

from framework.exceptions.connection import DatabaseCreatedException
from framework.connections.connection import connect


def execute(sql):
	try:
		with connect() as cnx:
			try:
				cursor = cnx.cursor()
				result = cursor.execute(sql)
				return result
			except	mysql.connector.Error as err:
				if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
					print('already exists.')
				else:
					raise err
	except DatabaseCreatedException:
		execute(sql)