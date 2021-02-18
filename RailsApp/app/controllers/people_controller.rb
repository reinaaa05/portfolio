class PeopleController < ApplicationController
  layout 'people'
  def index
    @msg = 'Person data.'
    @data = Person.all
  end

  def show
    @msg = "Indexed data."
    @data = Person.find(params[:id])
  end

  def add
    @msg = "add new data."
    @person = Person.new
  end

  def create
    if request.post?
      Person.create(person_params)
    end
    redirect_to '/people'
  end

  def edit
    @msg = "edit data.[id = " + params[:id] + "]"
    @person = Person.find(params[:id])
  end

  def update
    obj = Person.find(params[:id])
    obj.update(person_params)
    redirect_to '/people'
  end

  def delete
    obj = Person.find(params[:id])
    obj.destroy
    redirect_to '/people'
  end

  def find
    @msg = 'please type search word...'
    @people = Array.new 
    if request.post?
      f = params[:find].split(',')
      @people = Person.all.limit(f[0]).offset(f[1])
    else
      @people = Person.all
    end
  end

  private
  def person_params
    params.require(:person).permit(:name, :age, :mail)
  end
end
