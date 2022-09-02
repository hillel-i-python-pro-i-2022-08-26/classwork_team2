import os

clear = lambda: os.system('cls')


def if_letter_is_correct(letters):
    while True:
        a = input("Введите букву:").strip().lower()
        if a not in letters:
            return a
        else:
            print("Буква уже есть!")


def game():
    while True:
        print("----------------\nНачало")
        names = [input(f"Введите имя игрока: "), input(f"Введите имя ведущего: ")]

        word = list(input("Введите слово: ").strip().lower())
        clear()
        our_word = []
        letters = []
        lives = 10

        for i in range(len(word)):
            our_word.append('_')
        while True:
            a = if_letter_is_correct(letters)
            if a not in word:
                lives -= 1
            else:
                for i in range(len(word)):
                    if word[i] == a:
                        our_word[i] = a
                letters.append(a)
            print("Конец хода.")
            print(f"Оставшиеся жизни: {lives}")
            print(*our_word)

            if "_" not in our_word:
                print("Victory!")
                print(f'Игрок {names[0]} победил!')
                break
            if lives == 0:
                print("Game over!")
                print(f'Игрок {names[1]} победил!')
                break


game()
