This streamlit appplication allows for the prediction of a loan default score in real time.

The data is being pulled directly from a database and hence requires you to set up the access credentials.

1. You will need to create a file with the path "./.streamlit/secrets.toml

2. Within the secrets.toml file, copy the variables below and populate the credentials for a Postgres database.

### .streamlit/secrets.toml
[postgres]
host = "***"
port = "***"
dbname = "***"
user = "***"
password = "***"