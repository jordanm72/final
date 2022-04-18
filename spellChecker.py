from line import Line
from word import Word


class SpellChecker:
    """Spell checker class"""
    def __init__(self, name):
        ist = []
        self.name = name
        with open(self.name, encoding='utf8') as f:
            for line in f:
                ist.append(line)
        self.lines = ist
        words = {}
        with open('words_alpha.txt') as w:
            for line in w:
                words[line] = ""
        self.dict = words
        self.corrected = []

    def check(self):
        for line in self.lines:
            l = Line(line, self.dict)
            self.corrected.append(l.checkLine())
        with open('self.name', 'w') as f:
            for line in self.corrected:
                f.write(line + "\n")









