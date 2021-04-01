
from urllib.parse import urljoin
from urllib.request import urlopen
from html.parser import HTMLParser

# Define Global variable to enable access inside or outside of the function
TopWord = 25
url = 'https://en.wikipedia.org/wiki/DePaul_University'


def main():
    """This main function is to arrange all functions in this program"""

    printIntro()
    content = analyze()
    sortedList = wordFrq(content)
    realList = sortFreq(sortedList)
    topCommonWord(realList)


def printIntro():
    """This printIntro() is to inform users for number of top word and url where retrieved info"""

    global url, TopWord                                         # reminder of global variable
    print('-'*85)
    print("Here is the list of top {} words on: {}".format(TopWord, url))
    print("The result will appear in the format of [count, word]")
    print('-'*85)


class MyHTMLParser(HTMLParser):
    """overriding superclass:HTMLParser to MyHTMLParser child class"""

    def __init__(self, url1):
        """This method is to initialize parser, data, url, and a list"""

        HTMLParser.__init__(self)
        self.data = []
        self.url1 = url1
        self.links = []

    def handle_starttag(self, tag, attrs):
        """This handle_starttag method is to handle starttag and collects hyperlink URLs in their absolute format,
            this hyperlink collection is left to be developed in the future utilization"""

        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    absolute = urljoin(self.url1, attr[1])    # construct absolute URL
                    if absolute[:4] == 'http':                # collect HTTP URLs
                        self.links.append(absolute)

    def getLinks(self):
        """This getLinks method is to return hyperlinks URLs in their absolute format"""
        return self.links

    def handle_data(self, data):
        """This handle_data method is to eliminate unnecessary words and handle data"""

        cleanData = data.strip().split()
        for i in cleanData:
            cliche1 = ['a', 'an', 'are', 'and', 'of', 'to', 'in', 'this', 'as', 'it', 'was', 'for']
            cliche2 = ['on', 'of', 'or', 'is', 'if', 'by', 'at', 'we', 'the', 'you', 'we', 'they']
            cliche = cliche1 + cliche2
            if i.isalpha() and i not in cliche:              # select only string and eliminate nonessential words
                self.data.append(i.lower())

    def getData(self):
        """This getData method is to display the handled data"""
        return self.data


def analyze():
    """This analyze() is to read html, decode, feed content in superclass, return cleaned content"""
    global url                                               # reminder of global variable
    content = urlopen(url).read().decode()                   # read to return content of HTML, decode to str
    parser = MyHTMLParser(url)                               # call HTMLParser
    parser.feed(content)                                     # fed html file to parser
    content = parser.getData()                               # manipulated content

    return content


def wordFrq(content):
    """This wordFrq() is to count number of word appeared in list and return in descending order"""

    wordFreq = [[content.count(i), i] for i in content]     # count unique words
    wordSort = sorted(wordFreq, reverse=True)               # sort in descending order

    return wordSort


def sortFreq(wordSort):
    """This sortFrq() is to filter the repetitive displays"""

    realList = []
    for i in wordSort:
        if i not in realList:
            realList.append(i)

    return realList


def topCommonWord(realList):
    """This topCommonWord() is to print the top word appeared on the website with order, count and word"""

    global TopWord                                          # reminder of global variable
    print("No : [Count, 'Word] ")
    print('\n'.join(['%i :  %s' % (n, realList[n]) for n in range(TopWord)]))


if __name__ == "__main__":
    main()
