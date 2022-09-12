FROM python:3.9.6

WORKDIR /usr/src/app

#Copy requirements into the working directory
COPY requirements.txt ./

#Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

#to copy the whole app
COPY . .

CMD ["uvicorn" ,"src.main:app","--host","0.0.0.0","--port","8000"]
