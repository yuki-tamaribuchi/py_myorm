import mysql.connector
from mysql.connector import errorcode

from framework.exceptions.connection import DatabaseCreatedException

from settings.databases import user, password, host, database


def connect():
	try:
		cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
		return cnx
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_BAD_DB_ERROR:
			with mysql.connector.connect(user=user, password=password, host=host) as cnx:
				cursor = cnx.cursor()
				sql = "CREATE DATABASE {}".format(database)
				cursor.execute(sql)
				raise DatabaseCreatedException(database)
		else:
			raise err

