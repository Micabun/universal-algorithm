bagal = [230, 8, 46, 1]
pasta = [220, 8.07, 42.95, 1.29]
bread = [69, 1.99, 13.16, .86]
nutri = [114, 6.6, 20.8, 0.2]
chikn = [130, 26, 0, 3]
omilk = [120, 3, 16, 5]
crech = [100, 2, 1, 10]
gouch = [101, 7.07, 0.63, 7.78]
hashb = [143, 2.07, 18.43, 7.54]
salmn = [166, 24.52, 0, 6.72]
dresn = [60, 0.13, 1.41, 6.17]
eggss = [74, 6.29, 0.38, 4.97]
oatml = [145, 6.06, 25.37, 2.39]
qinoa = [229, 8.01, 42.17, 3.55]
pents = [160, 7, 5, 14]
pinto = [110, 7, 21, 0]

food = [bagal, pasta, bread, nutri, chikn, crech, gouch, salmn, dresn, eggss, oatml, qinoa, pents, pinto]
# food class, better getter

total = [0, 0, 0, 0]
comp = [1] * len(food)
modi = [0] * len(food)
pref = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
realcal = [0] * len(food)

i = 0
while i < len(food):
    realcal[i] = (food[i][1] * 4) + (food[i][2] * 4) + (food[i][3] * 9)
    food[i][0] = realcal[i]
    i = i + 1

i = 0
while i <= len(food) - 1:
    j = 3
    while j >= 0:
        food[i][j] = food[i][j] / food[i][0] * pref[i]
        j = j - 1
    i = i + 1

# print(food[0])

for x in range(0, (len(modi))):
    modi[x] = pref[x] * comp[x]

i = 0
while i < (len(total)):
    j = 0
    while j < (len(food)):
        total[i] = total[i] + food[j][i]
        j = j + 1
    i = i + 1

grams_proteins = 150
grams_carbs = 200
grams_fats = 66.7
calories = (grams_proteins * 4) + (grams_carbs * 4) + (grams_fats * 9)
goal = [calories, grams_proteins, grams_carbs, grams_fats]
# print(goal)

# -------- Calculates values using the caloric property (goal[0] and total[0]) as a base -------- #

ideal = [0, 0, 0, 0]
for x in range(0, len(goal)):
    ideal[x] = goal[x] / goal[0]
current = [0, 0, 0, 0]
for x in range(0, len(goal)):
    current[x] = total[x] / total[0]

# print(modi)
print(current)
print(ideal)

# ----- Adds 1 to comp when current and ideal meet specified conditions ----- #

while total[0] < goal[0]:
#the loop will run until total calories meet goal calories

    if current[1] > ideal[1] and current[2] > ideal[2] and current[3] < ideal[3]:
        for x in range(0, len(food)):
            if food[x][1] < food[x][3] and food[x][2] < food[x][3] or food[x][3] > ideal[3]:
                comp[x] = comp[x] + 1
                modi[x] = pref[x] * comp[x]
                for z in range(0, len(total)):
                    total[z] = total[z] + (pref[x] * food[x][z])
                    current[z] = total[z] / total[0]

    elif current[1] > ideal[1] and current[2] < ideal[2] and current[3] < ideal[3]:
        for x in range(0, len(food)):
            if food[x][1] < food[x][2] and food[x][1] < food[x][3] or food[x][1] < ideal[1]:
                comp[x] = comp[x] + 1
                modi[x] = pref[x] * comp[x]
                for z in range(0, len(total)):
                    total[z] = total[z] + (pref[x] * food[x][z])
                    current[z] = total[z] / total[0]

    elif current[1] > ideal[1] and current[2] < ideal[2] and current[3] > ideal[3]:
        for x in range(0, len(food)):
            if food[x][1] < food[x][2] and food[x][3] < food[x][2] or food[x][2] > ideal[2]:
                comp[x] = comp[x] + 1
                modi[x] = pref[x] * comp[x]
                for z in range(0, len(total)):
                    total[z] = total[z] + (pref[x] * food[x][z])
                    current[z] = total[z] / total[0]

    elif current[1] < ideal[1] and current[2] > ideal[2] and current[3] < ideal[3]:
        for x in range(0, len(food)):
            if food[x][1] > food[x][2] and food[x][3] > food[x][2] or food[x][2] < ideal[2]:
                comp[x] = comp[x] + 1
                modi[x] = pref[x] * comp[x]
                for z in range(0, len(total)):
                    total[z] = total[z] + (pref[x] * food[x][z])
                    current[z] = total[z] / total[0]

    elif current[1] < ideal[1] and current[2] > ideal[2] and current[3] > ideal[3]:
        for x in range(0, len(food)):
            if food[x][1] > food[x][2] and food[x][1] > food[x][3] or food[x][1] > ideal[1]:
                comp[x] = comp[x] + 1
                modi[x] = pref[x] * comp[x]
                for z in range(0, len(total)):
                    total[z] = total[z] + (pref[x] * food[x][z])
                    current[z] = total[z] / total[0]

    elif current[1] < ideal[1] and current[2] < ideal[2] and current[3] > ideal[3]:
        for x in range(0, len(food)):
            if food[x][3] < food[x][1] and food[x][3] < food[x][2] or food[x][3] < ideal[3]:
                comp[x] = comp[x] + 1
                modi[x] = pref[x] * comp[x]
                for z in range(0, len(total)):
                    total[z] = total[z] + (pref[x] * food[x][z])
                    current[z] = total[z] / total[0]

thing = 0
for x in range(0, len(modi)):
    thing = thing + modi[x]

print(total)
# print(ideal)
# print(current)
# print(modi)
print(thing)
print(goal)
print(modi)