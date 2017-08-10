BEGIN;

/*
    machine fails
*/

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

COMMIT;
