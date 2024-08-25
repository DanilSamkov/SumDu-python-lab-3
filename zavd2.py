def chek_word(word):
    return word and ' ' not in word

def main():
    while True:
        word1 = input("Введіть перше слово: ").strip()
        if not chek_word(word1):
            print("Будь ласка, введіть одне слово без пробілів.")
            continue

        word2 = input("Введіть друге слово: ").strip()
        if not chek_word(word2):
            print("Будь ласка, введіть одне слово без пробілів.")
            continue

        if word1 == word2:
            print("Слова однакові.")
        else:
            print("Слова різні.")

        choice = input("Бажаєте повторити? (y/n): ").strip().lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()
