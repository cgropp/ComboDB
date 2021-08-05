import mysql.connector

#MySQL connection configuration
dbconfig = {
	'host': "localhost",    
	'user': "PythonDBUser",         
	'passwd': "PythonDBPass",  
	'db': "combo_db"
}

db = mysql.connector.connect(**dbconfig)

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
		
#call_insert_combo('Guilty Gear -Strive-', 'Zato-1', 'CH 2S > 22H', 'Anywhere', -1, 0, '[1] Very Easy', 'Everyone except nago can jump out')		
		
		
# testSelectQuery = "SELECT * FROM clients WHERE client_id > 1;"

# with db.cursor() as cursor:
	# cursor.execute(testSelectQuery)
	# result = cursor.fetchall()
	# for row in result:
		# print(row)
	# cursor.close()




# db.close()