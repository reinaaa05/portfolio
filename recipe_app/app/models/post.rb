class Post < ApplicationRecord
mount_uploader :posts_image, ImagesUploader
  belongs_to :user
  has_many :foods, inverse_of: :post
  has_many :comments
  accepts_nested_attributes_for :foods, allow_destroy: true, update_only: true
  has_many :recipes, inverse_of: :post
  accepts_nested_attributes_for :recipes, allow_destroy: true, update_only: true
  
  def user
    return User.find_by(id: self.user_id)
  end

 
end
