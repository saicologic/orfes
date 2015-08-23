from flask import Flask
from flask import request
from orphe import Orphe

app = Flask(__name__)
orphe = Orphe('127.0.0.1', 7777)

@app.route("/estimote/beacon")
def message():
    color = request.args.get('color')
    print color
    if color == 'red':
        orphe.flicker_color1('left', 255, 0, 0)
        orphe.flicker_color1('right', 255, 0, 0)
    elif color == 'green':
        orphe.flicker_color1('left', 0, 255, 0)
        orphe.flicker_color1('right', 0, 255, 0)
    elif color == 'blue':
        orphe.flicker_color1('left', 0, 0, 255)
        orphe.flicker_color1('right', 0, 0, 255)
    elif color == 'yellow':
        orphe.flicker_color1('left', 255, 255, 0)
        orphe.flicker_color1('right', 255, 255, 0)
    return color

if __name__ == "__main__":
    app.run('0.0.0.0')
