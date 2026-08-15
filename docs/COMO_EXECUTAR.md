# Como Executar — e-diaristas API (Django)

Escolha **um** guia conforme seu ambiente:

| Guia | Quando usar | Requisitos no PC |
| --- | --- | --- |
| **[COMO_EXECUTAR_DOCKER.md](COMO_EXECUTAR_DOCKER.md)** | Executar em qualquer máquina com containers | Docker Desktop |
| **[COMO_EXECUTAR_LOCAL.md](COMO_EXECUTAR_LOCAL.md)** | Desenvolver com venv e o servidor do Django | Python 3.9+ |
| [ACESSOS_TESTES.md](ACESSOS_TESTES.md) | CEPs de teste, URLs e fluxos | — |

> API REST do workshop e-diaristas. Não possui autenticação: os endpoints são públicos.

---

## Início rápido

### Local

Ative o bloco `LOCAL` no `.env` e execute:

```bash
cp .env.example .env
```

```bash
pip install -r requirements.txt
```

```bash
cd ediaristas_workshop && python manage.py migrate && python manage.py runserver
```

Aplicação:

http://127.0.0.1:8000

### Docker

Ative o bloco `DOCKER` no `.env` e execute:

```bash
cp .env.example .env
```

```bash
docker compose up -d --build
```

Aplicação:

http://localhost:8000

---

## Logins demo

O `/admin/` do Django **não possui usuários cadastrados** e a API é pública. Para criar um superusuário:

```bash
docker compose exec api python manage.py createsuperuser
```

CEPs de teste validados estão em [ACESSOS_TESTES.md](ACESSOS_TESTES.md).

---

## URLs principais

| Área | Local | Docker |
| --- | --- | --- |
| API — busca por CEP | http://127.0.0.1:8000/api/diaristas-cidade?cep=45055485 | http://localhost:8000/api/diaristas-cidade?cep=45055485 |
| Cadastro de diaristas | http://127.0.0.1:8000/web/ | http://localhost:8000/web/ |
| Admin do Django | http://127.0.0.1:8000/admin/ | http://localhost:8000/admin/ |
| Fotos enviadas | http://127.0.0.1:8000/media/ | http://localhost:8000/media/ |

---

## Outros documentos

- [COMO_EXECUTAR_LOCAL.md](COMO_EXECUTAR_LOCAL.md) — Execução com venv
- [COMO_EXECUTAR_DOCKER.md](COMO_EXECUTAR_DOCKER.md) — Execução com containers
- [ACESSOS_TESTES.md](ACESSOS_TESTES.md) — CEPs de teste e validação
