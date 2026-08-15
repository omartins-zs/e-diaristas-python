# Como Executar com Docker — e-diaristas API (Django)

Guia para executar a API utilizando Docker Desktop.

---

## Stack e containers

| Container | Função | Porta |
| --- | --- | --- |
| api | Django com o servidor de desenvolvimento | 8000 |

> O banco é **SQLite** (arquivo no próprio projeto), portanto não há container de banco de dados, cache, filas ou administração.

O container usa o **servidor de desenvolvimento do Django** porque é ele quem serve as fotos em `/media/` e os arquivos do admin — o `urls.py` publica a media apenas quando `DEBUG=True`.

---

## 1) Preparar ambiente

```bash
cp .env.example .env
```

O `.env` controla a porta e as configurações do Django:

```env
APP_PORT=8000

DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1]
```

> `APP_PORT` é a porta publicada no seu computador. Internamente o container sempre escuta na `8000`.
>
> O front-end espera a API em `http://127.0.0.1:8000` por padrão — mantenha `APP_PORT=8000` para o consumo funcionar sem ajustes.

---

## 2) Subir containers

```bash
docker compose up -d --build
```

```bash
docker compose ps
```

---

## 3) Inicialização e migrations

O banco já vem versionado e populado. Para aplicar migrations pendentes:

```bash
docker compose exec api python manage.py migrate
```

Para criar um usuário do admin:

```bash
docker compose exec api python manage.py createsuperuser
```

---

## 4) Acessos

| Recurso | URL |
| --- | --- |
| API — busca por CEP | http://localhost:8000/api/diaristas-cidade?cep=45055485 |
| Cadastro de diaristas | http://localhost:8000/web/ |
| Admin do Django | http://localhost:8000/admin/ |
| Fotos enviadas | http://localhost:8000/media/images.jpg |

### Credenciais de teste

A API é pública e não exige autenticação. O admin não possui usuários cadastrados.

CEPs validados estão em [ACESSOS_TESTES.md](ACESSOS_TESTES.md).

---

## 5) Logs e diagnóstico

```bash
docker compose logs -f
```

```bash
docker compose logs -f api
```

```bash
curl -s "http://localhost:8000/api/diaristas-cidade?cep=45055485"
```

---

## 6) Persistência dos dados

O banco SQLite e a pasta de fotos são montados como volume:

```yaml
volumes:
  - ./ediaristas_workshop/db.sqlite3:/app/db.sqlite3
  - ./ediaristas_workshop/media:/app/media
```

Ou seja, **as diaristas cadastradas e as fotos enviadas sobrevivem a rebuilds** da imagem.

---

## 7) Parar ou reconstruir

```bash
docker compose down
```

```bash
docker compose up -d --build
```

Para remover também a imagem gerada:

```bash
docker compose down --rmi local
```

---

## 8) Problemas comuns

### Porta 8000 já está em uso

Altere `APP_PORT` no `.env` e suba novamente. Lembre de ajustar a URL da API no front-end.

### Erro de CEP em todas as consultas

O container precisa de **acesso à internet** para consultar a ViaCEP.

### As fotos não carregam

Confirme que `DJANGO_DEBUG=True` no `.env` — a media só é servida nesse modo.

---

## Próximo passo

Para desenvolvimento com venv, consulte [COMO_EXECUTAR_LOCAL.md](COMO_EXECUTAR_LOCAL.md).
