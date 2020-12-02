class Article < ApplicationRecord
  belongs_to :user
  mount_uploader :image, ImagesUploader
  mount_uploader :image2, ImagesUploader
  mount_uploader :image3, ImagesUploader
  mount_uploader :image4, ImagesUploader
  mount_uploader :image5, ImagesUploader

  def user
    return User.find_by(id: self.user_id)
  end
end
