#! /usr/bin/env bash

# -------------------------------------
# HEROKU RESTORE DB
# -------------------------------------
# -e, exit on error
# -u, unset variable is an error
# -o pipefail, fail pipe chain if error
set -u -o pipefail

# Commands
# =====================================

command_help() {
cat <<EOT

Heroku Restore DB

Import a dumpfile from heroku pg:backup:download

Requires:
    - A postgres user must exist
    - dropdb, createdb, pg_restore

Commands:
    import          Import dumpfile from Heroku pg:backup:download

Usage:
    import DUMPFILE

Options:
    -h, --help      Print this help message

EOT
}

# Import Heroku Dumpfile
#
# $1 DUMPFILE: The path to the Heroku dumpfile
command_import_dumpfile() {
    local dumpfile_path="${1}"
    local db_name="djangodb"

    echo "Attempting to import ${dumpfile_path} into ${db_name}..."

    dropdb "${db_name}"
    createdb "${db_name}"
    pg_restore -v --no-owner -d "${db_name}" "${dumpfile_path}"

    echo "Complete!!!"
}

# Argv Handling
# =====================================

# $#, number of args
if [[ $# == 0 || "$1" =~ (--help|-h) ]]; then
    command_help
    exit
fi

# Handle heroku_restore_db.sh import DUMPFILE
if [[ "$1" == "import" ]]; then
    command_import_dumpfile $2
    exit
fi

# Nothing matched, show help
command_help

unset command_help command_import_dumpfile
exit 0
