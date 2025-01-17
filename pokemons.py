import random
global pokemon_level
global pokemon_name
pokemon_level = 0
pokemon_name = "squirtle"
day = 1
def greet():
    print ("Hello, Users, Your Choosen Pokemon is Squirtle!")  
greet()
def draw_pokemon():
    """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠞⠛⠛⠉⠉⠛⠛⠳⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠃⠀⠀⣠⡖⢠⠀⠀⠀⠀⠀⠀⠀⠀⣧⣼⣷⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡟⠀⠀⢠⢿⣷⣶⡇⠀⠀⠀⠀⠀⠀⠀⡿⣿⡿⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣇⠀⠀⢸⠸⠻⡿⠇⠀⠀⠀⠀⠀⠀⠀⠐⠒⠈⢀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣄⡀⣿⠀⠀⠀⠁⠀⠉⠁⢀⣀⣀⣀⣄⣤⠴⢶⣶⣿⡏⠀⣸⣃⣀⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⣾⠉⠛⠛⠦⠤⣄⡀⢿⡋⠉⠉⠁⠀⠀⠉⠁⠀⠀⢈⡟⢀⡼⠛⠉⠉⠉⠉⠉⠛⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠉⠛⢷⣦⣀⠀⣀⣠⠤⠖⠒⠒⢛⣛⣻⣷⡖⣀⡀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡋⢉⣠⠴⠖⠚⠉⠉⠁⠉⠻⣍⣹⣶⣦⣀⡀⠀⠀⣸⣷⠶⠶⠶⠶⢦⣤⣴⣦⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠙⠳⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⣀⠀⠀⠀⠀⣀⣠⠤⠖⠛⠙⢿⣄⠈⠉⠙⠻⢿⣇⠀⠀⠀⠀⢠⠟⠀⠘⠛⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠛⢦⣄⡀⠀⠀⠀⠀⣠⣏⡉⠉⠉⠉⢉⡿⠟⠒⠒⠤⣄⡀⠀⠉⢦⡀⠀⠀⠀⠉⢧⠀⠀⠀⠋⠀⠀⠀⠀⠀⠉⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⢷⣶⣿⣿⣭⣭⡉⠑⢦⣴⠃⠀⠀⠀⠀⠀⠀⣙⣦⣠⣄⡹⢦⣀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣁⣀⣠⣤⣄⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣆⠘⡇⠀⠀⠀⠀⣶⠶⠞⠉⠛⠋⠘⣇⠀⠈⠳⢦⡀⠘⡆⠀⠀⠀⠀⠀⠀⠀⣰⠟⠋⠁⠀⠀⠀⠉⠙⠳⣤⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⡄⣧⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠙⠳⡿⣶⣶⣤⣀⣀⣠⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣷⡘⢧⡀⠀⠀⢿⠀⠀⠀⠀⠀⠀⣼⠀⢀⣠⣤⣄⡼⠁⣼⠀⠀⠉⠉⣽⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣷⣤⡉⠓⠦⠼⣧⡀⠀⠀⠀⣰⡇⢠⠋⠀⠀⠀⠙⠶⣯⣀⠀⠀⠀⣿⠀⠀⠀⠀⡴⠚⠛⠳⣆⠀⠀⠀⠀⠸⣇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣶⣶⣦⣽⣶⣶⣾⣉⣉⠙⣄⠀⠀⠀⠀⠀⠈⠙⠛⠛⠛⠻⡆⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⠀⠀⠀⠀⠀⢀⡾⠀⠀⠀⠀⢰⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⠿⠿⠛⠛⠉⠁⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⠶⢤⡤⠴⠛⠁⠀⠀⠀⢠⡿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠶⣦⣤⣤⣀⣀⣀⣀⣠⣤⡴⠾⠋⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀"""
draw_pokemon()

def train():
    pokemon_level = pokemon_level + 1
    print("Your current level is:{pokemon_level}")
    number = random.randint(0,10)
    print("Generated number:{number}")
    if number % 2 == 0:
        pokemon_level += 1
        print("level up!")
    else:
        pokemon_level -= 1
        print("level down!")

def gym_battle():
    print("Welcome to the Gym Battle! I Hope Your Ready to Fight!")
    input("Click enter to generate the number")
    random_number = random.randint(1,2)
    if random_number ==1:
        pokemon_level -=2
        print("You lost!")
    if random_number ==2:
        pokemon_level +=4
        print("You win!")

def evolve():
    if pokemon_level > 16:
        pokemon_name = "Squirtle"
    if pokemon_level == 16:
        print("Your pokemon has evolved!")
        pokemon_name = "Wartortle"
    if pokemon_level >36:
        pokemon_name = "Wartortle"
    if pokemon_level == 36:
        print("Your pokemon has evolved!")
        pokemon_name = "Blastoise"
    if pokemon_level <=36:
        pokemon_name = "Blastoise"

def rest():
    print("Your current pokemon is:{pokemon_name}")
    print("Your current pokemon's level is: {pokemon_level}")
    draw_pokemon()

print("Welcome to Pokemon Evolution")
while True:
    print("Choose an activity for the Day:" + str(day))
    print("""1. Train
2. Gym Battle
3. Rest(Display InFo)
4. Quit""")
    activity = int(input("activity for the day:"))
    if activity == 1:
        train()
        evolve()
    elif activity == 2:
        gym_battle()
        evolve()
    elif activity == 3:
        rest()
    elif activity == 4:
        exit