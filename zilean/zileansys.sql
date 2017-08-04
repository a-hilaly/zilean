BEGIN;

/*
    Zilean System Database
*/

CREATE DATABASE zileansystem;

USE zileansystem;

CREATE TABLE `zilean_env` (
  `mode` VARCHAR(25) NOT NULL,
  `status` enum('active', 'null') DEFAULT 'null',
  `working_directory` VARCHAR(50) NOT NULL,
  `mysql_connector_use_pure` BOOLEAN DEFAULT 1,
  `recording_sessions` BOOLEAN DEFAULT 1,
  `recording_pen_history` BOOLEAN DEFAULT 1,
  `recording_fails` BOOLEAN DEFAULT 1,
  `recording_db_backups` BOOLEAN DEFAULT 1,
  `recording_dr_backups` BOOLEAN DEFAULT 1,
  `default_backup_type` VARCHAR(10) DEFAULT 'default',
  PRIMARY KEY (`mode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `zilean_env` (`mode`, `status`, `working_directory`)
VALUES (
  'zilean_default_mode',
  'active',
  'zilean-path-not-implmented'
);

CREATE TABLE `zilean_linked_databases` (
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
