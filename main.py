# # №1
#date = '2025-12-31'
#new_date = tuple(date.split('-')[::-1])
#print(new_date)

# # №2
# list = ['1', '2', '3', '4', '5']
# sum_of_elements = sum(int(x) for x in list)
# print(sum_of_elements)

# # №3
# list = [1, 2, 3, 4, 5, 6]
# mid = len(list) // 2
# first_half_sum = sum(list[:mid])
# second_half_sum = sum(list[mid:])

# result = first_half_sum / second_half_sum
# print(result)

# # №6
# def find_divisors(number):
# result = []
# for num in number:
# divisors = []
# for i in range(1, num+1):
# if num % i == 0:
# divisors.append(i)
# result.append(divisors)
# return result

# # №4
# dct1 = {
# 'a': 1,
# 'b': 2,
# }
# dct2 = {
# 'c': 3,
# 'd': 4,
# }

# # №5
# def find_min_max(numbers):
# result = {}
# result['max'] = max(numbers)
# result['min'] = min(numbers)
# return result

# # №7
# def generate_random_num(N, start, end):
# result = []
# previous_num = None
# for _ in range(N):
# num = random.randint(start, end)
# while num == previous_num:
# num = random.randint(start, end)
# result.append(num)
# previous_num = num
# return result

# # №8
# def random_color():
# Список доступных цветов
# colors = ["чёрный", "синий", "зеленый", "желтый", "оранжевый", "фиолетовый", "красный",]
# random_index = random.randint(0, len(colors) - 1)
# return colors[random_index]

# random_color_result = random_color()
# print("Случайный цвет:", random_color_result)






