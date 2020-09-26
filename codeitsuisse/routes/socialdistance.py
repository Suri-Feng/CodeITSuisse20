import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/social_distancing', methods=['POST'])
def evaluateSocialDistancing():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    result = ways(data.get("tests"))
    logging.info("My result :{}".format(result))
    return jsonify(result);

import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def ways(tests):
    result={}
    for key, testcase in tests.items():
        places=testcase["people"]+1
        seats = testcase["seats"] - testcase["people"] - (testcase["people"]-1)*testcase["spaces"]
        if seats < 0:
            return 0
        result[key] = ncr(seats+places-1,seats)
    return {"answers":result}
