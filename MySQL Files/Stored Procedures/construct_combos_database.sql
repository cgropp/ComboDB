CREATE TABLE `combos` (
  `combo_id` int NOT NULL AUTO_INCREMENT,
  `game` varchar(45) NOT NULL,
  `char_name` varchar(45) NOT NULL,
  `combo` varchar(1000) NOT NULL,
  `position` varchar(45) DEFAULT NULL,
  `damage` int DEFAULT NULL,
  `meter` varchar(45) DEFAULT NULL,
  `difficulty` varchar(45) DEFAULT NULL,
  `notes` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`combo_id`)
) 