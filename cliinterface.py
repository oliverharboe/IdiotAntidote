import questionary


class CLIInterface:
    def __init__(self):
        pass

    def user_rating(self):
        # user inputs their own rating on how well they did from (1-5)
        print("rate yourself from (1-5) 1 is bad, 5 is good.")
        choice = questionary.select(
            "rate yourself from (1-5) 1 is bad, 5 is good.\n" \
            "Enter 0 if would like to remove the card: ",
            choices=["1","2","3","4","5","0"]
            ).ask()
        return int(choice)
    
    def get_source(self):
        # returns True if y or False if n
        return questionary.confirm("Would you like to see the Source?").ask()

    def show_flashcards(self,card):
        print(f"Question: {card[0]}")
        input("Press enter to show answer")
        print(f"Answer: {card[1]}")
        


if __name__ == "__main__":
    interface = CLIInterface()
    interface.user_rating()
    print(interface.get_source())
