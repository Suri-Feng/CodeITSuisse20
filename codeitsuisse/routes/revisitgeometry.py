import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/revisitgeometry', methods=['POST'])
def evaluateGeometry():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    #inputValue = data.get("input");
    result = geometry(data.get("shapeCoordinates"), data.get("lineCoordinates"))
    logging.info("My result :{}".format(result))
    return jsonify(result);

def geometry(shapeCoordinates, lineCoordinates):
    from numpy import ones,vstack
    from numpy.linalg import lstsq
    results=[]
    # Change the dataformate 
    fixedpoints = []
    for lineCoordinate in lineCoordinates:
        fixedpoints.append((lineCoordinate["x"],lineCoordinate["y"]))
    shapeCoordinates.append(shapeCoordinates[0])
    for i in range(len(shapeCoordinates)-1):
        movingpoints=[(shapeCoordinates[i]["x"],shapeCoordinates[i]["y"]),(shapeCoordinates[i+1]["x"],shapeCoordinates[i+1]["y"])]
        interSection=line_intersection(fixedpoints, movingpoints)
        if ((interSection[0]<=movingpoints[0][0] and  interSection[0]>=movingpoints[1][0]) or (interSection[0]>=movingpoints[0][0] and  interSection[0]<=movingpoints[1][0]))\
        and ((interSection[1]<=movingpoints[0][1] and  interSection[1]>=movingpoints[1][1]) or (interSection[1]>=movingpoints[0][1] and  interSection[1]<=movingpoints[1][1])):
            if interSection not in results:
                results.append({"x": interSection[0], "y": interSection[1]})
    return results

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y
