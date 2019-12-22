# Simple 2048 bot
#
# Alternate between right and down. If two moves in a row result in no change
# to the board, move left and then continue.

import json
import flask

app = flask.Flask(__name__)

lastMove = 2
lastBoard = None
numMatches = 0

@app.route('/move', methods=['POST'])
def getMove():
    global lastMove, lastBoard, numMatches
    data = json.loads(flask.request.get_data())
    if data['cells'] == lastBoard:
        numMatches += 1
    else:
        numMatches = 0
    lastBoard = data['cells']
    if numMatches >= 2:
        # go left to break out of stalemate
        lastMove = 0
    else:
        # alternate between right and down
        lastMove = 3 if lastMove != 3 else 2
    resp = flask.Response(json.dumps({'move': lastMove}))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

app.run()
