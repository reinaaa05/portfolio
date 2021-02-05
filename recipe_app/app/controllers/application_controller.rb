class ApplicationController < ActionController::Base
  before_action :configure_permitted_parameters, if: :devise_controller?

  def after_sign_in_path_for(resource)
    posts_path # ログイン後に遷移するpathを設定
  end
protected

def configure_permitted_parameters
  devise_parameter_sanitizer.permit(:sign_up, keys: [:name])
  devise_parameter_sanitizer.permit(:account_update, keys: [:name])
  devise_parameter_sanitizer.permit(:sign_up, keys: [:user_image])
  devise_parameter_sanitizer.permit(:account_update, keys: [:user_image])
  devise_parameter_sanitizer.permit(:sign_up, keys: [:content])
  devise_parameter_sanitizer.permit(:account_update, keys: [:content])
  devise_parameter_sanitizer.permit(:sign_up, keys: [:icon_image])
  devise_parameter_sanitizer.permit(:account_update, keys: [:icon_image])
end

end
