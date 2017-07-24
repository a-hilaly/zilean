/*
* Zilean mysql dependencies
*
*/

/* ZileanDB */

CREATE DATABASE ZileanDB;

/* zilean sessions */

CREATE TABLE `zilean_sessions` (
  `session_id` VARCHAR(10) NOT NULL;
  `status` VARCHAR(5) NOT NULL;
  `starting_time` VARCHAR(25) NOT NULL;
  `ending_time` VARCHAR(25) NOT NULL;
  `success_rate` INT(3) NOT NULL;
)

/* zilean intern jobs */

CREATE TABLE `zilean_intern_jobs` (
  `job_id` INT(8) NOT NULL;
  `sub_jobs_id` VARCHAR(25) NOT NULL;
  `finished` BOOLEAN NOT NULL;
  `lunch_time` VARCHAR(25) NOT NULL;
)

/* zilean fails*/

CREATE TABLE `zilean_fails` (
  `fail_id`
  `type`
  `time`
  `called_function`
  `error_id`
  `job_id`
  `out_put`
  `arguments`
  `related_fails`
  `ocuracy`
)

/* zilean backups */

CREATE TABLE `zilean_backups` (
  `backup_id`
  `targeted_databases`
  `forced_ignore`
  `time`
  `exit_status`
  `working_directory`
  `runtime`

)

/* zilean cache */

CREATE TABLE `zilean_cache` (

)
