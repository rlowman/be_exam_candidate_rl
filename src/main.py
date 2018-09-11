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
    if len(sys.argv) != 4:  # If one of our directories is not given as an argument
                            # then we cannot continue with our application
        print("Invalid number of arguments.")
        valid = False
    else:
        for arg in sys.argv[1:]
        if not os.path.isdir(arg):  # Validates that given arguments are directories
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
                    if temp.endswith(".csv"):   # We only want to deal with csv files
                        processFile(str(inputDir + "/" + temp), errorDir, outputDir)


def processFile(fileName, errorDirectory, outputDirectory):
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        lineCount = 0
        jsonData = []   # Array of dictronaries that will be dumped to JSON

        # Assuming that csv columns will come in different orders, hold the index
        # for each attribute for the csv file currently being processed
        columnIndexes = {"INTERNAL_ID":0,
                         "FIRST_NAME":1,
                         "MIDDLE_NAME":2,
                         "LAST_NAME":3,
                         "PHONE_NUM":4}
        for row in csv_reader:
            if lineCount > 0:
                # Retrive necessary information from csv row
                idNum = row[columnIndexes["INTERNAL_ID"]]
                first = row[columnIndexes["FIRST_NAME"]],
                middle = row[columnIndexes["MIDDLE_NAME"]],
                last = row[columnIndexes["LAST_NAME"]],
                phone = row[columnIndexes["PHONE_NUM"]]}

                # If the the information is valid then add to our JSON dictionary
                if validate(idNum, first, middle, last, phone, lineCount):
                    tempDict = {"id":int(idNum)}

                    # Process all the name data
                    name = {"first" : first}
                    if middle != "":
                        name["middle"] = middle
                    name["last"] = last
                    tempDict["name"] = name

                    tempDict["phone"] = phone
                    jsonData.append(tempDict)
                    lineCount += 1
            else:
                index = 0
                for attr in row:
                    columnIndexes[attr] = index     # Sets a new value of index
                    index += 1

def validate(idString, firstName, middleName, lastName, phoneNumber, line):
    errorDir = sys.argv[3]
    errorString = str(line + ": ")
    valid = True

    # Validate identification number
    if idString == "":
        errorString += "ID cannot be empty.\n"
        valid = False
    elif len(attributeValues) > 8:
        errorString += "ID value cannot exceed 8 digits.\n"
        valid = False
    try:
        parsedId = int(identification)
        if parsedId < 0:
            errorString += "ID cannot be negative.\n"
            valid = False
    except ValueError:
        errorString += "ID contains invalid characters.\n"
        valid = False

    # Validate first name
    if firstName == "":
        errorString += "First name cannot be empty.\n"
        valid = False
    elif len(firstName) > 15:
        errorString += "First name cannot exceed 15 characters.\n"
        valid = False

    #Validate middle name
    if len(middleName) > 15:
        errorString += "Middle name cannot exceed 15 characters.\n"

    # Validate last name
    if lastName == "":
        errorString += "Last name cannot be empty.\n"
        valid = False
    elif len(lastName) > 15:
        errorString += "Last name cannot exceed 15 characters.\n"
        valid = False

    



if __name__ == "__main__": main()
