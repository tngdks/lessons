bb000 = {
    "x": 5, 
    "y": 5,
    "energy": 100
}

food = {
    "x": 8,
    "y": 5
}

print("Pehle BB-000 ki posotion:", bb000["x"])

for step in range(3):
    bb000["x"] += 1
    bb000["energy"] -= 2

print("Ab BB-000 ki nayi position:", bb000["x"])
print("Bachi hui energy:", bb000["energy"])

