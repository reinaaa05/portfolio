Rails.application.routes.draw do
  resources :posts do
    resources :comments, only: [:create]
    get 'ranking', :on => :collection
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
