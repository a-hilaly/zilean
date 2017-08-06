#!/bin/bash

mysql=$MYSQL_PATH
config_file="$ZILEAN_PATH/zilean/config.json"
zilean_sys="$ZILEAN_PATH/zilean/zileansys.sql"
zilean_cache="$ZILEAN_PATH/zilean/zileancache.sql"
zilean_clear="$ZILEAN_PATH/zilean/zileanclear.sql"

function _extract_from_json () {
    file=$1
    target=$2
    res=$(cat $file | jq -r ".$target")
    echo "$res"
}

function extract_mysql_logs () {
    _extract_from_json $1 ".mysql.$2"
}

zuser='extract_mysql_logs $config_file user'
zpassword='extract_mysql_logs $config_file password'

function make_zilean_mysql_dependencies () {
  $mysql -u $zuser "-p$zpassword" < $zilean_cache
  $mysql -u $zuser "-p$zpassword" < $zilean_sys
}

function clear_zilean_mysql_dependencies () {
  $mysql -u $zuser "-p$zpassword" < $zilean_clear
}

function zilean_mysql_maker () {
  option=$1
  mode=$2
  if [ "$option" = "make" ]; then
    make_zilean_mysql_dependencies
  elif [ "$option" = "remake" ]; then
    clear_zilean_mysql_dependencies
    make_zilean_mysql_dependencies
  elif [ "$option" = "clear-only" ] || [ "$option" = "clear" ]; then
    clear_zilean_mysql_dependencies
  fi
}

$@
