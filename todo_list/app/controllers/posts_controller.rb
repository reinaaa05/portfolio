class PostsController < ApplicationController
  def index
    @post = Post.all
  end

  def create
    @post = Post.new(content: params[:content])
    @post.save
    redirect_to("/")
  end

  def edit
    @post = Post.find_by(id: params[:id])
  end
  
  def update
    @post = Post.find_by(id: params[:id])
    @post.content = params[:content]
    @post.save
    redirect_to("/")
  end
  
  def destroy
    @post = Post.find_by(id: params[:id])
    @post.destroy
    redirect_to("/")
  end

end
