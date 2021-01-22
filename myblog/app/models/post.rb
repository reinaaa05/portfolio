class Post < ApplicationRecord
  has_many :comments, dependent: :destroy
  validates :title, presence: true, length: { minimum: 3, messege: 'Too short to post!' }
  validates :body, presence: true
end
