class AddImage3ToArticles < ActiveRecord::Migration[5.2]
  def change
    add_column :articles, :image3, :string
  end
end
