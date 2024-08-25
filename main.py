while True:
    text = input("Введіть рядок: ")

    # Перевірка довжини рядка
    if len(text) < 5:
        print("Помилка: рядок занадто короткий! Повинно бути щонайменше 5 символів.")
    else:

        last_five = text[-5:]
        print("Останні 5 символів:", last_five)

    choice = input("Бажаєте повторити? (y/n): ").strip().lower()

    if choice != "y":
        break