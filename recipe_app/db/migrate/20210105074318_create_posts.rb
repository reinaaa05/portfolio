class CreatePosts < ActiveRecord::Migration[6.1]
  def change
    create_table :posts do |t|
      t.integer :user_id
      t.string :name
      t.string :posts_image
      t.text :content
      t.text :point

      t.timestamps
    end
  end
end
