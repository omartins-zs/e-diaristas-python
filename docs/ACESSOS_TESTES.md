# 🔐 Acessos e Dados de Teste

> Esta é uma **API REST** sem autenticação. Os endpoints são públicos e não exigem token.
> O banco SQLite versionado já contém **9 diaristas** de exemplo — os CEPs abaixo foram testados contra a API em execução.

## 1. Acesso ao Sistema (Usuários de Teste)

| Perfil | E-mail / Usuário | Senha | Permissão / Detalhes |
| --- | --- | --- | --- |
| — | — | — | A API é pública, sem autenticação. |

O `/admin/` do Django **não possui nenhum usuário cadastrado**. Para criar um:

```bash
docker compose exec api python manage.py createsuperuser
```

Sem Docker:

```bash
python manage.py createsuperuser
```

## 2. CEPs de teste

Valores validados chamando `GET /api/diaristas-cidade?cep={cep}`:

| CEP | Cidade | Diaristas retornadas |
| --- | --- | --- |
| `45055485` | Vitória da Conquista (BA) | **4** |
| `88060455` | Florianópolis (SC) | 1 |
| `68909871` | Macapá (AP) | 1 |
| `59621630` | Mossoró (RN) | 1 |
| `88133592` | Palhoça (SC) | 1 |
| `01001000` | São Paulo (SP) | 0 (região sem cobertura) |

Exemplo de resposta:

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

> O campo `reputacao` é **gerado aleatoriamente** a cada requisição (`random.randint(0, 5)` no serializer), então muda a cada chamada.

## 3. URLs Principais

| Item | Link (Docker e Local) |
| --- | --- |
| API — busca por CEP | `http://localhost:8000/api/diaristas-cidade?cep=45055485` |
| Cadastro de diaristas | `http://localhost:8000/web/listar_diaristas` |
| Admin do Django | `http://localhost:8000/admin/` |
| Fotos enviadas | `http://localhost:8000/media/images.jpg` |

## 4. Validação do Acesso

| Verificação | Resultado Esperado |
| --- | --- |
| Container `e-diaristas-python-api` | `Up` na porta 8000 |
| `GET /api/diaristas-cidade?cep=45055485` | HTTP `200` com 4 diaristas |
| `GET /api/diaristas-cidade?cep=01001000` | HTTP `200` com lista vazia |
| CEP inválido (menos de 8 dígitos) | Erro de validação da ViaCEP |

```bash
docker compose ps
```

```bash
curl -s "http://localhost:8000/api/diaristas-cidade?cep=45055485"
```

## 5. Carregar Dados de Teste

O banco **já vem populado** no arquivo `db.sqlite3`, versionado no repositório e montado como volume.

Para aplicar as migrations em um banco novo:

```bash
docker compose exec api python manage.py migrate
```

Novas diaristas podem ser cadastradas pela interface web em `http://localhost:8000/web/listar_diaristas`.

---

### 📝 Observações:

- A busca por CEP depende da **API pública ViaCEP** (`https://viacep.com.br`). Sem internet, todas as consultas falham.
- O filtro é feito pelo **código IBGE da cidade**, não pelo CEP em si — por isso qualquer CEP da mesma cidade retorna as mesmas diaristas.
- Use estas instruções **apenas** em ambiente local ou Docker de desenvolvimento.
