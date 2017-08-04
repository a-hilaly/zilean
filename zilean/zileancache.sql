BEGIN;

/*
    Zilean Cache Databases
*/

CREATE DATABASE zileancache;

CREATE TABLE `zilean_sessions` (
  `session_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `status` enum('active', 'inactive', 'failed', 'aboarted') DEFAULT 'active',
  `starting_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `finished_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `success_rate` INT(3) NOT NULL DEFAULT 100,
  `executed_jobs` JSON,
  PRIMARY KEY (`session_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `zilean_intern_jobs` (
  `job_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `sub_jobs` JSON,
  `status` enum('active', 'inactive', 'failed', 'finished'),
  `started_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `finished_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`job_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `zilean_pen_history` (
  `zilean_move_id` INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `job_id` INT(10) NOT NULL,
  `started_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `finished_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `function` VARCHAR(25) NOT NULL,
  `arguments` JSON,
  `out_put` JSON,
  `success` BOOLEAN DEFAULT 0,
  PRIMARY KEY (`zilean_move_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `zilean_fails` (
  `fail_id` INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `move_id` INT(10) NOT NULL,
  `type` enum('intern', 'mysql_query', 'mysql_conection', 'outer', 'unknown', 'unclassified'),
  `record_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `called_function` VARCHAR(50) NOT NULL,
  `error_id` INT(5) NOT NULL,
  `job_id` INT(10) NOT NULL,
  `out_put` JSON,
  `arguments` JSON,
  `related_fails` JSON,
  `ocuracy` INT(4) NOT NULL,
  PRIMARY KEY (`fail_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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

CREATE TABLE `zilean_directory_backups` (
  `backup_id` INT(8) NOT NULL,
  `target_directory` VARCHAR(25) NOT NULL,
  `forced_ignore` BOOLEAN DEFAULT 0,
  `started_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `finished_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `exit_status` INT(5) NOT NULL DEFAULT -9999,
  `working_directory` VARCHAR(50) NOT NULL,
  `runtime` INT(5) NOT NULL,
  PRIMARY KEY (`backup_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


COMMIT;
