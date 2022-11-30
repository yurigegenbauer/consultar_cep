def consulta_cep(cep):
    import requests

    url = 'https://viacep.com.br/ws/%s/json/' % cep
    response = requests.get(url)
    response_json = response.json()
    return response_json