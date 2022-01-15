import mysql.connector
from mysql.connector import errorcode

from framework.exceptions.connection import DatabaseCreatedException
from framework.connections.connection import connect


def execute(sql, data=None):
	try:
		with connect() as cnx:
			try:
				with cnx.cursor() as cursor:
					cursor.execute(sql, data)
					cnx.commit()

				#cursor = 
				#cursor.execute(sql, data)
				#cnx.commit()
			except	mysql.connector.Error as err:
				if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
					print('already exists.')
				else:
					raise err
	except DatabaseCreatedException:
		print('Please try again')


def execute_select(sql, data=None):
	results = []
	try:
		with connect() as cnx:
			try:
				with cnx.cursor() as cursor:
					cursor.execute(sql)
					
					for result in cursor:
						results.append(result)
				return results
			except	mysql.connector.Error as err:
				if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
					print('already exists.')
				else:
					raise err
	except DatabaseCreatedException:
		print('Please try again')