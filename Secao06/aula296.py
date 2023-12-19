import random

nomes = ['Luiz', 'Maria', 'Helena', 'Joana']

# r_shuffle = random.shuffle(nomes)
# print(nomes)

# r_sample = random.sample(nomes, k=3)
# print(r_sample)

random.seed(0)

r_choices = random.choices(nomes, k=3)
print(r_choices)


r_choice = random.choice(nomes)
print(r_choice)

