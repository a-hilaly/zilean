#!/bin/bash

source $ZILEAN_SQL/_mysqltools.sh

function _api () {
    cmd=$1
    trg1=$2
    trg2=$3
    if [ "$cmd" = "read" ]; then
        mysql_read $trg1 $trg2
    elif [ "$cmd" = "dump" ]; then
        mysql_dump_database $trg1 $trg2
    else
        return 2
    fi
}

_api $1 $2 $3
