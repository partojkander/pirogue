venv: venv-touch-file

venv-touch-file: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -r requirements.txt
	touch venv/touchfile

update-venv: venv
	 . venv/bin/activate; pip install -r requirements.txt

test: venv
	. venv/bin/activate; pytest

test-cov: venv
	. venv/bin/activate; coverage run -m pytest; coverage report

run: venv
	. venv/bin/activate; python3 main.py

clean:
	rm -rf venv
	find . -name "*.pyc" -delete