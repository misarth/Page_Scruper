FROM python:3.9

ADD main.py .


RUN pip install requests beautifulsoup4 mysql-connector-python fastapi typing uvicorn

CMD ["uvicorn", "main:app", "--reload"]