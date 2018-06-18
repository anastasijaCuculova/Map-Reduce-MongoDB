from bson.code import Code
from myCode import get_db

map = Code("function () {"
           "  this.sentence.forEach(function(z) {"
           "    emit(z, 1);"
           "  });"
           "}")
reduce = Code("function (key, values) {"
              "  var total = 0;"
              "  for (var i = 0; i < values.length; i++) {"
              "    total += values[i];"
              "  }"
              "  return total;"
              "}")

result = get_db().sentences.map_reduce(map, reduce, "myresults")

for doc in result.find():
    print(doc)
