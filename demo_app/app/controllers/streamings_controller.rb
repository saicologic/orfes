class StreamingsController < ApplicationController
  protect_from_forgery :except => :message
  include ActionController::Live
   # 接続中のクライアント一覧を格納する配列
  @@streams ||= []
  #@@colors = ['red','green','blue','yellow']
  def index 	
  end

  def message
    @@streams.each_with_index do |stream,i|
      stream.write(data: params) rescue nil
      logger.debug(i)
    end
    render text: nil
	end

  # SSE接続用アクション
  def stream
    response.headers['Content-Type'] = 'text/event-stream'
    sse = SSE.new(response.stream, retry: 300, event: "push")
    @@streams.push(sse)
    # 20秒おきにクライアントへダミー送信
    loop do
      response.stream.write(":ping ¥n¥n")
      sleep 15
    end
  rescue IOError
  ensure
    @@streams.delete(response.stream)
    response.stream.close
  end

  def estimote
    render :action => "estimote"
  end

  def control
    render :action => "control"
  end

  def destroy
    @@streams.delete(response.stream)
    response.stream.close
  end
end
