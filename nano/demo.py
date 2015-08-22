import rtmidi_python as rtmidi
import OSC
import requests
import json

midi_in = rtmidi.MidiIn()
midi_in.open_port(0)

client = OSC.OSCClient()

def flash_color(r, g, b):
    print r, g, b
    msg = OSC.OSCMessage()
    msg.setAddress("/flashColor")
    msg.append(0)
    msg.append(r)
    msg.append(g)
    msg.append(b)
    client.sendto(msg, ('127.0.0.1', 7777))

def roll_color(r, g, b):
    print r, g, b
    msg = OSC.OSCMessage()
    msg.setAddress("/rollColor")
    msg.append(0)
    msg.append(r)
    msg.append(g)
    msg.append(b)
    client.sendto(msg, ('127.0.0.1', 7777))

def push_to_web(action, device, rgb):

    data = {
        'action': action,
        'device': device,
        'rgb': rgb
    }

    params = json.dumps(data)
    print params
    # r = requests.get('http://c0161b1c.ngrok.io/Streamings/message', params=params)
    # print r


while True:
    message, delta_time = midi_in.get_message()
    if message:
        _id, _type, _level = message
        event_id = ''
        print _id, _type, _level

        # up 3 botton
        if _type == 18:
            if _id == 144:
                flash_color(255, 0, 0)

        if _type == 20:
            if _id == 144:
                flash_color(0, 255, 0)

        if _type == 22:
            if _id == 144:
                flash_color(0, 0, 255)

        # up 3 button
        if _type == 30:
            if _id == 144:
                roll_color(255, 0, 0)

        if _type == 32:
            if _id == 144:
                roll_color(0, 255, 0)

        if _type == 34:
            if _id == 144:
                roll_color(0, 0, 255)

        # down left
        if _type == 12:
            if _id == 144:
                print 'red'
                push_to_web('kick', 'left', [0, 0, 0])
                flash_color(255, 0, 0)
                # roll_color(255, 0, 0)

        if _type == 14:
            if _id == 144:
                print 'green'
                push_to_web('kick', 'left', [0, 255, 0])
                flash_color(0, 255, 0)
                # roll_color(0, 255, 0)

        if _type == 16:
            if _id == 144:
                print 'blue'
                push_to_web('kick', 'left', [0, 0, 255])
                flash_color(0, 0, 255)
                # roll_color(0, 0, 255)
