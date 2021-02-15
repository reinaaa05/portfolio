class HelloController < ApplicationController
  protect_from_forgery
  def index
    if request.post? then
      @title = 'Result'
      if params['s1'] then
        @msg = 'you selected: ' + params['s1']
      else
        @msg = 'not selected...'
      end
    else
      @title = 'Index'
      @msg = 'check it...'
    end
  end

  def other
    redirect_to action: :index, params: {'msg': 'from other page'}
  end
end
