maxDays = int(input())
n = int(input())
numDays = str.split(input())
currentDay = 1
manualCount = 0
for i in range(n-1):
    currentDay = int(numDays[i])
    if (currentDay <= maxDays):
        diff = maxDays - currentDay
        manualCount += diff
    currentDay = 1
print(manualCount)
