# 1. Робота із словниками
print("Завдання 1: Робота із словниками")
athlete = {
    "name": "Якийсь Спортсмен",
    "age": 38,
    "sport": "Легка атлетика",
    "team": "Збірна Ямайки"
}
print("Інформація про спортсмена:")
print(f"Name: {athlete['name']}")
print(f"Age: {athlete['age']}")
print(f"Sport: {athlete['sport']}")
print(f"Team: {athlete['team']}")
print()

# 2. Оновлення словника
print("Завдання 2: Оновлення словника")
books = {
    "Harry Potter": 1997,
    "1984": 1949,
    "Master and Margarita": 1967
}
print(f"Початковий словник книг: {books}")

# Додаємо нову книгу
books["Pride and Prejudice"] = 1813
print(f"Оновлений словник книг: {books}")
print()

# 3. Пошук значення
print("Завдання 3: Пошук значення")
countries = {
    "Ukraine": "Київ",
    "France": "Париж",
    "Japan": "Токіо",
    "Brazil": "Бразиліа"
}
print(f"Словник країн: {countries}")

country = input("Введіть назву країни: ")
if country in countries:
    print(f"Столиця {country}: {countries[country]}")
else:
    print(f"Вибачте, такої країни немає в словнику!")