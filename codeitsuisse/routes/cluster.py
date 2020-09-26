import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/square', methods=['POST'])
def evaluate():
    data = request.get_date();
    logging.info("data sent for evaluation {}".format(data))
    result = cluster(data)
    logging.info("My result :{}".format(result))
    return json.dumps(result);

def unionaround(grid, x, y, uf):
    m, n = len(grid), len(grid[0])
    dx = [-1 , 1, 0, 0, -1, 1, 1, -1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    for i in range(8):
        nx = x+dx[i]
        ny = x+dy[i]
        if (nx < 0 or nx >= m or ny<0 or ny >=n):
            continue
        if grid[nx][ny] != "*":
            uf.union(x*n + y + 1, nx*n +ny + 1)
    if (grid[x][y] == '1'):
        uf.union(x*n+y+1, 0)


def cluster(grid):
    m = len(grid)
    n = len(grid[0])
    num = m*n + 1
    uf = Unionfind(num)
    for i in range(m):
        for j in range(n):
            if (grid[i][j] != "*"):
                unionaround(grid, i, j, uf)
    ans = 0
    for i in range(num):
        if uf.parents[i] < -1 and uf.connected(i, 0):
            ans += 1
    print(uf.parents)
    return {"result":ans}


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
        root1 = self.find(v1)
        root2 = self.find(v2)
        if (root1 != root2 or (root1 == -1 and root2 == -1)):
            self.parents[root1] = root2
            self.parents[root2] -= size1