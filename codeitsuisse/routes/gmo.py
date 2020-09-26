import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/intelligent-farming', methods=['POST'])
def evaluate():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    runId = data.get("runId")
    allLists = resequence(data.get("list"))
    result = {"runId":runId, "list": allLists}
    logging.info("My result :{}".format(result))
    return json.dumps(result);

def resequence():
    return []
