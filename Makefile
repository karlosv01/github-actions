lint:
	# Aquí pones tu linter (ej: flake8, pylint, ruff)
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

test:
	# Aquí pones tu suite de tests (ej: pytest, unittest)
	python -m unittest discover tests
