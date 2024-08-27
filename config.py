import os

# For a production app, you should use a secret key set in the environment
# The recommended way to generate a 64char secret key is to run:
# python -c 'import secrets; print(secrets.token_hex())'
SECRET_KEY = os.getenv('SECRET_KEY', 'not-set')

# When deploying, set in the environment to the PostgreSQL URL
#connection_string = 'postgresql://postgres:postgres@localhost:5432/exercises'
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://anand:xwDGjtTBf8d1LF62diyINDilAQmKR54t@dpg-cr733ji3esus73dn8gr0-a.oregon-postgres.render.com/test_n5z8')
