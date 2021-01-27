Rails.application.routes.draw do
  resources :posts do
    collection do
      post :confirm
    end
    resources :comments, only: [:create,:destroy]
    get 'ranking', :on => :collection
    get 'search', :on => :collection
  end
  devise_for :users
  get 'welcome/index'
  root "welcome#index"
  get "posts/ranking" => "posts#ranking"
  get "users" => "users#index"
  get "users/:id" => "users#show"
  get "users/:id/likes" => "users#likes"
  post "likes/:post_id/create" => "likes#create"
  post "likes/:post_id/destroy" => "likes#destroy"
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
end
Rails.application.routes.draw do

 end