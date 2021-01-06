class Post < ApplicationRecord
mount_uploader :posts_image, ImagesUploader
  belongs_to :user
  has_many :materials
  accepts_nested_attributes_for :materials, allow_destroy: true
end
