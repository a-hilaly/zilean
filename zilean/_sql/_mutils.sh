#!/bin/bash

source $HOME/machineenv.sh
#XXX: OR the next line should be already exported at the machine
# creation
#mysql=$MYSQL_PATH

zilean_sys="$ZILEAN_SQL/zileansys.sql"
zilean_cache="$ZILEAN_SQL/zileancache.sql"
zileanmdb_s1="$ZILEAN_SQL/zileanmdb_s1.sql"
zileanmdb_s2="$ZILEAN_SQL/zileanmdb_s2.sql"
zilean_clear="$ZILEAN_SQL/zileanclear.sql"
zilean_pysqlboost="$ZILEAN_SQL/zsqlmake.py"
zilean_temp="$ZILEAN_WORKING_DIR/zileantemp"
z_user=""
z_password=""
zc="zileancache"
zs="zileansystem"

alias mkzileantemp='mkdir $zilean_temp'
alias clzileantemp='rm -rf $zilean_temp'

function clear_temp() {
    if [ -d $zilean_temp ]; then
        rm -rf $zilean_temp/*
    else
        echo "Temp Not Found"
    fi
}

function _extract_from_json () {
    file=$1
    target=$2
    res=$(cat $file | jq -r ".$target")
    echo "$res"
}

function extract_mysql_logs () {
    _extract_from_json $1 ".mysql.$2"
}

function _extract_from_machine_configuration () {
    python3 greww --data --mysqllogs "$1"
}

z_user='_extract_from_machine_configuration user'
z_password='_extract_from_machine_configuration password'

$@
