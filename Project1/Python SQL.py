import mysql.connector

#MySQL connection configuration
dbconfig = {
	'host': "localhost",    
	'user': "PythonDBUser",         
	'passwd': "PythonDBPass",  
	'db': "sql_invoicing"
}

db = mysql.connector.connect(**dbconfig)

#Call stored procedure
def call_get_payments(client_id, payment_id):
	try:
		db = mysql.connector.connect(**dbconfig)
		cursor = db.cursor()
		
		args = [client_id,payment_id]
		result = cursor.callproc('get_payments', args)
		
		for result in cursor.stored_results():
			print(result.fetchall())
		
	except Error as e:
		print(e)
		
	finally:
		cursor.close()
		db.close()
		
call_get_payments(1,1)		
		
		
# testSelectQuery = "SELECT * FROM clients WHERE client_id > 1;"

# with db.cursor() as cursor:
	# cursor.execute(testSelectQuery)
	# result = cursor.fetchall()
	# for row in result:
		# print(row)
	# cursor.close()




# db.close()