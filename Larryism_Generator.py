import random
from Resources.Functions import *
from Resources.Classes import *

def main():
    openers = readFile("Openers")
    adjs = readFile("Adjectives")
    foods = readFile("Foods")
    connectors = readFile("Connectors")

    Larryism = Phrase(random.choice(openers), random.choice(adjs), random.choice(foods), random.choice(connectors))
    
    print(f"{Larryism.opener} {Larryism.era}! I hope you are having a {Larryism.adj} {Larryism.food} {Larryism.connector} {Larryism.day}!\n")
    print(f"I hope you're having a {Larryism.adj} {Larryism.connector} {Larryism.day} {Larryism.era}!\n")
    print(f"I hope you're having a 'Hot-Load' {Larryism.connector} {Larryism.day} {Larryism.era}!\n")

if __name__ == "__main__":
    main()