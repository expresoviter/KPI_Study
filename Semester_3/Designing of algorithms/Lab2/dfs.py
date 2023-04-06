def LDFS(m, level, start=None):
    maxMem=0
    end=0
    if start is None:
        start = (m.rows, m.cols)
    explored = []
    frontier = [[0, start]]
    dfsPath = {}
    dSeacrh = []
    counter=0
    while len(frontier) > 0:
        maxMem=max(maxMem,len(frontier))
        counter+=1
        lev, currCell = frontier.pop()
        dSeacrh.append(currCell)
        if currCell == m._goal:
            break
        poss = 0
        if currCell in explored or lev >= level:
            continue
        explored.append(currCell)
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    child = (currCell[0], currCell[1] + 1)
                if d == 'W':
                    child = (currCell[0], currCell[1] - 1)
                if d == 'N':
                    child = (currCell[0] - 1, currCell[1])
                if d == 'S':
                    child = (currCell[0] + 1, currCell[1])
                if child not in explored:
                    poss += 1
                    frontier.append([lev + 1, child])
                    dfsPath[child] = currCell
        if poss > 1:
            m.markCells.append(currCell)
        if poss==0:
            end+=1
    fwdPath = {}
    cell = m._goal
    if cell in dfsPath:
        while cell != start:
            fwdPath[dfsPath[cell]] = cell
            cell = dfsPath[cell]
    else:
        print("На такій глибині шлях LDFS знайти не може")
    print("Кількість ітерацій LDFS = ", counter)
    print("Кількість глухих кутів LDFS =",end)
    print('LDFS Path Length =', len(fwdPath))
    print("Максимум станів у пам'яті LDFS =",maxMem)
    return dSeacrh, dfsPath, fwdPath
