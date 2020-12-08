Rails.application.routes.draw do
  resources :articles  do
    resources :comments, only: [:create,:destroy, :index]
  end
  devise_for :users
  get 'welcome/index'
  root 'welcome#index'
  get "/users" => "users#index"
  get "users/:id" => "users#show"
  get "users/:id/likes" => "users#likes"
  post "likes/:article_id/create" => "likes#create"
  post "likes/:article_id/destroy" => "likes#destroy"
  
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
