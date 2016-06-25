# WebCrawler
import urllib.request
import re

def extractData(data, pattern):
    extracted = pattern.findall(data)
    noRepeatData = set(extracted)
    extracted = list(noRepeatData)
    return extracted

initialiser = input("Please enter the initial website: ")

initialLink = urllib.request.urlopen(initialiser)

#Patterns
linkPattern = re.compile(r'http[s]*\://[www\.]?\w+\.\w+[\.\w+]*[/\w[\.\w]*]*')
noPattern = re.compile(r'\d{5,5}[-|\s]*\d{5,5}')
emailPattern = re.compile(r'\w+@\w+\.\w+[\.\w]*')

crudeData = str(initialLink.read())

linkList = extractData(crudeData, linkPattern)
noList = extractData(crudeData, noPattern)
emailList = extractData(crudeData, emailPattern)

for no in noList:
    noFile = open('Numbers.txt', 'a')
    noFile.write(no + '\n')
    noFile.close()

for email in emailList:
    emailFile = open('Emails.txt', 'a')
    emailFile.write(email + '\n')
    emailFile.close()

for link in linkList:

    try:
        crudeLink = urllib.request.urlopen(link)
        crudeData = str(crudeLink.read())

        tempNos = extractData(crudeData, noPattern)
        tempEmails = extractData(crudeData, emailPattern)
        tempLinks = extractData(crudeData, linkPattern)

        for no in tempNos:
            if no not in noList:
                noFile = open('Numbers.txt', 'a')
                noFile.write(no + '\n')
                noFile.close()
                noList.append(no)

        for email in tempEmails:
            if email not in emailList:
                emailFile = open('Emails.txt', 'a')
                emailFile.write(email + '\n')
                emailFile.close()

        for tempLink in tempLinks:
            if tempLink not in linkList:
                linkFile = open('Crawled.txt', 'a')
                linkFile.write(tempLink + '\n')
                linkFile.close()
                linkList.append(tempLink)
    except:
        pass