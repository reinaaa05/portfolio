class CreatePictures < ActiveRecord::Migration[5.2]
  def change
    create_table :pictures do |t|
      t.integer :article_id
      t.string :photo

      t.timestamps
    end
  end
end
