from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from random import randint
from models import mistral_model
from heapq import heappush,heappop



class FlashcardDeck:
    def __init__(self,path="books/"):
        self.cards = {} # cards with question, answer and context
        self.path = path # path to pdfs 
        self.chunks = [] # chunks of pdf
        self.cardheap = [] # priority queue of flashcards weighted by user score

    def load_and_split(self):
        """
        loads pdfs in a folder and splits them into chunks
        """

        print("Loading pdf...")

        loader = PyPDFDirectoryLoader(self.path)
        pdfs = loader.load()

        print(f"Loaded {len(pdfs)} documents")

        print("Splitting pdf...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 850
        )
        chunks = text_splitter.split_documents(pdfs)
        self.chunks = chunks
    
    def generate_flashcards(self,model=mistral_model,amount=1):
        for i in range(amount):

            index = self.get_new_index() 
            result = model(self.chunks[index].page_content)
            question, answer = result.split("#||#")
            flashcard = (
                question,  
                answer,  
                self.chunks[index].page_content, # context
                self.chunks[index].metadata.get("page","?") # page
            )
            self.cards[index] = flashcard
            heappush(self.cardheap,(-(100/3),flashcard)) # adds flashcard to queue

    def draw_flashcard(self):
        """
        returns next flashcard in queue 
        """
        if self.cardheap:
            return heappop(self.cardheap)

        else:
            "No flashcards :("
    
    def update_card_score(self,card,current_score,userrating):
        if userrating != 0:
            new_score = -(100/userrating)
            updated_score = (new_score*1.5+current_score*0.5)/2
            heappush(self.cardheap,(updated_score,card))

    
    def show_flashcards(self,card):
        print(f"Question: {card[0]}")
        input("Press enter to show answer")
        print(f"Answer: {card[1]}")
        ans = input("source? (y/n)")
        if ans == "y":
            print(f"Context: {card[2]}")
            print(f"Page: {card[3]}")
        print("-----------------------------")
        userrating = float(input(
                "rate yourself from (1-5) 1 is bad, 5 is good.\n " \
                "Enter 0 if you don't want to rate: "))
        return userrating


    def get_new_index(self):
        """
        finds new index that has not been used 
        """
        while True:
            random_index = randint(0,len(self.chunks)-1)
            if random_index not in self.cards: 
                return random_index

def main():
    # creates flashcard deck
    deck = FlashcardDeck()
    deck.load_and_split() # loads pdfs from path and splits them
    # it will keep generating new cards until all possible are generated
    while len(deck.cards) < len(deck.chunks):
        deck.generate_flashcards()
        score,card = deck.draw_flashcard()
        print(f"score : {score}")
        userrating = deck.show_flashcards(card)
        deck.update_card_score(card,score,userrating)
    while True: # just rating system
        score,card = deck.draw_flashcard()
        userrating = deck.show_flashcards(card)
        deck.update_card_score(card,score,userrating)
    

main()

    
    
    
    
    