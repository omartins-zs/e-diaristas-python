# Como Executar Localmente — e-diaristas API (Django)

Guia para rodar **sem Docker**, usando um ambiente virtual do Python.

> **Não quer instalar Python?** Use [COMO_EXECUTAR_DOCKER.md](COMO_EXECUTAR_DOCKER.md) — basta Docker Desktop, em qualquer Windows, Mac ou Linux.

---

## Requisitos

Não é necessário instalar o Django globalmente — ele entra no projeto com `pip install -r requirements.txt`.

| Ferramenta | Obrigatório? | Versão mínima |
| --- | --- | --- |
| **Python** | Sim | 3.9+ |
| **pip** | Sim | 21+ |

Este projeto **não utiliza** MySQL, PostgreSQL, Redis, filas ou Node.js. O banco é **SQLite**, já incluso no Python.

### Ambiente de referência (máquina de desenvolvimento)

Stack usada na elaboração deste projeto — **não é requisito fixo**, só referência do que já foi testado:

| Ferramenta | Versão |
| --- | --- |
| **Python** | **3.9.5** |
| Django (no projeto) | 3.2 |
| Django REST Framework | 3.12.4 |

Para conferir no seu computador:

```bash
python --version
```

```bash
pip --version
```

---

## 1) Preparar ambiente

### 1.1 Acessar o projeto

```bash
cd c:/Projetos/e-diaristas-python
```

### 1.2 Copiar variáveis de ambiente

```bash
cp .env.example .env
```

No PowerShell:

```powershell
Copy-Item .env.example .env
```

### 1.3 Criar e ativar o ambiente virtual

```bash
python -m venv venv
```

No PowerShell:

```powershell
venv\Scripts\activate
```

No Linux ou Mac:

```bash
source venv/bin/activate
```

> O `venv/` **não é versionado**. Cada máquina cria o seu a partir do `requirements.txt`.

---

## 2) Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 3) Banco de dados

O arquivo `db.sqlite3` já vem versionado **com dados de exemplo**. Para garantir que as migrations estão aplicadas:

```bash
python manage.py migrate
```

Para criar um usuário do admin (não existe nenhum):

```bash
python manage.py createsuperuser
```

---

## 4) Rodar aplicação

```bash
python manage.py runserver
```

Aplicação:

http://127.0.0.1:8000

Testando a API:

```bash
curl "http://127.0.0.1:8000/api/diaristas-cidade?cep=45055485"
```

---

## 5) Filas e workers

Este projeto **não possui filas, workers ou scheduler**. Toda a resposta é gerada na requisição.

---

## 6) Acessos

| Recurso | URL |
| --- | --- |
| API — busca por CEP | http://127.0.0.1:8000/api/diaristas-cidade?cep=45055485 |
| Cadastro de diaristas | http://127.0.0.1:8000/web/listar_diaristas |
| Admin do Django | http://127.0.0.1:8000/admin/ |

### Credenciais de teste

A API é pública e não exige autenticação. O admin não possui usuários — crie um com `createsuperuser`.

CEPs validados estão em [ACESSOS_TESTES.md](ACESSOS_TESTES.md).

---

## 7) Comandos úteis

```bash
python manage.py migrate
```

```bash
python manage.py showmigrations
```

```bash
python manage.py createsuperuser
```

```bash
python manage.py shell
```

---

## 8) Problemas comuns

### A busca sempre retorna erro de CEP

A consulta depende da **API pública ViaCEP**. Verifique sua conexão com a internet.

### Todos os CEPs retornam lista vazia

O filtro é por **código IBGE da cidade**. Use um dos CEPs validados em [ACESSOS_TESTES.md](ACESSOS_TESTES.md).

### As fotos das diaristas não aparecem

A media só é servida com `DJANGO_DEBUG=True` (comportamento do `static()` no `urls.py`).

### Tabelas não encontradas

```bash
python manage.py migrate
```

### Erro ao instalar o Pillow

Atualize as ferramentas de build:

```bash
pip install --upgrade pip setuptools wheel
```

---

## Próximo passo

Para ambiente containerizado, consulte [COMO_EXECUTAR_DOCKER.md](COMO_EXECUTAR_DOCKER.md).
