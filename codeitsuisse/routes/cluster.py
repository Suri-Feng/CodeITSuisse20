import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/cluster', methods=['POST'])
def evaluateCluster():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    result = cluster(data)
    logging.info("My result :{}".format(result))
    return jsonify(result);

def unionaround(grid, x, y, uf):
    m, n = len(grid), len(grid[0])
    dx = [-1 , 1, 0, 0, -1, 1, 1, -1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    onlyOne = True
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if (nx < 0 or nx >= m or ny<0 or ny >=n):
            continue
        if grid[nx][ny] != "*":
            uf.union(x*n + y + 1, nx*n +ny + 1)
            onlyOne = False
    if grid[x][y] == '1':
        if onlyOne == False:
            uf.union(x*n+y+1, 0)
        if onlyOne == True:
            uf.union(x*n+y+1, n*m +1)


def cluster(grid):
    m = len(grid)
    n = len(grid[0])
    num = m*n + 2
    uf = Unionfind(n*m +2)
    for i in range(m):
        for j in range(n):
            if (grid[i][j] != "*"):
                unionaround(grid, i, j, uf)
    ans = 0
    print(uf.parents)
    for i in range(1, n*m+1):
        if uf.parents[i] < -1  and uf.connected(i, 0):
            ans += 1
        if uf.connected(i, n*m+1):
            ans += 1
    return {"answer":ans}


class Unionfind:
    def __init__(self, n):
        self.parents = [-1]*n

    def size(self, v):
        i = self.find(v)
        size = abs(self.parents[i])
        return size

    def connected(self, v1, v2):
        return self.find(v1) == self.find(v2)
        
    def find(self, v):
        r = v
        while(self.parents[r] >= 0):
            r = self.parents[r]
        return r

    def union(self, v1, v2):
        size1 = self.size(v1)
        size2 = self.size(v2)
        root1 = self.find(v1)
        root2 = self.find(v2)
        if (root1 != root2 or (root1 == -1 and root2 == -1)):
            if size1<=size2:
                self.parents[root1] = root2
                self.parents[root2] -= size1
            else:
                self.parents[root2] = root1
                self.parents[root1] -= size2