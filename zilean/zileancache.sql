BEGIN;

/*
    Zilean Cache Databases
*/

CREATE DATABASE zileancache;

CREATE TABLE `` (

);

CREATE TABLE `zilean_sessions` (
  `session_id` VARCHAR(10) NOT NULL,
  `status` VARCHAR(5) NOT NULL,
  `starting_time` VARCHAR(25) NOT NULL,
  `ending_time` VARCHAR(25) NOT NULL,
  `success_rate` INT(3) NOT NULL,
);

CREATE TABLE `zilean_intern_jobs` (
  `job_id` INT(8) NOT NULL,
  `sub_jobs_id` VARCHAR(25) NOT NULL,
  `finished` BOOLEAN NOT NULL,
  `lunch_time` VARCHAR(25) NOT NULL,
);

CREATE TABLE `zilean_pen_history`(

);

CREATE TABLE `zilean_fails` (
  `fail_id` INT(8) NOT NULL,
  `type` VARCHAR(10) NOT NULL,
  `time` VARCHAR(25) NOT NULL,
  `called_function` VARCHAR(25) NOT NULL,
  `error_id` INT(10) NOT NULL,
  `job_id` INT(10) NOT NULL,
  `out_put` VARCHAR(25) NOT NULL,
  `arguments` VARCHAR(25) NOT NULL,
  `related_fails` VARCHAR(25) NOT NULL,
  `ocuracy` VARCHAR(25) NOT NULL,
);

CREATE TABLE `zilean_backups` (
  `backup_id` INT(8) NOT NULL,
  `targeted_databases` VARCHAR(25) NOT NULL,
  `forced_ignore` VARCHAR(25) NOT NULL,
  `lunch_time` VARCHAR(25) NOT NULL,
  `stop_time` VARCHAR(25) NOT NULL,
  `exit_status` VARCHAR(5) NOT NULL,
  `working_directory` VARCHAR(5) NOT NULL,
  `runtime` VARCHAR(5) NOT NULL,
);

COMMIT;
