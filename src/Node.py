class Node():
    def __init__(self, position, children):
        self.children = self.parseChildren(children)
        self.position = self.parseTuple(position)

    def getChildren(self):
        return self.children

    def getPosition(self):
        return self.position

    def parseTuple(self, str):
        myPair = str.split(',')
        return (int(myPair[0]), int(myPair[1]))

    def parseChildren(self, argChildren):
        myChildren = []
        for child in argChildren:
            myChildren.append(self.parseTuple(child['Id']))
        return myChildren
