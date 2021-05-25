import click
@click.command()

def opener():
    click.echo('\nHello! Welcome to Rover\'s Ratings Page!\n')
    menu()

def menu():
    user_choice = input('Do you want to download CSV of user ratings? \n' +
                        'Y\n' + 'N\n'+ 'X (type \'X\' to exit)\n')
    checkUserInput(user_choice)

def checkUserInput(user_choice):
    our_choices = ['y','Y','n','N','X','x']

    while user_choice not in our_choices:
        click.echo('Invalid input, try again!\n')
        menu()

    if user_choice == 'X' or user_choice == 'x':
        click.Abort()

if __name__ == '__main__':
    opener()


