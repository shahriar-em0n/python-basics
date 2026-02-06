## Random & OS module
import random

# Psedorandom --> random but not purely random
# random
random_int = random.randint(1, 100)
print(f"Random number: {random_int}")

# Random list
choices = ["apple", "banana", "cherry"]
random_choice = random.choice(choices)
print(f"Random fruit: {random_choice}")


