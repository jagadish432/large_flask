!#/bin/bash

export LC_ALL=C.UTF-8 && export LANG=C.UTF-8
alias python=python3
touch db/$DATABASE_NAME
python migrate.py db upgrade
flask run --host 0.0.0.0 --port 5020