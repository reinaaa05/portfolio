class Comment < ApplicationRecord
  mount_uploader :cook_image, ImagesUploader
  belongs_to :user
  belongs_to :post

end
