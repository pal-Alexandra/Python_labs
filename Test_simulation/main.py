# Write a class Vocabulary that can we used to construct for operations on a specific vocabulary.
# class can be instantiated with a string. ex: Vocab("Some input string")
# will generate in the background a vocabulary with the known words "some" , "input" and "string" and the known symbols : "S", "s", "o" ...
# a method statistics can be called to get the current counts for the known words and symbols
# a method update can be called with a string in order to update the current vocabulary and known symbols
# a method to_string can be called to retun a string with all the known words in the vocab concatenated with spaces
# a method compare can be called with another Vocabulary object as a parameter and the words and symbols that apper in both vocabularies will be printed

class Vocabulary:
    def __init__(self, string):
        self.letters = None
        self.string = string
        self.vocabulary = self.string.split(' ')
        self.vocabulary = set(self.vocabulary)
        self.generate_letters()

    def generate_letters(self):
        self.letters = set()
        for letter in self.string:
            self.letters.add(letter)

    def statistics(self):
        return len(self.vocabulary), len(self.letters)

    def update(self, string):
        new_words = string.split(' ')
        for new_word in new_words:
            self.vocabulary.add(new_word)
        for letter in string:
            self.letters.add(letter)

    def to_string(self):
        string = ''
        for word in self.vocabulary:
            string += word
            string += ' '
        return string

    def compare(self, other_vocab):
        mutual_words = set()
        for word in self.vocabulary:
            if word in other_vocab.vocabulary:
                mutual_words.add(word)

        mutual_letter = set()
        for letter in self.letters:
            if letter in other_vocab.letters:
                mutual_letter.add(letter)

        print("\tMutual words:")
        print(mutual_words)

        print("\tMutual letters:")
        print(mutual_letter)


# vocabulary_1 = Vocabulary("i'm vocabulary one")
# vocabulary_1.update("here is update of the vocabulary one")
# print(vocabulary_1.to_string())
# print(vocabulary_1.statistics())
#
#
# vocabulary_2 = Vocabulary("i'm vocabulary two")
# vocabulary_1.compare(vocabulary_2)


a = Vocabulary("ana are mere")
print(a.statistics())
b = Vocabulary("Ana nu mai are mere")
print(b.statistics())
a.compare(b)
a.update(b.to_string())
print(a.statistics())