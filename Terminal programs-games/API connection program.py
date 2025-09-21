# ---------------- API CONNECTION EXAMPLE ----------------
# Connect to: https://pokeapi.co/
# Purpose: Retrieve information about a Pokémon using its name.

import requests

# ---------------- FUNCTION ----------------
def get_pokemon_info(name):
    # Base URL of the API with the Pokémon name appended
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    # Send a GET request to the API
    response = requests.get(url)

    # HTTP response codes:
    # 200 = Success, 404 = Not found, 500 = Server error, etc.
    if response.status_code == 200:
        pokemon_data = response.json()     # Convert the response JSON → Python dictionary
        return pokemon_data
    else:
        print(f"Failed to retrieve data, code: {response.status_code}")


# ---------------- USAGE ----------------
pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

# Only proceed if valid data was returned
if pokemon_info:
    # Access JSON data by dictionary keys
    print(f"Name: {pokemon_info['name']}")
    print(f"Id: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")


# https://www.youtube.com/watch?v=JVQNywo4AbU&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=81