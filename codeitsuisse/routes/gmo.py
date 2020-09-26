import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/intelligent-farming', methods=['POST'])
def evaluateGMO():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    runId = data.get("runId")
    allLists = resequence(data.get("list"))
    result = {"runId":runId, "list": allLists}
    logging.info("My result :{}".format(result))
    return json.dumps(result);

def resequence(myList):
    ids = []
    seqs = []
    seqs2 = []
    ans = []
    for dicts in myList:
        ids.append(dicts.get('id'))
        seqs.append(dicts.get('geneSequence'))
    n = len(ids)
    for i in range(n):
        seqs2.append(shuffle(seqs[i]))
    for i in range(n):
        ans.append({"id": ids[i], "geneSequence": seqs2[i]})
    return ans 

def shuffle(seq):
    A = 0
    C = 0
    G = 0
    T = 0
    for char in seq:
        if char == 'A':
            A += 1
        if char == 'C':
            C += 1
        if char == 'G':
            G += 1
        if char == 'T':
            T += 1
    AGT_smallest = A
    if G < AGT_smallest:
        AGT_smallest = G
    if T < AGT_smallest:
        AGT_smallest = T
    diff = C - AGT_smallest
    if diff <= 0:
        ans = reconstructACGT(A, C, G, T)
    else:
        ans = reconstructCC(A, C, G, T, diff, AGT_smallest)
    return ans 

def reconstructACGT(A, C, G, T):
    ans = 'ACGT'*C
    A -= C
    G -= C
    T -= C
    while (A > 0):
        if A == 1:
            ans += 'A'
            A -= 1
        else:
            ans += 'A'
            A -= 2
        if T > 0:
            ans += 'T'
            T -= 1
        elif G > 0:
            ans += 'G'
            G -= 1 
    while(T > 0):
        ans += 'T'
        T -= 1
    while(G>0):
        ans += "G"
        G -= 1
    return ans

def reconstructCC(A, C, G, T, diff, AGT_smallest):
    if diff%2 == 0:
        CC = diff/2
        ACGT = AGT_smallest
    else:
        CC = int(diff/2) + 1
        ACGT = AGT_smallest - 1 
    ans = 'ACGT'*ACGT
    A -= ACGT
    G -= ACGT
    T -= ACGT
    while (A > 0):
        if A == 1:
            ans += 'A'
            A -= 1
        else:
            ans += 'A'
            A -= 2
        if CC > 0:
            ans += 'CC'
            CC -= 1
        elif T > 0:
            ans += 'T'
            T -= 1
        elif G > 0:
            ans += 'G'
            G -= 1 
    while (CC > 0):
        ans += 'CC'
        CC -= 1
    while(T > 0):
        ans += 'T'
        T -= 1
    while(G>0):
        ans += "G"
        G -= 1
    return ans
