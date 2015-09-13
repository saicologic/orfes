Rails.application.routes.draw do
  get 'streamings/index'
  get 'streamings/estimote'
  get 'streamings/control'

  get 'streamings/stream'  
  post 'streamings/message'

  root to: "streamings#index"
end
