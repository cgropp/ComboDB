CREATE DEFINER=`PythonDBUser`@`%` PROCEDURE `edit_combo`(
	old_gameV varchar(45),
	old_char_nameV varchar(45),
	old_comboV varchar(1000), 
    gameV varchar(45),
    char_nameV varchar(45),
    comboV varchar(1000), 
	positionV varchar(45), 
	damageV int, 
	meterV varchar(45), 
	difficultyV varchar(45), 
	notesV varchar(500)
    
)
BEGIN
	IF gameV IS NULL OR char_nameV IS NULL OR comboV IS NULL OR old_gameV IS NULL OR old_char_nameV IS NULL OR old_comboV IS NULL THEN
		SIGNAL SQLSTATE '22004'
			SET MESSAGE_TEXT = 'Game name, character name, and combo must not be NULL';
            
	ELSEIF NOT EXISTS(
		SELECT *
        FROM combos
        WHERE
        game = old_gameV AND
        char_name = old_char_nameV AND
        combo = old_comboV
        ) THEN
			SIGNAL SQLSTATE'45000'
				SET MESSAGE_TEXT = 'This combo does not exist in the database';
	ELSE
		UPDATE combos
        SET game = gameV,
			char_name = char_nameV,
			combo = comboV,
			position = positionV,
			damage = damageV,
			meter = meterV,
			difficulty = difficultyV,
			notes = notesV
		WHERE combo = old_comboV AND game = old_gameV AND char_name = old_char_nameV;
		
    END IF;
END