import re
import json
from collections import Counter

class text_cleaner:
    def __init__(self, text):
        self.text = text
        self.textList = []
        self.min_wordsize = 2
        self.stop_words = []

        # load stop words
        with open('stop-words.json') as json_data:
            self.stop_words = json.load(json_data)

    def _cleanTextRegex(self, regex_statement, replacement):
        """
        This function removes the html-language from the article. Using a regex statement the function 
        clears all the text that is between '<' and '>'.
        """
        pattern = re.compile(regex_statement)
        self.text = re.sub(pattern, replacement, self.text)

    def _cleanSmallWords(self):
        """
        This function removes all words that are smaller than two characters.
        """
        new_list = []
        for word in self.text:
            if len(word) >= self.min_wordsize:
                new_list.append(word)
        
        self.text = new_list

    def _lowerWords(self):
        self.text =  [word.lower() for word in self.text]

    def _removeStopWords(self):
        temp_list = []

        for word in self.text:
            if word not in self.stop_words:
                temp_list.append(word)

        self.text = temp_list

    def clean_text(self):
        # Clear HTML tags
        self._cleanTextRegex('<.*?>', '')

        # Remove newlines
        self._cleanTextRegex('\n', ' ')

        # Remove urls
        self._cleanTextRegex(r'http\S+', '')

        # Remove everything that aren't letters.(aka leestekens)
        self._cleanTextRegex(r"[^a-zA-Z]+", ' ')

        # Convert the text into a list
        self.text = self.text.split()

        # Remove small words
        self._cleanSmallWords()

        # lower the words
        self._lowerWords()

        self._removeStopWords()

def getWords(text):
    clean = text_cleaner(text)
    clean.clean_text()
    counts = Counter(clean.text).most_common(5)

    return_list = []
    for words in counts:
        return_list.append(words[0])

    return {'words': return_list, 'parsed_source': clean.text, 'source': text}
