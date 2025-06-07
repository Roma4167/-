import random

def play_game():
    choices = ['камень', 'ножницы', 'бумага']
    computer_choice = random.choice(choices)
    
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    print("Выберите один из вариантов:")
    print("1 - Камень")
    print("2 - Ножницы")
    print("3 - Бумага")
    
    while True:
        try:
            user_input = int(input("Ваш выбор (1-3): "))
            if 1 <= user_input <= 3:
                user_choice = choices[user_input - 1]
                break
            else:
                print("Пожалуйста, введите число от 1 до 3.")
        except ValueError:
            print("Пожалуйста, введите число от 1 до 3.")
    
    print(f"\nВы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}\n")
    
    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        print("Вы победили!")
    else:
        print("Компьютер победил!")

    play_again = input("\nХотите сыграть ещё раз? (да/нет): ").lower()
    if play_again == 'да':
        print()
        play_game()
    else:
        print("Спасибо за игру!")

play_game()