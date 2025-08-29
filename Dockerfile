FROM python:3.13-slim-bullseye
WORKDIR /vectramind.py /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Make port 10000 available to the world outside this container
EXPOSE 10000
COPY . .
CMD ["python", "vectramind.py"]