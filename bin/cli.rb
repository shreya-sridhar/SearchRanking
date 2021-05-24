require 'io/console'
require 'tty-prompt'
require 'pry'
# require 'colorize'
# require 'lolize'
require "tty-table"

class CLI

    attr_reader :prompt, :font
    attr_accessor :customer, :cart, :pid, :current_user

    def main_menu
        system 'clear'
        `say Welcome to The Cart`
        @font = TTY::Font.new
        @pastel = Pastel.new
        opener
        puts @pastel.cyan(@font.write("                                   Shopping        Cart !!"))

        opener
        prompt = TTY::Prompt.new
        choices = ['🔹Login'.green ,'🔹Signup'.yellow, '🔹Exit'.red] # '🔹Update Name Info', '🔹Delete Account'
        choice = prompt.select("\n please make a selection🔹\n", choices) # do not use multi_select it leaves an octogon symble 

        if choice == '🔹Login'.green
            attempts = 0
            login(attempts)
        elsif choice == '🔹Signup'.yellow
            signup
        elsif choice == '🔹Exit'.red
            exit
        end
    end
end





