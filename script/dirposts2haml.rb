# ~/x611/script/dirposts2haml.rb

# I use this script to copy filenames from 
# app/views/posts into app/views/posts/index.haml

require 'tempfile'

tfh = Tempfile.new('tmp.haml')

filenames = Dir["#{Rails.root}/app/views/posts/*.haml"]

names_sorted_bydate = filenames.sort_by {|filename| File.mtime(filename) }

names_sorted_bydate.each{ |fn|
  # I should get anchor content
  acont = fn.sub(/\/.*posts\//,'').sub(/.haml$/,'')
  # I should create a link if filename starts with a through z.
  if acont =~ /^[a-z]/
    hrefp = "/posts/#{acont}"
    mydate = File.mtime(fn)
    tfh.puts "%a(href='#{hrefp}') #{mydate.strftime('%Y-%m-%d')} | #{acont}"
  end
}

tfh.close
FileUtils.mv(tfh.path, "#{Rails.root}/app/views/posts/_index.haml")
