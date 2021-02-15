class HelloController < ApplicationController
  protect_from_forgery
  def index
    @header = 'layout sample'
    @footer ='copyright SYODA-Tuyano 2020'
    @title = 'New Layout'
    @msg = 'this is sample page!'
  end
end
