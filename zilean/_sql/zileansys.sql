BEGIN;

/*
    Zilean System Database
*/

CREATE DATABASE zileansystem;

USE zileansystem;

CREATE TABLE `zilean_service` (
  `service` VARCHAR(30) NOT NULL,
  `status` BOOLEAN NOT NULL DEFAULT 0,
  PRIMARY KEY (`service`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `zilean_serve`
  (`service`)
VALUES
  ('db_backup'),
  ('safety_switch'),
  ('mysql_security');

CREATE TABLE `zilean_registred_machines` (
  `machine_id` INT(5) NOT NULL AUTO_INCREMENT,
  `machine_name` VARCHAR(30) NOT NULL,
  `owner` VARCHAR(30) DEFAULT "NaN",
  `alias` JSON DEFAULT '[]',
  `extra` JSON DEFAULT '{}',
  `adress` VARCHAR(30),
  `type` enum(
                'intern',
                'local',
                'virtual',
                'hard',
                'unkown'
              ) DEFAULT 'unknown',
  `authorisation` VARCHAR(30) DEFAULT "UNDEFINED",
  `front_database` VARCHAR(30) NOT NULL,
  `zilean_auto_backup` BOOLEAN NOT NULL DEFAULT 0,
  PRIMARY KEY (`machine_name`)
)

ALTER TABLE `machine_id` AUTO_INCREMENT = 0;

CREATE TABLE `zilean_linked_databases` (
  `database_id` INT(5) NOT NULL AUTO_INCREMENT,
  `database` VARCHAR(25) NOT NULL,
  `local` BOOLEAN NOT NULL DEFAULT 0,
  `linked_time` timestamp DEFAULT CURRENT_TIMESTAMP,
  `last_backup_id` VARCHAR(30) DEFAULT 'none',
  PRIMARY KEY (`database`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `zilean_linked_databases` AUTO_INCREMENT = 0;

COMMIT;
