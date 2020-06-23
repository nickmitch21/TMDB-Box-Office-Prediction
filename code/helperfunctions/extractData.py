import re

#function that uses a regex to extract data we need from various cols in dataset
def extractData(str):
    return re.findall("'name': \'(.+?)\'", str)