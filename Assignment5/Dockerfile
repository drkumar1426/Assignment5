FROM python
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8080
COPY . /app  
CMD ["python", "./app.py"]  