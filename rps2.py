import random

def input_human_play(inputusr=input):
    play = inputusr('rock, paper, or scissors?')
    while not is_valid_play(play):
        play = inputusr('rock, paper, or scissors?')
    return play

def is_valid_play(play):
    return play in ['rock','paper','scissors']

def generate_computer_play():
    return random.choice(['rock','paper','scissors'])

def evaluate_game(human, computer):
    if human == computer:
        win = 'tie'
    elif human == 'rock' and computer == 'paper':
        win = 'computer'
    elif human == 'rock' and computer == 'scissors':
        win = 'human'

    elif human == 'paper' and computer == 'scissors':
        win = 'computer'
    elif human == 'paper' and computer == 'rock':
        win = 'human'

    elif human == 'scissors' and computer == 'paper':
        win = 'computer'
    elif human == 'scissors' and computer == 'rock':
        win = 'human'
    return win

def main(inputusr=input):
    human = input_human_play(inputusr)
    computer = generate_computer_play()

    print(computer)

    game = evaluate_game(human, computer)
    if game == 'tie':
        print('it is a tie')
    else:
        print(f'{game} won')


if __name__ == '__main__':
    main()
