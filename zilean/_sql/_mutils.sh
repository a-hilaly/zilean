#!/bin/bash

source $HOME/machineenv.sh
#XXX: OR the next line should be already exported at the machine
# creation
#mysql=$MYSQL_PATH

zilean_sys="$ZILEAN_SQL/zileansys.sql"
zilean_cache="$ZILEAN_SQL/zileancache.sql"
zileanmdb_fails="$ZILEAN_SQL/setfails.sql"
zileanmdb_moves="$ZILEAN_SQL/setmoves.sql"
zileanmdb_performances="$ZILEAN_SQL/setperformances.sql"
zileanmdb_traffic="$ZILEAN_SQL/settraffic.sql"
zilean_clear="$ZILEAN_SQL/zileanclear.sql"
zilean_pysqlboost="$ZILEAN_SQL/zsqlmake.py"
zilean_temp="$ZILEAN_WORKING_DIR/zileantemp"
z_user=""
z_password=""
zc="zileancache"
zs="zileansys"

alias mkzileantemp='mkdir $zilean_temp'
alias clzileantemp='rm -rf $zilean_temp'

function clear_temp() {
    if [ -d $zilean_temp ]; then
        rm -rf $zilean_temp/*
    else
        echo "Temp Not Found"
    fi
}

function extract_from_json () {
    file=$1
    target=$2
    res=$(cat $file | jq -r ".$target")
    echo "$res"
}

function extract_mysql_logs () {
    _extract_from_json $1 ".$2"
}

function extract_from_machine_configuration () {
    echo "Not Implemented"
}

z_user='extract_from_json user'
z_password='extract_from_json password'

$@
