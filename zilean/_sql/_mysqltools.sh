#!/bin/bash

source $ZILEAN_SQL/_mutils.sh

# MYSQLCMD & MYSQLDUMP should be in shell env or sourced from machineenv.sh

function mysql_read () {
    file=$1
    $MYSQLCMD -u $z_user "-p$z_password" < $file
}

function mysql_dump_database {
    database=$1
    file=$2
    $MYSQLCMD --databases $1 -u $z_user "-p$z_password" > $file
}
