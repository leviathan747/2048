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
    data = json.loads(flask.request.get_data())
    if 'size' in data and 'cells' in data and 'score' in data:
        move = calculateMove(data['size'], data['cells'], data['score'])
        resp = flask.Response(json.dumps({'move': move}))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    else:
        return 400, 'Request did not contain correct data.'

def calculateMove(size, cells, score):
    global lastMove, lastBoard, numMatches
    if cells == lastBoard:
        numMatches += 1
    else:
        numMatches = 0
    lastBoard = cells
    if numMatches >= 2:
        # go left to break out of stalemate
        lastMove = 0
    else:
        # alternate between right and down
        lastMove = 3 if lastMove != 3 else 2
    return lastMove

app.run()
