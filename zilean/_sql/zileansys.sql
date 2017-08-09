BEGIN;

/*
    Zilean System Database
*/

CREATE DATABASE zileansystem;

USE zileansystem;

CREATE TABLE `zilean_service` (
  `service` VARCHAR(30) NOT NULL,
  `state` BOOLEAN NOT NULL DEFAULT 0,
  `related` JSON DEFAULT '[]',
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
  `alias` JSON DEFAULT '[]'
  `extra` JSON DEFAULT '{}',
  `adress` VARCHAR(30) NOT NULL DEFAULT "255.255.255.255",
  `api` VARCHAR(30) DEFAULT "__localhost__",
  `authorisation` VARCHAR(30) DEFAULT "UNDEFINED",
)

CREATE TABLE `zilean_linked_machines` (
  `machine_id` INT(5) NOT NULL AUTO_INCREMENT,
  `front_database` VARCHAR(15) NOT NULL,
  `backup_directory` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`machine_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `machine_id` AUTO_INCREMENT = 0;

CREATE TABLE `zilean_linked_databases` (
  `database_id` INT(5) NOT NULL AUTO_INCREMENT,
  `database` VARCHAR(25) NOT NULL,
  `linked_time` timestamp DEFAULT CURRENT_TIMESTAMP,
  `id_backups` JSON,
  PRIMARY KEY (`database`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `zilean_linked_directories` (
  `directory` VARCHAR(40) NOT NULL,
  `linked_time` timestamp DEFAULT CURRENT_TIMESTAMP,
  `id_backups` JSON,
  PRIMARY KEY (`directory`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

COMMIT;
