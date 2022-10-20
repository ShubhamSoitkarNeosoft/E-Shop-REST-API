FROM python:3.10

WORKDIR /app
COPY requirements.txt .
COPY .flaskenv .
RUN pip install -r requirements.txt   
COPY . .
EXPOSE 5000
CMD ["flask","run","--host=0.0.0.0"]

