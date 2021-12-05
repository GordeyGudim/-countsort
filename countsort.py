a = list(map(int, input().split()))
numbers = [0]*101
for now in a:
    numbers[now] += 1
for number in range(len(numbers)):
    for i in range(numbers[number]):
        print(number, end=' ')
