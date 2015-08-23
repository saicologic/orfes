import rtmidi_python as rtmidi
import OSC
import requests
import json
from orphe import Orphe

def push_to_web(color):
    message = 'device=kick&action=left&color=' + color
    print message
    # r = requests.post('http://172.16.201.161:9292/streamings/message?' + message, params=message, headers= { 'Content-Type': 'text/event-stream'})
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
                orphe.flicker_color1('left', 255, 0, 0)
                orphe.flicker_color1('right', 255, 0, 0)
                # pass
                # flash_color(255, 0, 0)

        if _type == 20:
            if _id == 144:
                orphe.flicker_color1('left', 0, 255, 0)
                orphe.flicker_color1('right', 0, 255, 0)
                pass
                # flash_color(0, 255, 0)

        if _type == 22:
            if _id == 144:
                orphe.flicker_color1('left', 0, 0, 255)
                orphe.flicker_color1('right', 0, 0, 255)
                pass
                # flash_color(0, 0, 255)

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

        # down LED
        if _type == 12:
            if _id == 144:
                print 'red'
                orphe.flash_color('left', 255, 0, 0)
                # orphe.flicker_color1('left', 255, 0, 0)
                orphe.flash_color('right', 255, 0, 0)
                # orphe.flicker_color1('right', 255, 0, 0)
                push_to_web('red')

        if _type == 14:
            if _id == 144:
                print 'green'
                orphe.flash_color('left', 0, 255, 0)
                # orphe.flicker_color1('left', 0, 255, 0)
                orphe.flash_color('right', 0, 255, 0)
                # orphe.flicker_color1('right', 0, 255, 0)
                push_to_web('green')


        if _type == 16:
            if _id == 144:
                print 'blue'
                orphe.flash_color('left', 0, 0, 255)
                # orphe.flicker_color1('left', 0, 0, 255)
                orphe.flash_color('right', 0, 0, 255)
                # orphe.flicker_color1('right', 0, 0, 255)
                push_to_web('blue')

        if _type == 17:
            if _id == 144:
                print 'yellow'
                # orphe.flash_color('left', 0, 0, 255)
                orphe.flash_color('left', 255, 255, 0)
                # orphe.flicker_color1('left', 255, 255, 0)
                orphe.flash_color('right', 255, 255, 0)
                # orphe.flicker_color1('right', 255, 255, 0)
                push_to_web('yellow')

        if _type == 13:
            if _id == 144:
                init_0()

        if _type == 15:
            if _id == 144:
                init_255()
