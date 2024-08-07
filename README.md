# simple-fastapi
Simple Example of API using fastapi

## How to use

* Install requirements by `pip install -r requirements.txt`
* Delete `NewUserDB.db` and run `make create-db`
* open terminal / cmd and run `make run-api`
* open another terminal to interact with the api.
  * You can use `make post-one-sample` for one example
  * or use `curl` : `curl -X POST http://127.0.0.1:8085/users/ -H "Content-Type: application/json" -d @[json-file]`