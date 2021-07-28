CREATE DEFINER=`PythonDBUser`@`%` PROCEDURE `select_char_combos`(gameV varchar(45),
								char_nameV varchar(45)
                                )
BEGIN
	IF gameV IS NULL OR char_nameV IS NULL THEN
		SIGNAL SQLSTATE '22004'
			SET MESSAGE_TEXT = 'Game name and character name, must not be NULL';
            
	ELSEIF NOT EXISTS(
		SELECT *
        FROM combos
        WHERE
        game = gameV AND
        char_name = char_nameV
        ) THEN
			SIGNAL SQLSTATE'45000'
				SET MESSAGE_TEXT = 'This character does not have any combos in the database';
	ELSE
		SELECT *
        FROM combos
        WHERE
        game = gameV AND
        char_name = char_nameV;
    END IF;
END