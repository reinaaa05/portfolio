class RelationshipsController < ApplicationController
  def follow
    current_user.follow(params[:id])
    @user = User.find_by(id: params[:id])
    redirect_to("/users")
  end
  
  def unfollow
    current_user.unfollow(params[:id])
    @user = User.find_by(id: params[:id])
    redirect_to("/users")
  end
end
