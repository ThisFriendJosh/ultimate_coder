.PHONY: gui

gui:
	pip install -r requirements.txt && streamlit run ui/app.py
