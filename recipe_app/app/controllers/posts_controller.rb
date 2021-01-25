class PostsController < ApplicationController
  before_action :authenticate_user!
  before_action :set_post, only: [:show, :edit, :update, :destroy]

  # GET /posts
  # GET /posts.json
  def index
    @posts = Post.all
    
  end

  # GET /posts/1
  # GET /posts/1.json
  def show
    @likes_count = Like.where(post_id:@post.id).count
    @comments = @post.comments
    @comment = Comment.new
    @comment_count = Comment.where(post_id:@post.id).count
  end

  # GET /posts/new
  def new
    @post = Post.new
    @food = @post.foods.build
    @recipe = @post.recipes.build
  end

  # GET /posts/1/edit
  def edit
  end

  # POST /posts
  # POST /posts.json
  def create
    @post = Post.new(post_params)
    @post.user_id = current_user.id
    respond_to do |format|
      if @post.save
        format.html { redirect_to @post, notice: '作成しました' }
        format.json { render :show, status: :created, location: @post }
      else
        format.html { render :new }
        format.json { render json: @post.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /posts/1
  # PATCH/PUT /posts/1.json
  def update
    if @post.user_id == current_user.id
      respond_to do |format|
        if @post.update(post_params)
          format.html { redirect_to @post, notice: '編集しました.' }
          format.json { render :show, status: :ok, location: @post }
        else
          format.html { render :edit }
          format.json { render json: @post.errors, status: :unprocessable_entity }
        end
    end
    else
      redirect_to @post, notice: "権限がありません."
    end
  end

  # DELETE /posts/1
  # DELETE /posts/1.json
  def destroy
    if @post.user_id == current_user.id
      @post.destroy
      msg = "削除しました"
    else
      msg = "権限がありません"
    end
      respond_to do |format|
        format.html { redirect_to posts_url, notice: msg }
        format.json { head :no_content }
      end
  end

  def ranking
    @posts = Post.all.order(created_at: :desc)
    render 'ranking'
  end

  def search
    @posts = Post.all.order(created_at: :desc)
    if params[:id_keyword].present?
      @posts = Post.where(id: params[:id_keyword] )
    else
      @posts = Post.all.order(created_at: :desc)
    end

    
    if params[:keyword].present?
      keywords = params[:keyword].split(/[[:blank:]]+/) # 空白で分割
      @posts = [] 
      keywords.each do |keyword|
        next if keyword == "" 
        @posts += Post.joins(:foods).where(["name LIKE ? OR content LIKE ? OR m_name LIKE ?", "%#{keyword}%", "%#{keyword}%", "%#{keyword}%"])
      end 
      @posts.uniq!
      if params[:notkeyword].present?
        notkeywords = params[:notkeyword].split(/[[:blank:]]+/)
        minus_posts = [] 
        notkeywords.each do |notkeyword|
          next if notkeyword == "" 
          minus_posts += Post.joins(:foods).where(["name LIKE ? OR content LIKE ? OR m_name LIKE ?", "%#{notkeyword}%", "%#{notkeyword}%", "%#{notkeyword}%"])
        end
        minus_posts.each do |minus_post| 
          @posts.delete(minus_post) 
        end 
      end
    else
      if params[:notkeyword].present?
        notkeywords = params[:notkeyword].split(/[[:blank:]]+/)
        notkeywords.each do |notkeyword|
          next if notkeyword.blank?
        @posts = Post.joins(foods).where.not(["post.name LIKE ? OR post.content LIKE ? OR foods.m_name LIKE ?", "%#{notkeyword}%", "%#{notkeyword}%", "%#{notkeyword}%"]).references(:foods).uniq
        end
      else
        @posts = Post.all
      end
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_post
      @post = Post.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def post_params
      params.require(:post).permit(:user_id, :name, :posts_image, :content, :point, :comment, foods_attributes: [:id, :m_name, :m_amount, :_destroy], recipes_attributes: [:id, :process, :process_image, :_destroy])
    end
end
