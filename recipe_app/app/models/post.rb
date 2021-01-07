class Post < ApplicationRecord
mount_uploader :posts_image, ImagesUploader
  belongs_to :user
  has_many :materials, inverse_of: :post
  accepts_nested_attributes_for :materials, allow_destroy: true, update_only: true
  def material
    return Material.find_by(id: self.materials_id)
  end
  
  def user
    return User.find_by(id: self.user_id)
  end
end
