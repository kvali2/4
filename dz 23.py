#Завдання 3: Маючи змінну price з числовим значенням, виведіть цю змінну у вигляді грошової суми з двома знаками після десяткової коми (наприклад, 123.45 грн).
price = float(input("напиши свою зп в $: "))
print(f"твоя зп составляє : {price:.2f} $")

# Завдання 4: Створіть список з трьох довільних слів. Виведіть цей список на екран в один рядок, розділяючи слова табуляцією.
print("\n\tНі долі, ні волі у мене нема,"
         "\nЗосталася тільки надія одна:"
         "\n\tНадія вернутись ще раз на Вкраїну,"
         "\nПоглянути ще раз на рідну країну,"
         "\n\tПоглянути ще раз на синій Дніпро, –"
         "\nТам жити чи вмерти, мені все одно;"
         "\n\tПоглянути ще раз на степ, могилки,"
         "\nВостаннє згадати палкії гадки…"
         "\n\tНі долі, ні волі у мене нема,"
         "\nЗосталася тільки надія одна.")

#Завдання 2: Напиши програму, що приймає числа від 1 до 10 та виводить їх на екран з використанням форматування f-string, додавши символ нового рядка \n після кожного числа.
for число in range(1, 11):
    print(f"{число}\n")