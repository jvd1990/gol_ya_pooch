import random

def gol_ya_pooch():
    name = input("What is your name: ")
    print(f"Be bazi Gol ya Pooch khosh amadid, {name}!")
    
    total_attempts = 0
    total_wins = 0

    while True:
        print("Computer yek dast ra entekhab mikonad...")
        print(f"Dast 1 ya 2? {name}, shoma bayad hads bezanid!")

        # Computer yek adad tasadofi az bein 1 ta 2 entekhab mikonad
        correct_hand = random.randint(1, 2)
        attempts = 0

        while True:
            try:
                user_guess = int(input("Dast shoma (1 ya 2): "))
                if user_guess not in [1, 2]:
                    # Agar karbar adad 1 ya 2 vared nakard
                    print("Lotfan faghat adad 1 ya 2 ra vared konid.")
                    continue
                attempts += 1

                if user_guess == correct_hand:
                    # Agar hads karbar dorost bashad
                    print(f"Tabrik! {name}, shoma dorost hads zadid. Gol dar dast {correct_hand} bood!")
                    print(f"Shoma pas az {attempts} talash barande shodid.")
                    total_attempts += attempts
                    total_wins += 1
                    break
                else:
                    # Agar hads karbar eshtebah bashad
                    print(f"Pooch! {name}, dobare talash konid.")
            except ValueError:
                # Agar karbar adad ghalat vared konad
                print("Lotfan yek adad motabar vared konid.")
        
        # Porsidan az karbar baraye edame
        continue_game = input("Aya mikhahid edame bedahid? (yes/no): ").strip().lower()
        if continue_game not in ["yes"]:
            # Namayesh natije koli va khateme bazi
            print(f"{name}, bazi tamam shod!")
            print(f"Natije koli: Shoma {total_wins} bazi bordid va dar kol {total_attempts} talash dashtid.")
            print("Mamnoon az bazi kardan!")
            break
# Ejraye bazi
gol_ya_pooch()