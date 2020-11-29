class Article < ApplicationRecord
  belongs_to :user
  mount_uploader :image, ImagesUploader
  
  has_many :pictures
  accepts_nested_attributes_for :pictures
end
