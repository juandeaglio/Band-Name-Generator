from IBandGenerator import IBandGenerator


class SimpleBandGenerator(IBandGenerator):
    def __init__(self):
        self.__questions = ["What's the name of the city you grew up in?", "What's your pet's name?"]

    def list_questions(self):
        return self.__questions
