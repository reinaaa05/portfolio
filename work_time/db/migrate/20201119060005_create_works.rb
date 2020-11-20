class CreateWorks < ActiveRecord::Migration[5.2]
  def change
    create_table :works do |t|
      t.date :date
      t.integer :category_id
      t.integer :count

      t.timestamps
    end
  end
end
