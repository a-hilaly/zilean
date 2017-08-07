BEGIN;

/*
    Zilean Cache Databases
*/

CREATE DATABASE zileancache;

USE zileancache;

CREATE TABLE `zilean_sessions` (
  `session_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `status` enum('active', 'inactive', 'failed', 'aboarted') DEFAULT 'active',
  `starting_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `finished_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `success_rate` INT(3) NOT NULL DEFAULT 100,
  `executed_jobs` JSON,
  PRIMARY KEY (`session_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `zilean_sessions` AUTO_INCREMENT = 0;

CREATE TABLE `zilean_moves_history` (
  `move_id` INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `started_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `finished_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `function` VARCHAR(25) NOT NULL,
  `arguments` JSON,
  `out_put` JSON,
  `success` BOOLEAN DEFAULT 0,
  PRIMARY KEY (`move_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `zilean_moves_history` AUTO_INCREMENT = 0;

CREATE TABLE `zilean_intern_fails` (
  `fail_id` INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `move_id`INT(10) unsigned NOT NULL,
  `type` enum(
                'logs',
                'config',
                'mysql_query',
                'mysql_conection',
                'architecture',
                'outer',
                'intern2',
                'unknown',
                'unclassified'
              ) NOT NULL DEFAULT 'unclassified',
  `recorded_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `function` VARCHAR(30) NOT NULL,
  `module` VARCHAR(20) NOT NULL,
  `error_id` INT(5),
  `related_fails` JSON,
  `ocuracy` INT(4),
  PRIMARY KEY (`fail_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `zilean_intern_fails` AUTO_INCREMENT = 0;

CREATE TABLE `zilean_extern_fails` (
  `fail_id` INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `caller` VARCHAR(30) NOT NULL,
  `called_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `function` VARCHAR(30) NOT NULL,
  `arguments` JSON,
  `out_put` JSON,
  PRIMARY KEY (`fail_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `zilean_extern_fails` AUTO_INCREMENT = 0;

CREATE TABLE `zilean_database_backups` (
  `backup_id` INT(8) unsigned  NOT NULL AUTO_INCREMENT,
  `targeted_databases` VARCHAR(25) NOT NULL,
  `forced_ignore` BOOLEAN DEFAULT 0,
  `started_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `finished_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `exit_status` INT(5) NOT NULL DEFAULT -9999,
  `working_directory` VARCHAR(50) NOT NULL,
  `runtime` INT(5) NOT NULL,
  PRIMARY KEY (`backup_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `zilean_database_backups` AUTO_INCREMENT = 0;

CREATE TABLE `zilean_directory_backups` (
  `backup_id` INT(8) unsigned NOT NULL AUTO_INCREMENT,
  `target_directory` VARCHAR(25) NOT NULL,
  `forced_ignore` BOOLEAN DEFAULT 0,
  `started_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `finished_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `exit_status` INT(5) NOT NULL DEFAULT -9999,
  `working_directory` VARCHAR(50) NOT NULL,
  `runtime` INT(5) NOT NULL,
  PRIMARY KEY (`backup_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `zilean_directory_backups` AUTO_INCREMENT = 0;

COMMIT;
