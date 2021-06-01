import click
import sys
sys.path.append(r"C:\Users\shrey\SearchRanking")
from controllers.sitter_controller import SitterController

@click.command()
def opener():
    click.echo('\nHello! Welcome to Rover\'s Ratings Page!\n')
    menu()

def menu():
    user_choice = input('Do you want to download CSV of user ratings? \n' +
                        'Y\n' + 'N\n' + 'X (type \'X\' to exit)\n')
    validateUserInput(user_choice)

def validateUserInput(user_choice):
    our_choices = ['y', 'Y', 'n', 'N', 'X', 'x']
    while user_choice not in our_choices:
        click.echo('Invalid input, try again!\n')
        menu()
    runUserAction(user_choice)

def runUserAction(user_choice):
    if user_choice == 'X' or user_choice == 'x':
        click.Abort()

    if user_choice == 'Y' or user_choice == 'y':
        print("hello")
        s = SitterController()
        s.overall_score_calculator()


if __name__ == '__main__':
    opener()
