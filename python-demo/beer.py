bottles_remaining = 99

while bottles_remaining > 0:
    print(f"{bottles_remaining} bottles of beer on the wall, {bottles_remaining} of beer")
    print("Take one down, pass it around")
    bottles_remaining = bottles_remaining - 1
    print(f"{bottles_remaining} bottles of beer on the wall")
