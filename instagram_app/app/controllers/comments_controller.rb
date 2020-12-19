class CommentsController < ApplicationController
   before_action :authenticate_user!
  def index
    @article = Article.find_by(id: params[:id])
    @comments = Comment.all
    @comment = Comment.new
  end

  def create
    @article = Article.find(params[:article_id])
    @comment = @article.comments.new(comment_params)
    @comment.user_id = current_user.id
    if @comment.save
      redirect_back(fallback_location: root_path)
    else
      redirect_back(fallback_location: root_path)
    end
  end

  def destroy
    @comment = Comment.find(params[:id])
    @comment.destroy
    redirect_to articles_path
  end

  private

  def comment_params
    params.require(:comment).permit(:content)
  end
end
