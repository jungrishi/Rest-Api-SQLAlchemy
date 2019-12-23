clean:
	find . -type f -name '*.pyc' -delete
	# find . -type f -name ''

system-packages:
	sudo eopkg install python-pip -y

python-packages:
	pip install -r requirements.txt

run:
	python app.py

