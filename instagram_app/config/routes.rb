Rails.application.routes.draw do
  resources :pictures
  resources :articles
  devise_for :users
  get 'welcome/index'
  root 'welcome#index'
  resources :users, only: [:index]
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
