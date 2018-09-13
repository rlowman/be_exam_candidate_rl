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
        for arg in sys.argv[1:]:
            if not os.path.isdir(arg):  # Validates that given arguments are directories
                valid = False
                print(arg + " is not a valid directory.")

    if valid:
        inputDir = sys.argv[1]
        outputDir = sys.argv[2]
        errorDir = sys.argv[3]

        while(True):
            files = os.listdir(inputDir)
            csvFiles = []
            for temp in files:
                if temp.endswith(".csv"):   # We only want to deal with csv files
                    csvFiles.append(temp)
            if len(csvFiles) > 0:
                for f in csvFiles:
                    processFile(f, inputDir, errorDir, outputDir)
                    print("Processing " + f)
            else:
                time.sleep(5) # Wait 5 seconds if nothing new is found in directory
                print ("Waiting")


def processFile(fileName, inputDirectory, errorDirectory, outputDirectory):
    lineCount = 0
    errorDict = {}
    jsonData = []   # Array of dictionaries that will be dumped to JSON
    with open(str(inputDirectory + "/" + fileName), 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

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
                first = row[columnIndexes["FIRST_NAME"]]
                middle = row[columnIndexes["MIDDLE_NAME"]]
                last = row[columnIndexes["LAST_NAME"]]
                phone = row[columnIndexes["PHONE_NUM"]]

                # If the the information is valid then add to our JSON dictionary
                errorList = validate(idNum, first, middle, last, phone)
                print(len(errorList))
                if len(errorList) == 0:     # Add to JSON if no errors were found
                    tempDict = {"id": int(idNum)}

                    # Process all the name data
                    name = {"first" : first}
                    if middle != "":
                        name["middle"] = middle
                    name["last"] = last
                    tempDict["name"] = name

                    tempDict["phone"] = phone
                    print (tempDict)
                    jsonData.append(tempDict)
                    lineCount += 1
                else:
                    errorDict[lineCount] = errorList # Store found errors
            else:
                index = 0
                for attr in row:
                    columnIndexes[attr] = index     # Sets a new value of index
                    index += 1
                lineCount += 1
    if len(errorDict) > 0:
        with open(str(inputDir+ "/" + fileName), "w") as errorFile:
            headers = ["LINE_NUM", "ERROR_MSG"]
            writer = csv.DictWriter(errorFile, fieldnames=headers)
            writer.writeheader()
            for key in errorDict:
                for value in errorDict[key]:
                    writer.writerow({"LINE_NUM" : str(key), "ERROR_MSG" : value})
    jsonName = str(fileName[:len(fileName) - 4] + ".json")
    with open(outputDirectory + "/" + jsonName, "w") as w:
        json.dump(jsonData,w,indent = 4, sort_keys=True)
    os.remove(inputDirectory + "/" + fileName)


def validate(idString, firstName, middleName, lastName, phoneNumber):
    errors = []     # List that holds errors collected throughout validation

    # Validate identification number
    if idString == "":
        errors.append("ID cannot be empty.")
    elif len(idString) > 8:
        errors.append("ID value cannot exceed 8 digits.")
    try:
        parsedId = int(idString)
        if parsedId < 0:
            errors.append("ID cannot be negative.")
    except ValueError:
        errors.append("ID contains invalid characters.")

    # Validate first name
    if firstName == "":
        errors.append("First name cannot be empty.")
    elif len(firstName) > 15:
        errors.append("First name cannot exceed 15 characters.")

    # Validate middle name
    if len(middleName) > 15:
        errors.append("Middle name cannot exceed 15 characters.")

    # Validate last name
    if lastName == "":
        errors.append("Last name cannot be empty.")
    elif len(lastName) > 15:
        errors.append("Last name cannot exceed 15 characters.")

    # Validate phone number
    if len(phoneNumber) < 12:
        errors.append("Phone number is too short.")
    elif len(phoneNumber) > 12:
        errors.append("Phone number is too long.")
    if phoneNumber[3] != "-" and phoneNumber[7] != "-":
        errors.append("Phone number is not in correct format (###-###-####).")
    else:
        if not (phoneNumber[:3].isdigit() and
                phoneNumber[4:7].isdigit() and
                phoneNumber[8:].isdigit()):
            errors.append("Phone number contains invalid characters.")
    return errors




if __name__ == "__main__": main()
