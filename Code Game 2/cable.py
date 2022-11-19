r,g,b = str.split(input())
r = int(r)
g = int(g)
b = int(b)

total = r + g + b

time = 0
currentCar = 'red'

while (total > 0):
    if currentCar == 'red':
        if (r != 0):
            if (r >= 2):
                r -= 2
            else:
                r = 0
            if (time == 0):
                time += 30
            else:
                time += 1
        else:
            time += 1
        currentCar = 'green'
    elif currentCar == 'green':
        if (g != 0):
            if (g >= 2):
                g -= 2
            else:
                g = 0
            # time += 30
            if (time >= 30):
                time += 1
            else:
                time += 30
        else:
            time += 1
        currentCar = 'blue'
    else:
        if (b != 0):
            if (b >= 2):
                b -= 2
            else:
                b = 0
            # time += 30
            if (time >= 30):
                time += 1
            else:
                time += 30
        else:
            time += 1
        currentCar = 'red'
    total = r + g + b

print(time)