def count_words(sentence):
    # Розбиваємо речення на слова
    words = sentence.split()

    # Фільтруємо слова, які закінчуються на "р"
    words_ending_with_p = [word for word in words if word.endswith('р')]

    return len(words_ending_with_p)

while True:
    sentence = input("Введіть речення: ")
    count = count_words(sentence)
    print(f"Кількість слів, що закінчуються на літеру 'р': {count}")

    repeat = input("Бажаєте повторити? (y/n): ").strip().lower()
    if repeat != 'y':
        break