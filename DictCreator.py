import codecs
import re
from tqdm import tqdm


class DictCreator:
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name

    def create(self):
        """
        creates dictionary from the given text
        :return: list of correct words
        """
        try:
            with open(self._file_name) as f:
                text = codecs.decode(codecs.encode(f.read(), 'cp1251'), 'utf8')
        except TypeError:
            print('please, choose language or file for creating '
                  'your own dictionary')
            exit(1)
        dictionary = set()
        pattern = re.compile(r'([a-zA-Zа-яА-Я]+)\W*')
        list_of_words = pattern.findall(text.lower())
        count = len(list_of_words)
        loop = tqdm(total=count, position=0, leave=False)
        for k in range(count):
            loop.set_description('loading...'.format(k))
            dictionary.add(list_of_words[k])
            loop.update(1)
        loop.close()

        return dictionary
