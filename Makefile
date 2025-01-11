venv: venv/touchfile

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

test: venv
	. venv/bin/activate; pytest

run: venv
	. venv/bin/activate; python3 pirogue.py
clean:
	rm -rf venv
	find . -name "*.pyc" -delete