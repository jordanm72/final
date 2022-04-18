from itertools import permutations


class Word:
    """Class"""
    def __init__(self, word, dict, line):
        self.word = word
        self.dict = dict
        self.line = line

    def checkWord(self):
        if self.checkSpelled():
            return word
        ist = self.findAlternatives()
        return self.chooseAlternative(ist, self.line)

    def checkSpelled(self):
        if self.word in self.dict:
            return True
        return False

    def findAlternatives(self):
        s = self.word



    def chooseAlternative(self, ist, line):
        print("\n The incorrectly spelled word is and its line: " + self.word)
        print(self.line)
        print("Here is a list of possible intended words, along with an index showing how close they are to the"
              " original. Lower is closer to the original")
        print(ist)
        i = input("Enter the index corresponding to the word you want to replace the misspelled one.")
        return ist[i]

    def mixLetters(self):
        answer = []
        for l in permutations(self.word):
            answer.append("".join(l))
        words = []
        for ans in answer:
            if ans in self.dict:
                words.append(ans)
        return words

    def addDouble(self):
        answer = []
        w = self.word
        for i in range(len(w)):
            new = w[:i] + w[i] + w[i:]
            if new in self.dict:
                answer.append(new)
        return answer