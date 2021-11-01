import os
import sys
import csv
import requests

args = sys.argv[1:]
numArgs = len(args)
apiURL = 'http://127.0.0.1:8000/api/v1/cards/'
importedCardsCount = 0

def showDescription():
    print('This utilitary imports csv files to Insights API')
    print('Usage: "python ImportInsights.py <path_to_csv_file> <api_url>"')
    print('Example: python ImportInsights.py cards.csv http://127.0.0.1:8000/api/v1/cards/')
    print('If no api url is passed, it assumes localhost:8000/api/v1/cards/')

def sendCardToApi(card):
    global importedCardsCount
    global apiURL
    resp = requests.post(apiURL, json=card)
    if resp.status_code != 201:
        raise Exception('Card rejected by API with status message: ' + resp.reason)
    importedCardsCount = importedCardsCount + 1
    print('Card ' + str(importedCardsCount) + ' enviado')


def verifyFormat(csvReader):
    header = next(csvReader)
    if header[0] != 'text' or header[1] != 'tag':
        raise ValueError('Invalid csv file, format and header needs to be: "text", "tag1;tag2..."')

def rowToCard(row):
    text = row[0]
    tags = row[1]
    if tags != '':
        tags = [{"nome": nome} for nome in row[1].split(';')]
    else:
        tags = []
    card = {
        "texto" : text,
        "tags": tags
    }
    return card

def extractAndSendCards(csvFile):
    csvReader = csv.reader(csvFile, delimiter=',')
    verifyFormat(csvReader)
    for row in csvReader:
        card = rowToCard(row)
        sendCardToApi(card)

def main():
    global apiURL
    global importedCardsCount
    try:
        print('Starting importation...' + str(numArgs))
        if numArgs < 1:
            showDescription()
        else:
            csvPath = args[0]
            if numArgs == 2:
                apiURL = args[1]
            with open(csvPath) as csvFile:
                extractAndSendCards(csvFile)
        print('Total ' + str(importedCardsCount) + ' cards importeds')
    except Exception as e:
        print('An error occured: ' + str(e))

if __name__ == '__main__':
    main()