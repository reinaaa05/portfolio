class AddColumnToUser < ActiveRecord::Migration[6.1]
  def change
    add_column :users, :name, :string
    add_column :users, :user_image, :string
    add_column :users, :content, :text
  end
end
