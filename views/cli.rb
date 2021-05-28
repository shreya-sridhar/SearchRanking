require 'io/console'
require 'tty-prompt'
require 'pry'
require 'colorize'
require "tty-table"
require 'tty-font'

class CLI
    def main_menu
        system 'clear'
        @font = TTY::Font.new
        @pastel = Pastel.new
        # opener
        puts @pastel.cyan(@font.write("                                   ROVER CLI"))

        # opener
        prompt = TTY::Prompt.new
        choices = ['🔹DOWNLOAD SITTER RATINGS (IN CSV)'.green ,'🔹GET SITTER RATING BY NAME/EMAIL'.yellow, '🔹ADD SITTER RATING'.red]
        choice = prompt.select("\n please make a selection🔹\n", choices) 
        # do not use multi_select it leaves an octogon symble 
        # if choice == '🔹Login'.green
        #     attempts = 0
        #     login(attempts)
        # elsif choice == '🔹Signup'.yellow
        #     signup
        # elsif choice == '🔹Exit'.red
        #     exit
        # end
    end
end

cli = CLI.new()
cli.main_menu()




