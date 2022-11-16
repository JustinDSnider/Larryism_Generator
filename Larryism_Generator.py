import random
from Resources.ReadFile import *
from Resources.Classes import *

def main():
    openers = ReadFile("Openers")
    adjs = ReadFile("Adjectives")
    foods = ReadFile("Foods")
    connectors = ReadFile("Connectors")

    Larryism = Phrase(random.choice(openers), random.choice(adjs), random.choice(foods), random.choice(connectors))
    print(f"{Larryism.opener} {Larryism.era}! I hope you are having a {Larryism.adj} {Larryism.food} {Larryism.connector} {Larryism.day}!\n")

    

if __name__ == "__main__":
    main()