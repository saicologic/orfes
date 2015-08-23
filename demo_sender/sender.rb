#!/usr/bin/env ruby
require 'osc-ruby'
require 'osc-ruby/em_server'
require 'uri'
require 'faraday'
require 'pry'
require 'net/http'

server = OSC::EMServer.new(6666)
client = OSC::Client.new('localhost', 7777)

# #グラデーションのテスト
# client.send(OSC::Message.new('/baseColorMode', 0, 1))
# client.send(OSC::Message.new('/baseColorMode', 1, 1))

#キックの光基本設定
client.send(OSC::Message.new('/moveFlashColorModulation', 0, 100, 100, 100))
client.send(OSC::Message.new('/moveFlashColorModulation', 1, 100, 100, 100))


class Orphe
  attr_accessor :acc_x, :acc_y, :acc_z, :gyro_x, :gyro_y, :gyro_z
  def initialize
    @device = nil
    @acc_length = 0.0
    @gyro_length = 0.0
    @acc_x = 0.0
    @acc_y = 0.0
    @acc_z = 0.0
    @gyro_x = 0.0
    @gyro_y = 0.0
    @gyro_z = 0.0
  end

  def get_acc_length(m)

    @acc_x = m[8]
    @acc_y = m[9]
    @acc_z = m[10]
    @acc_length = @acc_x + @acc_y + @acc_z
    @acc_length
  end

  def get_gyro_length(m)
    @gyro_x = m[11]
    @gyro_y = m[12]
    @gyro_z = m[13]
    @gyro_length = @gyro_x + @gyro_y + @gyro_z
    @gyro_length
  end
end

class LeftOrphe < Orphe;
  def initialize
    @device = "left"
    super
  end
end

class RightOrphe < Orphe;
  def initialize
    @device = "right"
    super
  end
end

# 初期化
left_orphe = LeftOrphe.new
right_orphe = RightOrphe.new

left_step =0
left_kick =0

right_step =0
right_kick =0

jump = 0
count = 0

# puts right_orphe.acc_z
# right_orphe.acc_z = 1.1
# puts right_orphe.acc_z

def send_motion(motion, color)
  query = "action=left&motion=kick&color=#{color}&motion=#{motion}"
  uri = URI.parse("http://172.16.201.161:9292/streamings/message?#{query}")
  http = Net::HTTP.new(uri.host, uri.port)
  req = Net::HTTP::Post.new(uri.request_uri) #があるとして
  req["Content-Type"] = "text/event-stream"
  res = http.request(req)
  print res
  res
end

# def send_motion(action, motion)
#   query = "action=#{action}&motion=kick&motion=#{motion}"
#   url = "http://172.16.201.161:9292/streamings/message?#{query}"
#   conn = Faraday::Connection.new(:url => url) do |c|
#     c.adapter :em_synchrony
#   end
#   resp = conn.post do |req|
#     req.url url
#       req.headers['Content-Type'] = "text/event-stream"
#   end
#   resp
# end

# binding.pry

server.add_method '/sensorValues' do |message|
  # puts "Address: #{message.address} --  Message: #{message.to_a}"
  m = message.to_a

  case m[0]
  when 0
    left_orphe.get_acc_length(m)
    left_orphe.get_gyro_length(m)
  when 1
    right_orphe.get_acc_length(m)
    right_orphe.get_gyro_length(m)
  end

# puts "LEFT: #{left_x}, #{left_y}, #{left_z}"
# puts "RIGTH: #{right_x}, #{right_y}, #{right_z}"
# puts "acc-x = #{m[8]}", "acc-y = #{m[9]}", "acc-z = #{m[10]}"
# puts "gyro-x = #{m[11]}", "gyro-y = #{m[12]}","gyro-z = #{m[12]}"
# puts "right_orphe.acc_x = #{right_orphe.acc_x}"
# puts "m[8] = #{m[8]}"

  #ジャンプは緑
  if (right_orphe.acc_z - left_orphe.acc_z) < 0.5 && right_orphe.acc_z > 0.3 && left_orphe.acc_z > 0.3
    jump += 1
    puts "#{count} jump = #{jump}"
    client.send(OSC::Message.new('/FlashColor', 0, 0, 204, 0))
    client.send(OSC::Message.new('/FlashColor', 1, 0, 204, 0))
    send_motion('left', 'jump')
    # send_motion('right', 'jump')
    sleep 0.3
    next
  end

  #ステップは黄色いフラッシュ
  case m[0]
  when 0
    if left_orphe.acc_z > 0.3 && left_orphe.get_gyro_length(m) <0.05
      left_step += 1
      puts "#{count} left_step = #{left_step}"
      client.send(OSC::Message.new('/flashColor', 0, 170, 240, 0))
      send_motion('left', 'step')
      sleep 0.1
      next
    end
  when 1
    if right_orphe.acc_z > 0.3 && right_orphe.get_gyro_length(m) <0.05
      right_step += 1
      puts "#{count} right_step = #{right_step}"
      client.send(OSC::Message.new('/flashColor', 1, 170, 240, 0))
      send_motion('right', 'step')
      sleep 0.1
      next
    end
  end

  #キックは赤いフラッシュ
  case m[0]
  when 0
    if left_orphe.get_acc_length(m) > 0.3 && left_orphe.gyro_z > 0.05
      left_kick += 1
      puts "#{count} left_kick = #{left_kick}"
      client.send(OSC::Message.new('/flashColor', 0, 204, 0, 0))
      send_motion('left', 'kick')
      sleep 0.1
      next
    end
  when 1
    if right_orphe.get_acc_length(m) > 0.3 && right_orphe.gyro_z > 0.05
      right_kick += 1
      puts "#{count} right_kick = #{right_kick}"
      client.send(OSC::Message.new('/flashColor', 1, 204, 0, 0))
      send_motion('right', 'kick')
      sleep 0.1
      next
    end
  end

  count +=1
  # puts count
end

server.run
