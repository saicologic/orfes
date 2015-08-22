#!/usr/bin/env ruby
require 'osc-ruby' # osc-rubyのロード
require 'osc-ruby/em_server' # EventMachineサーバーのロード
require 'pry'
server = OSC::EMServer.new(6666)
server.add_method '/sensorValues' do |message|
  # puts "Address: #{message.address} --  Message: #{message.to_a}"
  # binding.pry
  m = message.to_a

  # case m[0]
  # when 0
  #   left_x = m[8]
  #   left_y = m[9]
  #   left_z = m[10]
  # when 1
  #   right_x = m[8]
  #   right_y = m[9]
  #   right_z = m[10]
  # end
  # binding.pry
  # puts "LEFT: #{left_x}, #{left_y}, #{left_z}"
  # puts "RIGTH: #{right_x}, #{right_y}, #{right_z}"
  if m[0] == 0
    puts m[8], m[9], m[10]
  end
end
server.run
