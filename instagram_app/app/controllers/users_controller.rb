class UsersController < ApplicationController
  before_action :authenticate_user!
  def index
    @users = User.all
    if params[:name_key]
      @users = User.where('name LIKE ?', "%#{params[:name_key]}%")
    else
      @users = User.all
    end
  end

  def show
    @user = User.find_by(id: params[:id])
    @articles = Article.all
  end

  def likes
    @user = User.find_by(id: params[:id])
    @likes = Like.where(user_id: @user.id)
    @article = Article.all
  end
  
end