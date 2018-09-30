import json
from Node import Node


class Board():

    def __init__(self, gameData):
        self.startingPos = gameData['startingNode']
        self.targetPos = gameData['targetNode']
        self.nodes = self.getNodesFromData(gameData['nodes'])

    def getNodesFromData(self, nodes):
        nodeDict = {}
        for item in nodes:
            n = Node(item["Id"], item["children"])
            nodeDict[n.getPosition()] = n.getChildren()
        return nodeDict

    def getNodes(self):
        return self.nodes


def dataFromJson(jsonObject):
    with open(jsonObject) as f:
        data = json.load(f)
    return data


if __name__ == "__main__":

    b = Board(dataFromJson('./example.json'))
    print(b.getNodes())
