# import json
#
# test = [{"id" : 12345678,
#         "name": {"first":"Craig","last":"Lowman"},
#         "phone": "555-555-5555"}]
#
# test.append({"id" : 1111111,
#         "name": {"first":"Robert","last":"Low"},
#         "phone": "555-555-5351"})
# with open("testFile.json", "w") as w:
#     json.dump(test,w,indent = 4, sort_keys=True)
import csv
fileName = "theTest.csv"
fileName = fileName[:len(fileName) - 4]
print(fileName)
