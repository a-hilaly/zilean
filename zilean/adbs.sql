BEGIN;

/*
    Assisted database sample
*/


CREATE TABLE `machine_registred_moves` (
  `move_id` INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `caller` VARCHAR(30) NOT NULL,
  `called_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `function` VARCHAR(30) NOT NULL,
  `arguments` JSON,
  `out_put` JSON,
  `success` BOOLEAN NOT NULL DEFAULT 1;
  PRIMARY KEY (`move_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `machine_registred_moves` AUTO_INCREMENT = 0;

CREATE TABLE `machine_registred_fails` (
  `fail_id` INT(10) unsigned NOT NULL AUTO_INCREMENT,
  `caller` VARCHAR(30) NOT NULL,
  `called_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `function` VARCHAR(30) NOT NULL,
  `arguments` JSON,
  `out_put` JSON,
  PRIMARY KEY (`fail_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `machine_registred_fails` AUTO_INCREMENT = 0;

/*
CREATE TABLE `machine_tcp_history` (
  `id` INT(12) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
)

ALTER TABLE `machine_tcp_history` AUTO_INCREMENT = 0;


CREATE TABLE `machine_performance_history` (

)
*/

COMMIT;
