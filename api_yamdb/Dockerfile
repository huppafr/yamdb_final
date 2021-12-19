FROM python:3.7-slim
WORKDIR /app
<<<<<<< HEAD
COPY requirements.txt ../.
RUN pip install -r ../requirements.txt --no-cache-dir
COPY ../. .
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ] 
=======
RUN pip install -r ../requirements.txt --no-cache-dir
COPY ../. .
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ] 
>>>>>>> 730e3e05a0197ad284285e34a4983b07f60e3700
