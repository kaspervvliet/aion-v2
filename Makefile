.PHONY: start test lint setup

start:
	@echo "Launching Streamlit Dashboard..."
	streamlit run src/tradetool/streamlit_dashboard.py

test:
	pytest src/tradetool/tests/

lint:
	flake8 src/tradetool/

setup:
	pip install -r requirements.txt
	cp .env.example .env || echo ".env already exists"