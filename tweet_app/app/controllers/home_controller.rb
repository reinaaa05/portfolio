class HomeController < ApplicationController
  before_action :forbid_login_user,{onry:[:top]}
  def top
  end

  def about
  end
end
