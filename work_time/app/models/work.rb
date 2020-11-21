  class Work < ApplicationRecord
  belongs_to :category

  enum category_id: { "出品": 0, "価格メンテ": 1, "在庫メンテ": 2, "発送": 3, other: 9 }
  
  # 日付による絞り込み
  scope :get_by_date, ->(date) {
  where("date like ?", "%#{date}%")
  }
  # 業務内容による絞り込み
  scope :get_by_category_id, ->(category_id) {
  where(category_id: category_id)
  }
  end