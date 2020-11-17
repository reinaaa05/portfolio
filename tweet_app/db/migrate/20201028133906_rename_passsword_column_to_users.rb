class RenamePassswordColumnToUsers < ActiveRecord::Migration[5.2]
  def change
    rename_column :users, :passsword, :password
  end
end
