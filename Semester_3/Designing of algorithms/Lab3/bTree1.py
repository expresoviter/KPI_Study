from math import trunc
from random import randint


class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


class BTree:
    def __init__(self, t, visual):
        self.root = BTreeNode(True)
        self.t = t
        self.window = visual

    def start(self):
        enter = [int(i) for i in self.window.values.displayText().split()]
        ind = self.window.box.currentIndex()
        exis, y = [-1], -1
        if ind == 1:
            for i in range(enter[0]):
                while y in exis:
                    y = randint(0, 10000)
                exis.append(y)
                self.insert((i,y))
        elif ind == 2:
            self.insert((enter[0], enter[1]))
        elif ind == 3:
            self.delete(self.root, (enter[0], ""))
        elif ind == 4:
            if len(enter) == 1:
                self.searchEdit(enter[0])
            else:
                self.searchEdit(enter[0],None, enter[1])
        self.window.treeLabel.label.setText("")
        self.printTree(self.root)

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.splitChild(temp, 0)
            self.insertNonFull(temp, k)
        else:
            self.insertNonFull(root, k)

    def insertNonFull(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.splitChild(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            self.insertNonFull(x.child[i], k)

    def splitChild(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

    def delete(self, x, k):
        t = self.t
        i = 0
        while i < len(x.keys) and k[0] > x.keys[i][0]:
            i += 1
        if x.leaf:
            if i < len(x.keys) and x.keys[i][0] == k[0]:
                x.keys.pop(i)
                return
            return

        if i < len(x.keys) and x.keys[i][0] == k[0]:
            return self.deleteInternalNode(x, k, i)
        elif len(x.child[i].keys) >= t:
            self.delete(x.child[i], k)
        else:
            if i != 0 and i + 2 < len(x.child):
                if len(x.child[i - 1].keys) >= t:
                    self.deleteSibling(x, i, i - 1)
                elif len(x.child[i + 1].keys) >= t:
                    self.deleteSibling(x, i, i + 1)
                else:
                    self.deleteMerge(x, i, i + 1)
            elif i == 0:
                if len(x.child[i + 1].keys) >= t:
                    self.deleteSibling(x, i, i + 1)
                else:
                    self.deleteMerge(x, i, i + 1)
            elif i + 1 == len(x.child):
                if len(x.child[i - 1].keys) >= t:
                    self.deleteSibling(x, i, i - 1)
                else:
                    self.deleteMerge(x, i, i - 1)
            self.delete(x.child[i], k)

    def deleteInternalNode(self, x, k, i):
        t = self.t
        if x.leaf:
            if x.keys[i][0] == k[0]:
                x.keys.pop(i)
                return
            return

        if len(x.child[i].keys) >= t:
            x.keys[i] = self.deletePredecessor(x.child[i])
            return
        elif len(x.child[i + 1].keys) >= t:
            x.keys[i] = self.deleteSuccessor(x.child[i + 1])
            return
        else:
            self.deleteMerge(x, i, i + 1)
            self.deleteInternalNode(x.child[i], k, self.t - 1)

    def deletePredecessor(self, x):
        if x.leaf:
            return x.pop()
        n = len(x.keys) - 1
        if len(x.child[n].keys) >= self.t:
            self.deleteSibling(x, n + 1, n)
        else:
            self.deleteMerge(x, n, n + 1)
        self.deletePredecessor(x.child[n])

    def deleteSuccessor(self, x):
        if x.leaf:
            return x.keys.pop(0)
        if len(x.child[1].keys) >= self.t:
            self.deleteSibling(x, 0, 1)
        else:
            self.deleteMerge(x, 0, 1)
        self.deleteSuccessor(x.child[0])

    def deleteMerge(self, x, i, j):
        cnode = x.child[i]
        if j > i:
            rsnode = x.child[j]
            cnode.keys.append(x.keys[i])
            for k in range(len(rsnode.keys)):
                cnode.keys.append(rsnode.keys[k])
                if len(rsnode.child) > 0:
                    cnode.child.append(rsnode.child[k])
            if len(rsnode.child) > 0:
                cnode.child.append(rsnode.child.pop())
            new = cnode
            x.keys.pop(i)
            x.child.pop(j)
        else:
            lsnode = x.child[j]
            lsnode.keys.append(x.keys[j])
            for i in range(len(cnode.keys)):
                lsnode.keys.append(cnode.keys[i])
                if len(lsnode.child) > 0:
                    lsnode.child.append(cnode.child[i])
            if len(lsnode.child) > 0:
                lsnode.child.append(cnode.child.pop())
            new = lsnode
            x.keys.pop(j)
            x.child.pop(i)

        if x == self.root and len(x.keys) == 0:
            self.root = new

    def deleteSibling(self, x, i, j):
        cnode = x.child[i]
        if i < j:
            rsnode = x.child[j]
            cnode.keys.append(x.keys[i])
            x.keys[i] = rsnode.keys[0]
            if len(rsnode.child) > 0:
                cnode.child.append(rsnode.child[0])
                rsnode.child.pop(0)
            rsnode.keys.pop(0)
        else:
            lsnode = x.child[j]
            cnode.keys.insert(0, x.keys[i - 1])
            x.keys[i - 1] = lsnode.keys.pop()
            if len(lsnode.child) > 0:
                cnode.child.insert(0, lsnode.child.pop())

    def printTree(self, x, l=0):
        self.window.treeLabel.label.setText(
            self.window.treeLabel.label.text() + "Level " + str(l) + " " + str(len(x.keys)) + ": ")
        for i in x.keys:
            self.window.treeLabel.label.setText(
                self.window.treeLabel.label.text() + "(" + str(i[0]) + ", " + str(i[1]) + ") ")
        self.window.treeLabel.label.setText(self.window.treeLabel.label.text() + "\n")
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.printTree(i, l)

    def searchEdit(self, k, x=None, ed=None):
        if x is not None:
            lst = x.keys[::]
            d = trunc(len(lst) / 2)
            i = d
            if len(lst) % 2 == 0:
                lst.append((lst[-1][0] ** 2 + 1, 0))
            while d != 0:
                if lst[i][0] == k:
                    self.window.lab.setText("Знайдено: (" + str(x.keys[i][0]) + ", " + str(x.keys[i][1]) + ")")
                    if ed is not None:
                        x.keys[i] = (x.keys[i][0], ed)
                    return x, (x.keys[i])
                elif lst[i][0] < k:
                    i += (trunc(d / 2) + 1)
                else:
                    i -= (trunc(d / 2) + 1)
                d = trunc(d / 2)
            if i < len(lst) and lst[i][0] == k:
                self.window.lab.setText("Знайдено: (" + str(x.keys[i][0]) + ", " + str(x.keys[i][1]) + ")")
                if ed is not None:
                    x.keys[i] = (x.keys[i][0], ed)
                return x, (x.keys[i])
            elif x.leaf:
                self.window.lab.setText("Не знайдено:(")
                return None
            else:
                if lst[i][0] > k:
                    return self.searchEdit(k, x.child[i], ed)
                else:
                    return self.searchEdit(k, x.child[i + 1], ed)

        else:
            return self.searchEdit(k, self.root, ed)