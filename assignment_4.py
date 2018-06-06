import numpy.random as random
class RockPaperScissors:
    """
    Implementation of the game Rock, Paper, Scissors
    """
    def __init__(self):
        scissors = {'rock': False, 'paper': True}
        rock = {'scissors': True, 'paper': False}
        paper = {'scissors': False, 'rock': True}
        self.choices = {'scissors': scissors, 'rock': rock, 'paper': paper}
        self.computerChoice = "Computer choice is pending."
        self.humanChoice= "Human choice is pending."
        self.results = [{'human':0,'computer':0}]
        self.gameIsOpen = True
        pass

    def computer_choice(self):
        """
        The computer chooses a value
        """
        self.computerChoice = random.choice(['rock', 'paper', 'scissors'])
        pass

    def human_choice(self):
        """
        The human player chooses a value
        """
        self.humanChoice = input("'rock', 'paper', or 'scissors'? ")
        pass

    def evaluate_game(self):
        """
        Evaluate the values of the two players
        """
        if self.humanChoice == self.computerChoice:
            self.results.append({'human':1,'computer':1})
        else:
            if self.choices[self.humanChoice][self.computerChoice]:
                self.results.append({'human':1,'computer':0})
            else:
                self.results.append({'human':0,'computer':1})
        pass

    def print_result(self):
        """
        Visualise game result
        """
        if self.humanChoice == self.computerChoice:
            print('Computer has {} as well!'.format(self.computerChoice))
            print('TIED GAME')
        else:
            if self.choices[self.humanChoice][self.computerChoice]:
                print('Computer has {}'.format(self.computerChoice))
                print('YOU WON')
            else:
                print('Computer has {}'.format(self.computerChoice))
                print('YOU LOST')

        pass

    def count_points(self):
        """
        Count the points of all rounds
        """
        numberOfGames = len(self.results)
        humanPoints = 0
        computerPoints = 0
        for i in range (1,numberOfGames):
            humanPoints = humanPoints + self.results[i]['human']
            computerPoints = computerPoints + self.results[i]['computer']
        print('Computer has {} points'.format(computerPoints))
        print('You have {} points'.format(humanPoints))
        pass

    def new_game_question(self):
        """
        Ask human player for new game
        """
        new_game = input("Another round? (y/n) ")
        if new_game in ['n', 'N', 'no', 'No', 'NO']:
            self.gameIsOpen = False
        pass


if __name__ == "__main__":
    game = RockPaperScissors()
    while game.gameIsOpen:
        game.computer_choice()
        game.human_choice()
        game.evaluate_game()
        game.print_result()
        game.count_points()
        game.new_game_question()
    print('Game closed.')