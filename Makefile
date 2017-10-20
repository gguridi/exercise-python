init:
	pip install -r requirements.txt
	npm install --prefix tests_api

.PHONY: init test
