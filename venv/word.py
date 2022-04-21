from itertools import permutations


class Word:
    """Class"""
    def __init__(self, word, dict, line):
        self.word = word
        self.dict = dict
        self.line = line

    def __str__(self):
        return self.word

    def checkWord(self):
        ist = self.findAlternatives()
        ist = sorted(ist, key=lambda x: x[1])
        return self.chooseAlternative(ist, self.line)

    def checkSpelled(self):
        if self.word in self.dict:
            return True
        return False

    def findAlternatives(self):
        answer = []
        checkreplicates = []
        for ans in self.removeDouble():
            if ans[0] not in checkreplicates:
                answer.append(ans)
                checkreplicates.append(ans[0])
        for ans in self.singleTranspostions():
            if ans[0] not in checkreplicates:
                answer.append(ans)
                checkreplicates.append(ans[0])
        for ans in self.mixLetters():
            if ans[0] not in checkreplicates:
                answer.append(ans)
                checkreplicates.append(ans[0])
        for ans in self.addDouble():
            if ans[0] not in checkreplicates:
                answer.append(ans)
                checkreplicates.append(ans[0])
        for ans in self.transpose():
            if ans[0] not in checkreplicates:
                answer.append(ans)
                checkreplicates.append(ans[0])
        return answer

    def chooseAlternative(self, ist, line):
        print("\n The incorrectly spelled word is: " + str(self.word) + "\nIt's line is: ")
        print(self.line)
        print("Here is a list of possible intended words, along with an index showing how close they are to the"
              " original. Lower is closer to the original")
        for i in range(len(ist)):
            print("Index = " + str(i) + str(ist[i]))
        i = str(input("Enter the index of the word you want to replace the misspelled one."))
        return ist[i]

    def singleTranspostions(self):
        answer = []
        w = self.word
        for i in range(len(w) - 1):
            new = w[:i] + (w[i + 1] + (w[i] + (w[i + 2:])))
            if new in self.dict:
                answer.append((new, 2))
        return answer

    def mixLetters(self):
        answer = []
        for l in permutations(self.word):
            answer.append("".join(l))
        words = []
        for ans in answer:
            if ans in self.dict:
                words.append((ans, 5))
        return words

    def addDouble(self):
        answer = []
        w = self.word
        for i in range(len(w)):
            new = w[:i] + w[i] + w[i:]
            if new in self.dict:
                answer.append((new, 3))
        return answer

    def removeDouble(self):
        answer = []
        w = self.word
        for i in range(0, len(w) - 1):
            if w[i + 1] == w[i]:
                new = w
                new = new[:i] + new[i + 1:]
                if new in self.dict:
                    answer.append((new, 1))
        return answer

    def transpose(self):
        answer = []
        w = self.word
        letters = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(w)):
            for j in range(25):
                new = w[:i] + letters[j] + w[(i + 1):]
                if new in self.dict:
                    answer.append((new, 7))
        return answer
