2048
====

Quick day project to practice with ReactJS.

Use the arrow keys to play.

The game supports a bot plugin through an HTTP hook. When the "Play" button is
pushed, a series of POST requests will be issued to the provided URL. Each
request will contain the cells represented as an array of integers (left to
right, top to bottom), the current score, and the length of one side of the
board in JSON format. A response is expected in JSON format with one integer
field "move" representing the desired next move. 0 is left, 1 is up, 2 is
right, 3 is down. All other responses will be ignored.
