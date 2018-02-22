# wybierz losowo jeden kolor
import random
from random import choice

colors = ["red", "blue", "green", "yellow"]

chosen_color = colors[random.randrange(len(colors))]

chosen_color1 = choice(colors)

print(chosen_color)
print(chosen_color1)
