#!/usr/bin/env make
PYTHON ?= python # python3 py

# Print out colored action message
MESSAGE = printf "\033[32;01m---> $(1)\033[0m\n"


# ---------------------------------------------------------
# Check the current python executable.
#
version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version


# ---------------------------------------------------------
# Setup a venv and install packages.
#
venv:
	test -d .venv || $(PYTHON) -m venv .venv
	@printf "Now activate the Python virtual envirounment.\n"
	@printf "\nOn Unix and Mac, do:\n"
	@printf ". venv/bin/activate && pip -V\n"
	@printf "\nOn Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate && pip -V\n"
	@printf "\nType 'deactivate' to deactivate.\n"


install:
ifeq ($(VIRTUAL_ENV), )
	@printf "\n\033[1m\t!!!You need to activate the Python virtual environment first!!!\033[1m \n\n"
else
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt
	@printf "\n Make sure to have 'Format on save' enabled in Visual Studio Code.\n"
	@printf "\033[1m https://code.visualstudio.com/docs/editor/codebasics#_format-on-save\033[0m\n\n"
	@printf "\n After that, make sure to have 'Black' selected as your preferred formatter.\n"
	@printf "\033[1m > Ctrl + Shift + P > Settings > Search 'Python Formatting Provider' \033[0m\n\n"
endif

installed:
	$(PYTHON) -m pip list


# ---------------------------------------------------------
# Work with codestyle.
#
black:
	@$(call MESSAGE,$@)
	 $(PYTHON) -m black src/ test/

codestyle: black


# ---------------------------------------------------------
# Work with static code linters.
#
pylint:
	@$(call MESSAGE,$@)
	-cd src && $(PYTHON) -m pylint *.py

flake8:
	@$(call MESSAGE,$@)
	-flake8

lint: flake8 pylint


# ---------------------------------------------------------
# Work with unit test and code coverage.
#
unittest:
	@$(call MESSAGE,$@)
	 $(PYTHON) -m unittest src/test/test_*.py

coverage:
	@$(call MESSAGE,$@)
	coverage run -m unittest src/test/test_*.py
	coverage html
	coverage report -m

test: lint coverage


# ---------------------------------------------------------
# Run the app
#
plans:
	python weekleh.py
