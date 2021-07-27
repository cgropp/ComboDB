CREATE DEFINER=`PythonDBUser`@`%` PROCEDURE `insert_combo`(gameV varchar(45),
															 characterV varchar(45),
															 comboV varchar(1000), 
															 positionV varchar(45), 
															 damageV int, 
															 meterV varchar(45), 
															 difficultyV varchar(45), 
															 notesV varchar(500)
															 )
BEGIN
	IF gameV IS NULL OR characterV IS NULL OR comboV IS NULL THEN
		SIGNAL SQLSTATE '22004'
			SET MESSAGE_TEXT = 'Game name, character name, and combo must not be NULL';
    
    ELSEIF EXISTS(
		SELECT *
        FROM combos
        WHERE
        game = gameV AND
        `character` = characterV AND
        combo = comboV
        ) THEN
			SIGNAL SQLSTATE'45000'
				SET MESSAGE_TEXT = 'This combo is already in the database';
	ELSE
		INSERT INTO combos
					(combo_id,
					 game,
					 `character`,
					 combo,
					 position,
					 damage,
					 meter,
					 difficulty,
					 notes)
		VALUES     ( DEFAULT,
					 gameV,
					 characterV,
					 comboV,
					 positionV,
					 damageV,
					 meterV,
					 difficultyV,
					 notesV);
	END IF;
END