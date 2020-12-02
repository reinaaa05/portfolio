class AddImage2ToArticle < ActiveRecord::Migration[5.2]
  def change
    add_column :articles, :image2, :string
  end
end
