class AddImageNameToCategories < ActiveRecord::Migration[5.2]
  def change
    add_column :categories, :image_name, :string
  end
end
