import mysql.connector

#MySQL connection configuration
dbconfig = {
	'host': "localhost",    
	'user': "PythonDBUser",         
	'passwd': "PythonDBPass",  
	'db': "combo_db"
}

#db = mysql.connector.connect(**dbconfig)

#Call stored procedure
def call_insert_combo(gameV, char_nameV, comboV, positionV, damageV, meterV, difficultyV, notesV) -> str:
	try:
		db = mysql.connector.connect(**dbconfig)
		cursor = db.cursor()
		
		args = [gameV, char_nameV, comboV, positionV, damageV, meterV, difficultyV, notesV]
		result = cursor.callproc('insert_combo', args)
		db.commit()

		print(cursor.rowcount, "record inserted.")
		
		for result in cursor.stored_results():
			print(result.fetchall())
		
	except mysql.connector.Error as e:
		#print(e)
		#Test detailed error messages
		# print ("Error code:", e.errno)        # error number
		# print ("SQLSTATE value:", e.sqlstate) # SQLSTATE value
		# print ("Error message:", e.msg)       # error message
		# print ("Error:", e)                   # errno, sqlstate, msg values
		# s = str(e)
		# print ("Error:", s)                   # errno, sqlstate, msg values
		return e.sqlstate
		print(e)

	finally:
		cursor.close()
		db.close()
		
#Call stored procedure
def call_select_char_combos(gameV, char_nameV) -> str:
	try:
		db = mysql.connector.connect(**dbconfig)
		cursor = db.cursor()
		
		args = [gameV, char_nameV]
		
		result = cursor.callproc('select_char_combos', args)
		
		#TODO: Figure out how to get number of records 
		#print(cursor[2].rowcount, "record(s) found.")
		
		for result in cursor.stored_results():
			print(result.fetchall())
		
	except mysql.connector.Error as e:
		return e.sqlstate
		print(e)

	finally:
		cursor.close()
		db.close()
		
		
# testSelectQuery = "SELECT * FROM clients WHERE client_id > 1;"

# with db.cursor() as cursor:
	# cursor.execute(testSelectQuery)
	# result = cursor.fetchall()
	# for row in result:
		# print(row)
	# cursor.close()




# db.close()