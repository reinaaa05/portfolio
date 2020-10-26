class CreateShops < ActiveRecord::Migration[5.2]
  def change
    create_table :shops do |t|
      t.integer :category_id
      t.string :name
      t.string :address

      t.timestamps
    end
  end
end
