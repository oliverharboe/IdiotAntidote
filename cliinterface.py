import questionary


class CLIInterface:
    def user_rating(self):
        # user inputs their own rating on how well they did from (1-5)
        print("rate yourself from (1-5) 1 is bad, 5 is good.")
        choice = questionary.select(
            "rate yourself from (1-5) 1 is bad, 5 is good.\n" \
            "Enter 0 if would like to remove the card: ",
            choices=["1","2","3","4","5","0"]
            ).ask()
        return int(choice)
    
    def get_source(self,card):
        # asks user if they would like to see the source
        ans = questionary.confirm("Would you like to see the Source?").ask()
        if ans == True:
            # prints text context and page number
            print("------------------------------------")
            print(f"Context: {card[2]}")
            print(f"Page: {card[3]}")
            print("------------------------------------")

    def show_flashcards(self,card):
        # shows question and answer to user
        print(f"Question: {card[0]}")
        input("|Press enter to show answer|")
        print(f"Answer: {card[1]}")
        

