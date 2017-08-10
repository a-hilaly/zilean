BEGIN;

/*
    Zilean Cache Databases
*/

CREATE DATABASE zileancache;

USE zileancache;

ALTER TABLE `zilean_sessions` AUTO_INCREMENT = 0;

CREATE TABLE `zilean_moves_history` (
  `move_id` INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `timed_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `module` VARCHAR(25) NOT NULL,
  `class` VARCHAR(25),
  `function` VARCHAR(25) NOT NULL,
  `arguments` JSON,
  `out_put` JSON,
  `run_time` INT(15),
  `success` BOOLEAN NOT NULL DEFAULT 0,
  PRIMARY KEY (`move_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `zilean_moves_history` AUTO_INCREMENT = 0;

CREATE TABLE `zilean_backups_history` (
  `backup_id` INT(8) unsigned  NOT NULL AUTO_INCREMENT,
  `targeted_databases` VARCHAR(30) NOT NULL,
  `started_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `finished_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `exit_status` INT(5) NOT NULL DEFAULT -9999,
  `working_directory` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`backup_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `zilean_database_backups` AUTO_INCREMENT = 0;

CREATE TABLE `zilean_migration_history` (
  `migration_id` INT(8) unsigned NOT NULL AUTO_INCREMENT,
  `target_database` VARCHAR(30) NOT NULL,
  `started_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `finished_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `exit_status` INT(5) NOT NULL DEFAULT -9999,
  `working_directory` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`backup_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `zilean_directory_backups` AUTO_INCREMENT = 0;

COMMIT;
