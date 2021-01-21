class Post < ApplicationRecord
  validaites :title, presence:true, length {minmum: 3, messege: 'Too short to post!' }
  validaites :body, presence: true
end
