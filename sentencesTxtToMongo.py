def get_db():
    # For local use
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    # 'examples' here is the database name. It will be created if it does not exist.
    db = client.sentences
    return db

def toJson(element):
    return {'element': element}

def txtToMongo():
    counter = 0
    db = get_db()

    with open("D:\\FakultetMaterijali\\FINKI\\6\\12Semestar\\NestrukturiraniBaziNaPodatociIXML\\ProektnaZadaca\\sentences.txt", "r") as ins:
        for line in ins:
            counter += 1
            lineSplit = line.split(" ", 1)
            #number = int(lineSplit[0])%10
            #numStr = str(number)
            #print(number)
            sentence = lineSplit[1].split("\n")[0]
            #print(len(sentence))
            #result = toJson(number, sentence, len(sentence))
            result = toJson(sentence)
            db.sentences.insert(result)
            #if counter >= numberOfLines:
            #    break
    return counter

print(txtToMongo()) # prefrlanje na podatocite od sentences.txt vo mongo