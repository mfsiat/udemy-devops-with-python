FROM python

COPY . /app

WORKDIR /app

COPY req.txt .

EXPOSE 5000

RUN pip install -r req.txt

CMD ["python", "app.py"]