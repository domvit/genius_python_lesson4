# 1. Робота із списками
print("Завдання 1: Робота із списками")
numbers1 = [1, 5, 8]  # Початковий список
print(f"Початковий список: {numbers1}")

numbers1.append(10)  # Додаємо 10
numbers1.append(20)  # Додаємо 20
print(f"Після додавання 10 і 20: {numbers1}")

numbers1.remove(10)  # Видаляємо 10
print(f"Після видалення 10: {numbers1}")
print()

# 2. Знаходження суми
print("Завдання 2: Знаходження суми")
numbers2 = [3, 7, 12, 4]  # Список чисел
print(f"Список чисел: {numbers2}")

sum_numbers = sum(numbers2)  # Знаходимо суму
print(f"Сума всіх чисел: {sum_numbers}")
print()

# 3. Подвійні значення
print("Завдання 3: Подвійні значення")
numbers3 = [2, 4, 6, 8]  # Початковий список
print(f"Початковий список: {numbers3}")

doubled = [num * 2 for num in numbers3]  # Подвоюємо кожне число
print(f"Список із подвоєними значеннями: {doubled}")