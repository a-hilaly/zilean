BEGIN;

/*
    Machine Performance
*/


CREATE TABLE `machine_performance_history` (
  `id` INT(12) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
)

ALTER TABLE `machine_performance_history` AUTO_INCREMENT = 0;

COMMIT;
