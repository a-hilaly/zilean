BEGIN;

/*
    Machine traffic
*/

CREATE TABLE `machine_tcp_history` (
  `id` INT(12) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
)

ALTER TABLE `machine_tcp_history` AUTO_INCREMENT = 0;

COMMIT;
