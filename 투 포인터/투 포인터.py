n = 5
m = 5
data = [1, 2, 3, 4, 5]

count = 0
interval_sum = 0
end = 0

for i in range(len(data)):
    while True:
        if data[i] + data[end] == m:
            count += 1
        for j in range(i, end+1):
            interval_sum += data[j]

        if interval_sum >= m:
            interval_sum = 0
            break
        else:
            interval_sum = 0
            end += 1

print(count)