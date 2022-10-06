customers = {
    'Katniss': {'username': 'gale4ever', 'password': 'hung3rg4m3s', 'name': 'Katniss Everdeen'},
    'Peeta': {'username': 'breadNstuff', 'password': 'i_love_katniss', 'name': 'Peeta Melark'},
    'Gale': {'username': 'hunter4life', 'password': 'k4tn1ss', 'name': 'Gale Hawthorne'},
    'Snow': {'username': 'imbetterthanU', 'password': 'whiteRose', 'name': 'President Snow'}
    'Effie': {'username': 'prettyInPink', 'password': 'thatWasMahogony', 'name': 'Effie Trinket'}
    'Hamitch': {'username': 'iLOVEMELONS', 'password': 'budweiser', 'name': 'Hamitch Abernathy'}
}

def get_by_username(username):
    return customers.get(username)