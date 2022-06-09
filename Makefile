#!/usr/bin/env make

PYTHON ?= python # python3 py

version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version


# ---------------------------------------------------------
# Setup a venv and install packages.
#

venv:
	test -d .venv || $(PYTHON) -m venv .venv
	@printf "\nNow activate the Python virtual envirounment.\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf "\033[1m> . .venv/Scripts/activate && pip -V\033[0m\n"
	@printf "On Unix and Mac, do:\n"
	@printf "\033[1m> . venv/bin/activate && pip -V\033[0m\n"
	@printf "Type 'deactivate' to deactivate.\n\n"

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

unittest:
	@$(call MESSAGE,$@)
	 $(PYTHON) -m unittest src/test/test_*.py

coverage:
	@$(call MESSAGE,$@)
	coverage run -m unittest src/test/test_*.py
	coverage html
	coverage report -m


# run the app
plans:
	python weekleh.py
