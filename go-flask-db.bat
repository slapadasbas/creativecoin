set SERVER_NAME=localhost:5000
set FLASK_APP=creativecoin/__init__.py
set FLASK_ENV=development
set SECRET_KEY=D9D7799EFE4327C64A6FF30FBDE865DFA5C45D4BC8265AD7E79205F13CDBA8BF
flask db stamp head
flask db migrate
flask db upgrade