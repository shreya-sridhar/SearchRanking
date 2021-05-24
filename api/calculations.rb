require 'set'
class Calculations
    
    private 

    def profile_score(name):
        count = 0
        existing_letters = Set.new()
        for letter in name do
            if letter not in existing_letters do
                existing_letters.add(letter)
                count += 1
            end 
        end
    end

    def ratings_score(email): 
        sitter_rows = db.find_all { |row| row.sitter_email == email}
    end

    def search_score(email):

    end

end




