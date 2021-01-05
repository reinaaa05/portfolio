json.extract! post, :id, :user_id, :name, :posts_image, :content, :point, :created_at, :updated_at
json.url post_url(post, format: :json)
