class RelationshipsController < ApplicationController
  def follow
    current_user.follow(params[:id])
    @user = User.find_by(id: params[:id])
    redirect_back(fallback_location: article_path)
  end
  
  def unfollow
    current_user.unfollow(params[:id])
    @user = User.find_by(id: params[:id])
    redirect_back(fallback_location: article_path)
  end
end
