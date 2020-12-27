class Article < ApplicationRecord
  validates :image, {presence: true}
 
  belongs_to :user
  has_many :comments, dependent: :destroy
  mount_uploader :image, ImagesUploader
  mount_uploader :image2, ImagesUploader
  mount_uploader :image3, ImagesUploader
  mount_uploader :image4, ImagesUploader
  mount_uploader :image5, ImagesUploader
  has_many :follower, class_name: "Relationship", foreign_key: "follower_id", dependent: :destroy # フォロー取得
  has_many :followed, class_name: "Relationship", foreign_key: "followed_id", dependent: :destroy # フォロワー取得
  has_many :following_user, through: :follower, source: :followed # 自分がフォローしている人
  has_many :follower_user, through: :followed, source: :follower # 自分をフォローしている人

  def user
    return User.find_by(id: self.user_id)
  end

    def follow(user_id)
    follower.create(followed_id: user_id)
  end
  
  # ユーザーのフォローを外す
  def unfollow(user_id)
    follower.find_by(followed_id: user_id).destroy
  end
  
  # フォローしていればtrueを返す
  def following?(user)
    following_user.include?(user)
  end
end
