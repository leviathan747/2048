import json
import flask

app = flask.Flask(__name__)

lastMove = 0

@app.route('/move', methods=['POST'])
def getMove():
    global lastMove
    data = json.loads(flask.request.get_data())
    lastMove = 0 if lastMove != 0 else 3
    resp = flask.Response(json.dumps({'move': lastMove}))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

app.run()
