from word import Word


class Line:

    def __init__(self, line, dict):
        self.line = line
        self.dict = dict

    def checkLine(self):
        for word in self.line:
            w = Word(word, self.dict, self.line)
            word = w.checkWord()
        return self.line
