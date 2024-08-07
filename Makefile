create-db:
	python app/db/create.py

run-api:
	uvicorn main:app --reload --app-dir app --port 8085

post-one-sample:
	curl -X POST http://127.0.0.1:8085/users/ -H "Content-Type: application/json" -d '[{"name": "John Doe", "email": "john@example.com"}]'

post-json-sample:
	curl -X POST http://127.0.0.1:8085/users/ -H "Content-Type: application/json" -d @sample/userlist.json

get-one-sample:
	curl -X GET "http://127.0.0.1:8085/user/8"