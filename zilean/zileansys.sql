BEGIN;

/*
    Zilean System Database
*/

CREATE DATABASE zileansystem;

CREATE TABLE `zilean_env` (
  `mode` VARCHAR(25) NOT NULL,
  `working_directory` VARCHAR(25) NOT NULL,
  `_use_pure` BOOLEAN NOT NULL,
  `databases` VARCHAR(25) NOT NULL,
  `recording_pen_history` BOOLEAN NOT NULL,
  `recording_fails` BOOLEAN NOT NULL,
  `recording_intern_jobs` BOOLEAN NOT NULL,
  `recording_sessions` BOOLEAN NOT NULL,
  `back_type` VARCHAR(25) NOT NULL,
)

CREATE TABLE `zilean_linked_databases` (
  `database` VARCHAR(25) NOT NULL,
  `linked_time` VARCHAR(25) NOT NULL,
  `backups_id` VARCHAR(25) NOT NULL,
  `formal_size` VARCHAR(25) NOT NULL,
  `extra_info` VARCHAR(25) NOT NULL,
);

COMMIT;
