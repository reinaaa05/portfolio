class AddImage5ToArticles < ActiveRecord::Migration[5.2]
  def change
    add_column :articles, :image5, :string
  end
end
