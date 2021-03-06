class UsersController < ApplicationController
  before_action :authenticate_user!
  def index
    @resource = User.find_by(id: params[:id])
    @users = User.all
    if params[:name_key]
      @users = User.where('name LIKE ?', "%#{params[:name_key]}%")
    else
      @users = User.all
    end
  end

  def show
    @user = User.find_by(id: params[:id])
    @articles = @user.articles.all.order(created_at: :desc)
  end

  def likes
    @user = User.find_by(id: params[:id])
    @likes = Like.where(user_id: @user.id)
    @article = Article.all
  end

  def following
    @user  = User.find(params[:id])
    @users = @user.following_user
    render 'show_follow'
  end

  def followers
    @user  = User.find(params[:id])
    @users = @user.follower_user
    render 'show_follower'
  end

end