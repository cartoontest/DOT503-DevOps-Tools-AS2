# Makefile

# Define the Python interpreter to use
PYTHON = python

# Compilation target
compile: application.py
	$(PYTHON) -m py_compile application.py

# Testing target
test: test_application.py
	$(PYTHON) -m unittest discover -s . -p 'test_*.py'

# Packaging target
package: application.py test_application.py
	zip -r myapp.zip application.py test_application.py

# Build target that depends on compile, test, and package
build: compile test package
