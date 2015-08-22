import rtmidi_python as rtmidi
import OSC
import requests
import json

class Orphe:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = OSC.OSCClient()

    def device_index(self, device):
        if device == 'left':
            return 0
        elif device == 'right':
            return 1

    def flash_color(self, device, r, g, b):
        # print r, g, b
        msg = OSC.OSCMessage()
        msg.setAddress("/flashColor")
        msg.append(self.device_index(device))
        msg.append(r)
        msg.append(g)
        msg.append(b)
        self.send(msg)

    def flash_modulation(self, device, decay, fade, duration):
        # print r, g, b
        msg = OSC.OSCMessage()
        msg.setAddress("/flashModulation")
        msg.append(self.device_index(device))
        msg.append(decay)
        msg.append(fade)
        msg.append(duration)
        self.send(msg)

    def roll_color(self, device, r, g, b):
        # print r, g, b
        msg = OSC.OSCMessage()
        msg.setAddress("/rollColor")
        msg.append(self.device_index(device))
        msg.append(r)
        msg.append(g)
        msg.append(b)
        self.send(msg)

    def roll_modulation(self, device, decay, fade, duration):
        # print r, g, b
        msg = OSC.OSCMessage()
        msg.setAddress("/rollModulation")
        msg.append(self.device_index(device))
        msg.append(decay)
        msg.append(fade)
        msg.append(duration)
        self.send(msg)

    def move_flash_color(self, device, r, g, b):
        # print r, g, b
        msg = OSC.OSCMessage()
        msg.setAddress("/moveFlashColor")
        msg.append(self.device_index(device))
        msg.append(r)
        msg.append(g)
        msg.append(b)
        self.send(msg)

    def move_flash_modulation(self, device, decay, fade, duration):
        # print r, g, b
        msg = OSC.OSCMessage()
        msg.setAddress("/moveFlashModulation")
        msg.append(self.device_index(device))
        msg.append(decay)
        msg.append(fade)
        msg.append(duration)
        self.send(msg)

    def flicker_duration(self, device, duration):
        # print r, g, b
        msg = OSC.OSCMessage()
        msg.setAddress("/flickerDuration")
        msg.append(self.device_index(device))
        msg.append(duration)
        self.send(msg)

    def flicker_color1(self, device, r, g, b):
        # print r, g, b
        msg = OSC.OSCMessage()
        msg.setAddress("/flickerColor1")
        msg.append(self.device_index(device))
        msg.append(r)
        msg.append(g)
        msg.append(b)
        self.send(msg)

    def flicker_color2(self, device, r, g, b):
        # print r, g, b
        msg = OSC.OSCMessage()
        msg.setAddress("/flickerColor2")
        msg.append(self.device_index(device))
        msg.append(r)
        msg.append(g)
        msg.append(b)
        self.send(msg)

    def send(self, message):
        print message
        client = OSC.OSCClient()
        self.client.sendto(message, (self.host, self.port))

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

# Connect to MIDI
midi_in = rtmidi.MidiIn()
midi_in.open_port(0)

# Connect to Orphe
orphe = Orphe('127.0.0.1', 7777)

# Init

def init_0():
    print 'init_0'
    for device in ['left', 'right']:
        orphe.flash_color(device, 0, 0, 0)
        orphe.flash_modulation(device, 0, 0, 0)
        orphe.roll_color(device, 0, 0, 0)
        orphe.roll_modulation(device, 0, 0, 0)
        orphe.move_flash_color(device, 0, 0, 0)
        orphe.move_flash_modulation(device, 0, 0, 0)
        orphe.flicker_duration(device, 0)
        orphe.flicker_color1(device, 0, 0, 0)
        orphe.flicker_color2(device, 0, 0, 0)


def init_255():
    print 'init_255'
    for device in ['left', 'right']:
        orphe.flash_color(device, 255, 255, 255)
        orphe.flash_modulation(device, 255, 255, 255)
        orphe.roll_color(device, 255, 255, 255)
        orphe.roll_modulation(device, 255, 255, 255)
        orphe.move_flash_color(device, 255, 255, 255)
        orphe.move_flash_modulation(device, 255, 255, 255)
        orphe.flicker_duration(device, 255)
        orphe.flicker_color1(device, 255, 255, 255)
        orphe.flicker_color2(device, 255, 255, 255)

# Initialize
init_0()

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
                # push_to_web('kick', 'left', [0, 0, 0])
                orphe.flash_color('left', 255, 0, 0)
                # orphe.flash_modulation('left', 255, 255, 255)
                # orphe.flash_color('right', 255, 0, 0)
                # roll_color(255, 0, 0)


        if _type == 14:
            if _id == 144:
                print 'green'
                # push_to_web('kick', 'left', [0, 255, 0])
                # orphe.flash_color(0, 255, 0)
                # roll_color(0, 255, 0)
                orphe.flash_color('left', 0, 255, 0)
                # orphe.flash_modulation('left', 0, 255, 0)
                # orphe.flash_color('right', 0, 255, 0)


        if _type == 16:
            if _id == 144:
                print 'blue'
                # push_to_web('kick', 'left', [0, 0, 255])
                # flash_color(0, 0, 255)
                # roll_color(0, 0, 255)
                orphe.flash_color('left', 0, 0, 255)
                # orphe.flash_modulation('left', 0, 0, 255)
                # orphe.flash_color('right', 0, 0, 255)
        if _type == 13:
            if _id == 144:
                init_0()

        if _type == 15:
            if _id == 144:
                init_255()
