import json

class Model:
    def save(self, cl):
        attrs = list(filter(lambda x: not x.startswith('_'), dir(cl)))
        dictionary = {}

        for attr in attrs:
            dictionary[attr] = cl.__getattribute__(attr)

        with open('json_data.json', 'w') as outfile:
            json.dump(dictionary, outfile)

class Test:
    def __init__(self, title, subtitle):
        self.title = title
        self.subtitle = subtitle

test = Test('title', 'subtitle')
m = Model()
m.save(test)