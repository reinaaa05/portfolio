class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable

  mount_uploader :image, ImageUploader
  has_many :articles, dependent: :destroy
  has_many :comments
  def articles
    return Article.where(user_id: self.id)
  end
end
