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
def call_insert_combo(gameV, char_nameV, comboV, positionV, damageV, meterV, difficultyV, notesV):
	try:
		db = mysql.connector.connect(**dbconfig)
		cursor = db.cursor()
		
		args = [gameV, char_nameV, comboV, positionV, damageV, meterV, difficultyV, notesV]
		result = cursor.callproc('insert_combo', args)
		db.commit()

		print(cursor.rowcount, "record inserted.")
		
		for result in cursor.stored_results():
			print(result.fetchall())
		
	except Error as e:
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