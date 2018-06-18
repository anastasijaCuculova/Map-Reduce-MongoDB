import os
import json

print(1)
datafile = "C://Users//Anastasija//Desktop//test.txt"

field_map = {
    "num_sentence": "num_sentence",
    "name": "name"
}

fields = field_map.keys()
print(fields)

def parse_file(dataFile):
    data = []
    with open(dataFile, "rb") as f:
        for line in f:
            print(line)


#parse_file(datafile)
