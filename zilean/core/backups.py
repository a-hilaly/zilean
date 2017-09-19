from greww.utils import execute_shell_command

_script = "$ZILEAN_PATH/zilean/_sql.sh {0} {1}"

def mysqlcmd_readscript(script_path):
    execute_shell_command(_script.format("read", script_path))

def migrate_database_backup(database, script_path):
    a="{0} {1}"
    execute_shell_command(_script.format("read", a.format(script_path, database)))

def create_database_backup(database, target):
    a="{0} {1}"
    execute_shell_command(_script.format("dump", a.format(database, target)))
