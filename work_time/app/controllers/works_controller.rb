class WorksController < ApplicationController
  before_action :set_work, only: [:show, :edit, :update, :destroy]
  before_action :authenticate_user!

  # GET /works
  # GET /works.json
  def index
    if params[:name_key] || params[:category_key]
      @works = Work.where('user_id LIKE ?', "%#{params[:name_key]}%").where('date LIKE ?', "%#{params[:date_key]}%").where('category_id LIKE ?', "%#{params[:category_key]}%")
    else
      @works = Work.all
    end
 
  end
     # パラメータとして名前か性別を受け取っている場合は絞って検索する
  #if params[:date].present?
   # @works = @works.get_by_date params[:date]
  #end
   # if params[:category_id].present?
    #@works = @works.get_by_category_id params[:category_id]
  #end
  

  # GET /works/1
  # GET /works/1.json
  def show
  end

  # GET /works/new
  def new
    @work = Work.new
  end

  # GET /works/1/edit
  def edit
  end

  # POST /works
  # POST /works.json
  def create
    @work = Work.new(work_params)
    @work.user_id = current_user.id
    respond_to do |format|
      if @work.save
        format.html { redirect_to @work, notice: 'Work was successfully created.' }
        format.json { render :show, status: :created, location: @work }
      else
        format.html { render :new }
        format.json { render json: @work.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /works/1
  # PATCH/PUT /works/1.json
  def update
    if @article.user_id == current_user.id
      respond_to do |format|
        if @work.update(work_params)
          format.html { redirect_to @work, notice: 'Work was successfully updated.' }
          format.json { render :show, status: :ok, location: @work }
        else
          format.html { render :edit }
          format.json { render json: @work.errors, status: :unprocessable_entity }
        end
      end
    else
      redirect_to @article, notice: "You don't have permission."
    end
  end

  # DELETE /works/1
  # DELETE /works/1.json
  def destroy
    if @article.user_id == current_user.id
       @work.destroy
       msg = "Article was successfully destroyed."
       else
         msg = "You don't have permission."
       end
    respond_to do |format|
      format.html { redirect_to works_url, notice: msg }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_work
      @work = Work.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def work_params
      params.require(:work).permit(:date, :category_id, :count)
    end

  
end
