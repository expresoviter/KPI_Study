from dfs import LDFS
from astar import aStar
from pyamaze import maze, agent, COLOR

n = int(input("Введіть довжину лабіринту:"))
m = int(input("Введіть ширину лабіринту:"))
myMaze = maze(n, m)
myMaze.CreateMaze(loopPercent=50)
p = int(input("Введіть максимальну глибину для LDFS:"))
searchPath, aPath, fwdPath = aStar(myMaze)
dSearch, dfsPath, fwdDFSPath = LDFS(myMaze, p)


a = agent(myMaze, footprints=True, color=COLOR.cyan, filled=True)
b = agent(myMaze, footprints=True, color=COLOR.yellow)
a1 = agent(myMaze, footprints=True, color=COLOR.red, filled=True)
b1 = agent(myMaze, footprints=True, color=COLOR.green, filled=True)
myMaze.tracePath({a: dSearch}, delay=50)
myMaze.tracePath({b: searchPath}, delay=50)
myMaze.tracePath({b1: fwdPath}, delay=50)
myMaze.tracePath({a1: fwdDFSPath}, delay=50)

myMaze.run()
