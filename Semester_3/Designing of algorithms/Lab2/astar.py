from queue import PriorityQueue


def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)


def aStar(m, start=None):
    maxMem=0
    end=0
    if start is None:
        start = (m.rows, m.cols)
    open = PriorityQueue()
    open.put((h(start, m._goal), h(start, m._goal), start))
    aPath = {}
    g_score = {row: float("inf") for row in m.grid}
    g_score[start] = 0
    f_score = {row: float("inf") for row in m.grid}
    f_score[start] = h(start, m._goal)
    searchPath = [start]
    counter=0
    while not open.empty():
        maxMem=max(maxMem,open.qsize())
        poss = 0
        counter+=1
        currCell = open.get()[2]
        searchPath.append(currCell)
        if currCell == m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                if childCell not in searchPath:
                    poss+=1

                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell, m._goal)

                if temp_f_score < f_score[childCell]:
                    aPath[childCell] = currCell
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_g_score + h(childCell, m._goal)
                    open.put((f_score[childCell], h(childCell, m._goal), childCell))

        if poss==0:
            end+=1

    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    print("Кількість ітерацій A* = ",counter+1)
    print("Кількість глухих кутів A* =",end)
    print('A-Star Path Length =', len(fwdPath))
    print("Максимум станів у пам'яті A* =",maxMem)
    return searchPath, aPath, fwdPath
