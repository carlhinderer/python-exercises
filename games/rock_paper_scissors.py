import random

class RockPaperScissors:
    BEST_OF = 3
    PLAY_OPTIONS = ['Rock', 'Paper', 'Scissors']

    def __init__(self):
        self.player_points = 0
        self.computer_points = 0
        self.still_playing = True

    def play_game(self):
        print('Welcome to Rock Paper Scissors!!!\n')
        while self.still_playing:
            self.take_turn()
        print('Game over.')

    def take_turn(self):
        player_turn = self.get_player_turn()
        computer_turn = random.choice(self.PLAY_OPTIONS)
        print('I choose %s' % computer_turn)
        self.evaluate_turn(player_turn, computer_turn)
        self.evaluate_still_playing()

    def get_player_turn(self):
        while True:
            turn = input("Enter 'Rock', 'Paper', or 'Scissors': ")
            if turn in self.PLAY_OPTIONS:
                return turn
            else:
                print('Invalid choice. Try again.')

    def evaluate_turn(self, player_turn, computer_turn):
        winner = self.rps(player_turn, computer_turn)
        if winner == 'Tie':
            print('Tie. Go again.\n')
        elif winner == 'Player':
            print('You win that round.\n')
            self.player_points += 1
        elif winner == 'Computer':
            print('I win that round.\n')
            self.computer_points += 1

    def evaluate_still_playing(self):
        points_to_win = self.BEST_OF // 2 + 1
        if self.computer_points == points_to_win:
            self.still_playing = False
            print('I win.')
        if self.player_points == points_to_win:
            self.still_playing = False
            print('You win.')

    def rps(self, player_turn, computer_turn):
        if player_turn == computer_turn:
            return 'Tie'
        elif player_turn == 'Rock' and computer_turn == 'Paper':
            return 'Computer'
        elif player_turn == 'Rock' and computer_turn == 'Scissors':
            return 'Player'
        elif player_turn == 'Paper' and computer_turn == 'Rock':
            return 'Player'
        elif player_turn == 'Paper' and computer_turn == 'Scissors':
            return 'Computer'
        elif player_turn == 'Scissors' and computer_turn == 'Rock':
            return 'Computer'
        elif player_turn == 'Scissors' and computer_turn == 'Paper':
            return 'Player'


if __name__ == '__main__':
    game = RockPaperScissors()
    game.play_game()
