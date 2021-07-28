CREATE DEFINER=`PythonDBUser`@`%` PROCEDURE `delete_combo`(gameV varchar(45),
								char_nameV varchar(45),
								comboV varchar(1000))
BEGIN

	IF gameV IS NULL OR char_nameV IS NULL OR comboV IS NULL THEN
		SIGNAL SQLSTATE '22004'
			SET MESSAGE_TEXT = 'Game name, character name, and combo must not be NULL';
            
	ELSEIF NOT EXISTS(
		SELECT *
        FROM combos
        WHERE
        game = gameV AND
        char_name = char_nameV AND
        combo = comboV
        ) THEN
			SIGNAL SQLSTATE'45000'
				SET MESSAGE_TEXT = 'This combo does not exist in the database';
	ELSE
		DELETE FROM combos
		WHERE combo = comboV AND game = gameV AND char_name = char_nameV;
		
    END IF;
END