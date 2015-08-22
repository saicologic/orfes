#!/usr/bin/env ruby

require 'osc-ruby'
require 'pry'

client = OSC::Client.new('localhost', 7777)
# binding.pry
# data = {
#   :left => [0, 204, 0, 0],
#   :right => [1, 0, 0, 0]
# }
# puts data[:left]
# binding.pry


client.send(OSC::Message.new('/flashColor', 0, 204, 0, 0))
client.send(OSC::Message.new('/flashColor', 1, 204, 0, 0))
# right_message = OSC::Message.new('/changeSensor', data[:left])
# client.send(message)
