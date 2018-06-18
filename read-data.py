import json
import pprint
import io
import re


def get_db():
    # For local use
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    # 'examples' here is the database name. It will be created if it does not exist.
    db = client.sentences
    return db


def add_sentence(db):
    # Changes to this function will be reflected in the output.
    # All other functions are for local use only.
    # Try changing the name of the city to be inserted
    db.sentences.insert({"name": "Chicago"})


def get_sentence(db):
    return db.sentences.find_one()


def skip_lines(input_file, skip):
    for i in range(0, skip):
        next(input_file)


def json_list(list1, list2, list3):
    lst = []
    for number, sentence, num_word in zip(list1, list2, list3):
        d = {}
        d['number'] = number
        d['sentence'] = sentence
        d['number_words'] = num_word
        lst.append(d)
    return lst


sum_of_words = 0


def process_file():
    counter = 1
    sentences = []

    parts = []
    with open("sentences.txt", "r") as ins:
        num_sentence = []
        sentence = []
        number_words = []
        # rows = []
        for line in ins:
            parts = re.findall(r'\S+', line)
            print(len(parts))
            number_words.append(len(parts))
            global sum_of_words
            sum_of_words+= len(parts)
            number = float(line[:2])
            num_sentence.append(int(number))
            sentence.append(line[2:])
            counter += 1
            if counter > 2000000:
                break
    return json_list(num_sentence, sentence, number_words)


def insert_data(sentences, db):
    for row in sentences:
        db.sentences.insert(row)


#print(process_file())
#insert_data(process_file(), get_db())
# print(get_sentence(get_db()))
pp = pprint.PrettyPrinter()
pp.pprint(process_file())
print(sum_of_words)
# print(get_sentence(number))
# array.append(line)
