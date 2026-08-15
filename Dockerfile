FROM python:3.9-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . ./

EXPOSE 8000

# Servidor de desenvolvimento do Django: e ele quem serve os arquivos de
# media (fotos das diaristas) e o admin, via `static()` no urls.py.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
