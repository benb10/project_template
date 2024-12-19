python3 manage.py migrate
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4