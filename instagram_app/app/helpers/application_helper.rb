module ApplicationHelper
  def resource_name
    :user
  end
  
  def resource
      @resource ||= User.new
      @resources || User.find_by(id: params[:id])
  end
  
  def devise_mapping
      @devise_mapping ||= Devise.mappings[:user]
  end
end
