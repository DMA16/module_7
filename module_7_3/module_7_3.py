import string as st

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = [*file_names]


    def get_all_words(self):
        words_dict = {}

        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                words = []

                for string in file.readlines():


                    for word in string.translate(str.maketrans('', '', st.punctuation + '\n')).split(" "):
                        if word != '':
                            words.append(word.lower())

                words_dict.setdefault(
                    file.name,
                    words
                )

        return words_dict


    def find(self, word):
        words_dict = self.get_all_words()

        word = word.lower()

        dict_ = {}

        for name, words in words_dict.items():
            if word in words:
                dict_.setdefault(name, words.index(word) + 1)

        return dict_


    def count(self, word):
        words_dict = self.get_all_words()
        word = word.lower()
        dict_ = {}

        for name, words in words_dict.items():
            word_count = 0

            for i in range(len(words)):
                if word == words[i]:
                    word_count += 1

            dict_.setdefault(name, word_count)

        return dict_


finder1 = WordsFinder('test_file.txt')
finder2 = WordsFinder('test_file2.txt')

print(finder1.get_all_words())
print(finder1.find('Is'))
print(finder1.count('is'))

print(finder2.get_all_words())
print(finder2.find('if'))
print(finder2.count('if'))