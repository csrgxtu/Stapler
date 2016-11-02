#!/usr/bin/env python
# encoding=utf-8
#
# Author: Archer
# File: graph.py
# Date: 02/Nov/2016
# Desc: 实现火车路径的相关问题
#
# Produced By CSRGXTU


class TrainGraph(object):
    """
        实现火车路径数据的图表示
        按照给定路径,计算距离
        查找符合条件的路径
    """
    Nodes = [] # all nodes alphabatically
    Graph = []

    def __init__(self, lst):
        """用矩阵表示火车路径有向图"""

        # get all Nodes
        for e in lst:
            self.Nodes.append(e[0])
            self.Nodes.append(e[1])
        self.Nodes = sorted(list(set(self.Nodes)))

        # build the graph mat
        for i in range(len(self.Nodes)):
            self.Graph.append([0] * len(self.Nodes)) # at the begining, all 0

        for i in range(len(self.Graph)):
            for j in range(len(self.Graph)):
                locations = self.Nodes[i] + self.Nodes[j]  # 两个地点
                for e in lst:
                    if locations in e:
                        self.Graph[i][j] = e[2:]
                        break

        print self.Graph

    def GetDistanceByRoute(self, route):
        """ 根据给出的路径计算距离 """
        pass

    def GetRouteAccordingConditions(self, start, end, stops):
        """ 给出起点终点, 按照stops找出路径 """
        pass

    def ToString(self):
        """ 给出图的序列化表示 """
        pass

if __name__ == "__main__":
    # load the test input data
    data = [] # in AB2 format
    with open('graph.data') as FH:
        rawData = FH.read().strip()
        data = rawData.split(', ')

    Graph = TrainGraph(data)
