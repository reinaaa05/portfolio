class AddImage4ToArticles < ActiveRecord::Migration[5.2]
  def change
    add_column :articles, :image4, :string
  end
end
