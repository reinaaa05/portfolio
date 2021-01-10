class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable
  mount_uploader :user_image, ImagesUploader
  mount_uploader :icon_image, ImagesUploader

  def posts
    return Post.where(user_id: self.id)
  end
end
