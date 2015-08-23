import OSC

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
