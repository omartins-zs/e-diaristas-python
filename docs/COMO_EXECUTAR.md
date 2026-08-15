# Como Executar — e-diaristas API (Django)

Escolha **um** guia conforme seu ambiente:

| Guia | Quando usar | Requisitos no PC |
| --- | --- | --- |
| **[Docker](#docker)** | Executar em qualquer máquina | Docker Desktop |
| **[Local](#local)** | Desenvolver com o venv | Python 3.9+ |

> API REST do workshop e-diaristas. Expõe a busca de diaristas por CEP consumida pelo front-end.

---

## Docker

```bash
cp .env.example .env
```

```bash
docker compose up -d --build
```

API:

http://localhost:8000/api/diaristas-cidade?cep=88060455

Para parar:

```bash
docker compose down
```

---

## Local

```bash
python -m venv venv
```

Windows:

```powershell
venv\Scripts\activate
```

Linux e Mac:

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
cd ediaristas_workshop
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

API:

http://127.0.0.1:8000/api/diaristas-cidade?cep=88060455

---

## Endpoints

| Método | Rota | Descrição |
| --- | --- | --- |
| GET | `/api/diaristas-cidade?cep={cep}` | Lista diaristas que atendem a cidade do CEP |
| — | `/web/` | Cadastro de diaristas (interface web) |
| — | `/admin/` | Admin do Django |
| — | `/media/{arquivo}` | Fotos enviadas |

---

## Variáveis de ambiente

| Variável | Padrão | Descrição |
| --- | --- | --- |
| `APP_PORT` | `8000` | Porta publicada no seu computador |
| `DJANGO_DEBUG` | `True` | Modo debug |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1,[::1]` | Hosts autorizados |
| `DJANGO_SECRET_KEY` | chave de desenvolvimento | Chave da aplicação |

---

## Observações

- O container usa o **servidor de desenvolvimento do Django**, pois é ele quem serve as fotos em `/media/` e o admin (o `urls.py` publica a media apenas com `DEBUG=True`). Para produção, seria necessário Gunicorn + Nginx servindo `static/` e `media/`.
- A busca por CEP consulta a **API pública ViaCEP**, portanto o container precisa de acesso à internet.
- O banco é **SQLite** e já vem com dados de exemplo. O arquivo `db.sqlite3` e a pasta `media/` são montados como volume, então os dados sobrevivem a rebuilds.
- Dados de teste e CEPs válidos: [ACESSOS_TESTES.md](ACESSOS_TESTES.md)
