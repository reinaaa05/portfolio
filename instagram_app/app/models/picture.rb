class Picture < ApplicationRecord
  mount_uploader :photo, PhotoUploader
  belongs_to :article
end
