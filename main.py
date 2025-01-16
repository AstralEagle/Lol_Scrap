from utils.lol_parser import get_all_perso_from_lol

if __name__ == "__main__":
    # Récupérer la liste des champions
    champions = get_all_perso_from_lol()

    # Vérifier si la liste des champions est vide ou non
    if champions:
        # Afficher chaque champion
        for champion in champions:
            print(f"Nom: {champion['name']}")
            print(f"Image: {champion['image']}")
            print(f"Abilities: {champion['abilities']}")
            print(f"Health: {champion['stats'].get('Health')}")
            print(f"Attack Damage: {champion['stats'].get('Attack Damage')}")
            print("-" * 40)
    else:
        print("Aucun champion trouvé.")
