z = 0
count = 0
for x in range(3, 500, 3):
    if x % 2 == 1:
        z = z + x
        count = count + 1
print(f'A soma dos {count} valores recebidos é {z}')