import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
person = random.choice(friends)
print(f"methode1: {person}")

num = random.randint(0,4)
print(f"methode2: {friends[num]}")
