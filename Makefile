VENV_PATH = ~/.venv/singapore-routes-streamlit

all: venv install run

venv:
	python3 -m venv $(VENV_PATH)

install: venv
	@source $(VENV_PATH)/bin/activate && \
	pip install --disable-pip-version-check -q -r requirements.txt

run:	
	source $(VENV_PATH)/bin/activate && \
	streamlit run streamlit_app.py

.PHONY: venv install run