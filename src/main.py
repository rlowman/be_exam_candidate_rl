# Main module for csv file reading application
# Author: Robert Lowman
# Date: 9/9/18
import time
import os
import sys
import csv
import json

def main():
    valid = True
    if len(sys.argv) != 3:
        print("Invalid number of arguments.")
        valid = False
    else:
        for arg in sys.argv[1:]
        if not os.path.isdir(arg):
            valid = False
            print(outputDir + " is not a valid directory.")

    if valid:
        inputDir = sys.argv[1]
        outputDir = sys.argv[2]

        while(true):
            files = os.listdir(inputDir)
            if len(files) > 0:
                csvFiles = []
                for temp in files:
                    if temp.endswith(".csv"):
                        processFile(str(inputDir + "/" + temp), errorDir, outputDir)


def processFile(fileName, errorDirectory, outputDirectory):
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        lineCount = 0
        jsonData = []
        columnIndexes = {"INTERNAL_ID":0,
                         "FIRST_NAME":1,
                         "MIDDLE_NAME":2,
                         "LAST_NAME":3,
                         "PHONE_NUM":4}
        for row in csv_reader:
            if lineCount > 0:
                attributes = {"INTERNAL_ID":row[columnIndexes["INTERNAL_ID"]],
                              "FIRST_NAME":row[columnIndexes["FIRST_NAME"]],
                              "MIDDLE_NAME":row[columnIndexes["MIDDLE_NAME"]],
                              "LAST_NAME":row[columnIndexes["LAST_NAME"]],
                              "PHONE_NUM":row[columnIndexes["PHONE_NUM"]]}
                if validate():
                    tempDict = {}
                    jsonData.append({"id" :
                                 "name": {
                                          "first" : row[columnIndexes["FIRST_NAME"]],
                                          "last" : row[columnIndexes["LAST_NAME"]]},
                                 "phone": row[columnIndexes["PHONE_NUM"]],})
                lineCount += 1
            else:
                for attr in row:
                    index = 0
                    columnIndexes[attr] = index
                    index += 1

def validate(attributeValues):
    errorDir = sys.argv[3]
    if attributeValues["INTERNAL_ID"]


if __name__ == "__main__": main()
