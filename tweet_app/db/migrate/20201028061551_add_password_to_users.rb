class AddPasswordToUsers < ActiveRecord::Migration[5.2]
  def change
    add_column :users, :passsword, :string
    change_column :users, :password, :string
  end
end
