# ~/x611/script/dirtags2haml.rb

# I use this script to copy filenames from 
# app/views/tags into app/views/posts/tags.haml

require 'tempfile'

tfh = Tempfile.new('tmp.haml')
adir = Dir["#{Rails.root}/app/views/tags/_*.haml"]
adir.sort.each{ |fn|
  # I should get anchor content
  acont = fn.sub(/\/.*tags\/_/,'').sub(/.haml$/,'')
  hrefp = "/tags/#{acont}"
  tfh.puts "%a(href='#{hrefp}') #{acont}"
}

tfh.close
FileUtils.mv(tfh.path, "#{Rails.root}/app/views/posts/_tags.haml")
