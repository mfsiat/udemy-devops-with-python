FROM python
WORKDIR /app
COPY . /app
COPY req.txt .
RUN pip install -r req.txt
CMD ["python", "app"]