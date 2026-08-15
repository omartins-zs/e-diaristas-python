import requests
from requests import Response


def buscar_cidade_cep(cep):
    response = requests.get(
        f"https://viacep.com.br/ws/{cep}/json/"
    )

    return response