  class Work < ApplicationRecord
  belongs_to :category
=begin
  enum category_id: { "a": 1, "b": 2, "c": 3, "d": 4 }

   # 日付による絞り込み
   scope :get_by_date, ->(date) {
    where("date like ?", "%#{date}%")
    }
    # 業務内容による絞り込み
    scope :get_by_category_id, ->(category_id) {
    where(category_id: category_id)
    }
=end

  end