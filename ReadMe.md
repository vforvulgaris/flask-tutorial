Generic single-database configuration.

before runnig app:
export FLASK_APP=microblog.py


before testing email implementation:
You need two terminal windows.
1. This is going to be running your local mail server that emulates your emails being sent
$(venv) python -m smtpd -n -c DebuggingServer localhost:8025

2. Your main flask terminal window with the following required commands (FLASK_DEBUG=1 is optional but highly recommended for troubleshooting)

$ export FLASK_APP=microblog.py
$ export FLASK_DEBUG=1
$ export MAIL_SERVER=localhost
$ export MAIL_PORT=8025
$ flask run