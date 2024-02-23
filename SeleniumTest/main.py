import requests

def make_request(method, url, json_data, headers):
    response = requests.request(method, url, json=json_data, headers=headers, timeout=1)
    print(response.status_code)
    data = response.json()
    print(data)

make_request('POST', 'https://api.pokemonbattle.me/v2/pokemons', {"name": "generate", "photo": "generate"}, {'trainer_token': '6e979386efe347be2da7e712c1c4c3aa', 'Content-Type': 'application/json'})
make_request('PUT', 'https://api.pokemonbattle.me/v2/pokemons', {"pokemon_id": "2202", "name": "TestNamedotpy", "photo": "generate"}, {'trainer_token': '6e979386efe347be2da7e712c1c4c3aa', 'Content-Type': 'application/json'})
make_request('POST', 'https://api.pokemonbattle.me/v2/trainers/add_pokeball', {"pokemon_id": "2203"}, {'trainer_token': '6e979386efe347be2da7e712c1c4c3aa', 'Content-Type': 'application/json'})