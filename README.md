<h1 align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="45" height="45" alt="Python" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="45" height="45" alt="Django" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" width="45" height="45" alt="SQLite" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="45" height="45" alt="Docker" />
  <br />
  e-diaristas API
</h1>

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.9-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.12-A30000?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

</div>

---

## 📝 Descrição

Back-end em **Django + Django REST Framework** da plataforma e-diaristas. Expõe a API que lista os profissionais de limpeza que atendem a uma determinada cidade, a partir de um CEP, e uma interface web para cadastro de diaristas.

Projeto desenvolvido durante o **Workshop Multi Stack da [TreinaWeb](https://www.treinaweb.com.br/)** — que constrói a mesma aplicação em diferentes stacks — e posteriormente **dockerizado** para rodar em qualquer máquina.

<cite>API que conecta clientes a diaristas disponíveis na sua localidade, a partir da busca por CEP.</cite>

---

## 🚦 Status do Projeto

<h4 align="center">
  ✅ e-diaristas API &nbsp;•&nbsp; 🚀 Concluído &nbsp;•&nbsp; ⚙️ Aberto a melhorias
</h4>

---

## 🏗️ Arquitetura do Projeto

> **Tipo:** 🔌 API + interface web de cadastro

```
┌──────────────────────────┐        HTTP        ┌────────────────────────┐
│  Front-end (outro repo)  │ ─────────────────▶ │  esta API (Django)     │
└──────────────────────────┘                    │  /api/diaristas-cidade │
                                                └───────────┬────────────┘
                                                            │ consulta o CEP
                                                            ▼
                                                    ┌───────────────┐
                                                    │  ViaCEP (API) │
                                                    └───────────────┘
```

A busca resolve o **código IBGE da cidade** pela ViaCEP e filtra as diaristas cadastradas por esse código.

---

## 🔥 Pré-requisitos

### 🐳 Via Docker (recomendado)

- **Docker** 20+ e **Docker Compose** v2+

### 💻 Local

- **Python** 3.9+

---

## 🚀 Tecnologias Utilizadas

| Categoria | Tecnologia |
| --- | --- |
| 🧠 **Linguagem** | Python 3.9 |
| 🎯 **Framework** | Django 3.2 |
| 🔌 **API** | Django REST Framework 3.12 |
| 🗄️ **Banco** | SQLite |
| 🖼️ **Imagens** | Pillow |
| 🎨 **Formulários** | django-crispy-forms + easy-mask |
| 🌐 **CORS** | django-cors-headers |
| 🐳 **Infra** | Docker + Docker Compose |

---

## 🔨 Funcionalidades

- 🔍 **Busca de diaristas por CEP**, resolvendo a cidade via API ViaCEP
- 🏙️ **Filtro por código IBGE**, retornando todos os profissionais da cidade
- 📄 **Paginação** dos resultados
- ⭐ **Reputação** gerada dinamicamente na serialização
- 📝 **Cadastro de diaristas** por interface web, com máscaras nos campos
- 🖼️ **Upload de fotos**, servidas em `/media/`
- 🔓 **CORS liberado**, permitindo o consumo por front-ends externos

---

## 💻 Comandos

### 🐳 Docker

```bash
docker compose up -d --build
```

API disponível em **http://localhost:8000**.

### 💻 Local

```bash
pip install -r requirements.txt
```

```bash
python manage.py runserver
```

> ⚠️ Guia completo em [docs/COMO_EXECUTAR.md](docs/COMO_EXECUTAR.md).

---

## 📊 Documentação da API

### `GET /api/diaristas-cidade?cep={cep}`

```bash
curl "http://localhost:8000/api/diaristas-cidade?cep=45055485"
```

```json
{
  "quantidade_diaristas": 0,
  "diaristas": [
    {
      "nome_completo": "Maria Fernanda",
      "foto_usuario": "http://localhost:8000/media/images.jpg",
      "cidade": "Santa Catarina",
      "reputacao": 3
    }
  ]
}
```

🚧 O projeto não possui Swagger ou collections do Postman. CEPs de teste validados estão em [docs/ACESSOS_TESTES.md](docs/ACESSOS_TESTES.md).

---

## 🧱 Estrutura do Projeto

```
├── api/                          # 🔌 API REST
│   ├── pagination/
│   ├── serializer/
│   ├── service/                  # 🧠 regra da busca por cidade
│   ├── urls.py
│   └── views.py
├── web/                          # 📝 cadastro de diaristas
│   ├── forms/
│   ├── services/                 # 🌐 integração com a ViaCEP
│   └── models.py
├── ediaristas_workshop/          # ⚙️ settings, urls e wsgi
├── media/                        # 🖼️ fotos enviadas
├── docs/                         # 📚 execução e dados de teste
├── db.sqlite3                    # 🗄️ banco com dados de exemplo
├── manage.py                     # 🎯 CLI do Django
├── Dockerfile                    # 🐳 imagem da API
├── docker-compose.yml            # 🐳 orquestração
└── requirements.txt              # 📦 dependências
```

---

## 📸 Preview do Projeto

🚧 Preview não disponível no projeto.

---

## 📝 Melhorias Futuras

- [ ] Atualizar Django 3.2 → 5.x e Python 3.9 → 3.12
- [ ] Servir a aplicação com Gunicorn + Nginx em vez do servidor de desenvolvimento
- [ ] Adicionar testes automatizados (`api/tests.py` está vazio)
- [ ] Mover `SECRET_KEY` e `DEBUG` definitivamente para variáveis de ambiente em produção
- [ ] Adicionar cache na consulta à ViaCEP
- [ ] Documentar a API com Swagger (drf-spectacular)

---

## 🖋️ Dicas

- 🐳 O `db.sqlite3` e a pasta `media/` são montados como volume — os dados sobrevivem a rebuilds da imagem.
- 🌐 A busca por CEP depende da **ViaCEP**, então o container precisa de acesso à internet.
- 🎲 O campo `reputacao` é aleatório a cada requisição, por isso muda entre chamadas.
- 🏙️ O filtro é por **cidade** (código IBGE) — qualquer CEP da mesma cidade retorna o mesmo resultado.

---

## 🎓 Créditos

Projeto desenvolvido a partir do **Workshop Multi Stack e-diaristas** da [TreinaWeb](https://www.treinaweb.com.br/), com a containerização implementada posteriormente.

---

<div align="center">

Feito com ❤️ por **Gabriel Martins** 🚀

</div>
