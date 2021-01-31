class Recipe < ApplicationRecord
  belongs_to :post
  mount_uploader :process_image, ImagesUploader
end
