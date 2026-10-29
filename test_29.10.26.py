def analyze_numbers(numbers):                           # Задание 1
    post_count = 0
    negative_sum = 0

    for x in numbers:
        if x > 0:
            post_count += 1
        elif x < 0:
            negative_sum += x

    return post_count, negative_sum

def get_even(numbers):                                # Задание 2
    even_numbers = []
    for x in numbers:
        if x % 2 == 0:
            even_numbers.append(x)
    return even_numbers


def swap_min_max(numbers):                           # Задание 3
    if len(numbers) == 0:
        return numbers


    num_min = 0
    num_max = 0

    for i in range(1, len(numbers)):
        if numbers[i] < numbers[num_min]:
            num_min = i
        if numbers[i] > numbers[num_max]:
            num_max = i


    numbers[num_min], numbers[num_max] = numbers[num_max], numbers[num_min]

    return numbers

def rotate_left(items, k):                  # Задание 4
    if not items:
        return []

    k = k % len(items)

    return items[:k] + items[k+1:]


numbers1 = [4, -2, 0, 7, -5]
res1 = analyze_numbers(numbers1)
print("1.", res1)                         # print к 1-му заданию


numbers2 = [5, 2, 8, 3, 10]
res2 = get_even(numbers2)
print("2.", res2)                        # print к 2-му заданию


numbers3 = [6, 1, 9, 4]
res3 = swap_min_max(numbers3)
print("3." , res3)                   # print к 3-ему заданию

items4 = [1, 2, 3, 4, 5]
k4 = 2
res4 = rotate_left(items4, k4)
print("4.", res4)                   # print к 4-му заданиюю