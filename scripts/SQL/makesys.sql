BEGIN;

/*
    Zilean System Database
*/

CREATE DATABASE zileansystem;

USE zileansystem;

CREATE TABLE `zilean_registred_machines` (
  `machine_id` INT(5) NOT NULL AUTO_INCREMENT,
  `machine_name` VARCHAR(50) NOT NULL,
  `host` VARCHAR(50) NOT NULL DEFAULT '__local__',
  `owner` VARCHAR(50) DEFAULT "NaN",
  `extra` JSON DEFAULT '{}',
  `type` enum(
                'intern',
                'local',
                'virtual',
                'hard',
                'unknown'
              ) DEFAULT 'unknown',
  `front_database` VARCHAR(30) NOT NULL,
  `other_databases` JSON DEFAULT '[]',
  `zilean_auto_backup` BOOLEAN NOT NULL DEFAULT 0,
  PRIMARY KEY (`machine_name`)
)

ALTER TABLE `machine_id` AUTO_INCREMENT = 0;

CREATE TABLE `zilean_linked_databases` (
  `database_id` INT(5) NOT NULL AUTO_INCREMENT,
  `database` VARCHAR(25) NOT NULL,
  `local` BOOLEAN NOT NULL DEFAULT 0,
  `linked_time` timestamp DEFAULT CURRENT_TIMESTAMP,
  `last_backup_id` VARCHAR(30) DEFAULT 'NaN',
  `last_backup_time` timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`database`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `zilean_linked_databases` AUTO_INCREMENT = 0;

COMMIT;
