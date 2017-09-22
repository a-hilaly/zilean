#!/bin/bash

# MYSQLCMD & MYSQLDUMP should be in shell env or sourced from machineenv.sh

function mysql_read () {
    file=$1
    db=$2
    if [ -n "$db" ]; then
        $MYSQLCMD -u $z_user "-p$z_password" $db < $file
    else
        $MYSQLCMD -u $z_user "-p$z_password" < $file
    fi
}

function mysql_backup_database {
    database=$1
    file=$2
    $MYSQLDUMPCMD --databases $database -u $z_user "-p$z_password" > $file
}

$@
