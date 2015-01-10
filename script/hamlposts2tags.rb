# ~/x611/script/hamlposts2tags.rb

# This script should loop through 
# ~/x611/app/views/posts/
# and look for tags in each HAML file.

# If I find a tag,
# I should make note of the HAML file name.
# Then I should make note of the tag.
# Then, in /tmp/, I should make a 2nd HAML file with the tag in it.
# The tag will be a link to the 1st HAML file.
# The name of this 2nd HAML file should be built from the tag.

# Next, if the tag is Rails, I should append the tag-link to
# ~/x611/app/views/tags/_rails.haml

require 'tempfile'

tagdir   = "#{Rails.root}/app/views/tags"
adir = Dir["#{Rails.root}/app/views/posts/*.haml"]
adir.each{ |fn|
  # I should stage my edits in tmpfile
  tmpfile = Tempfile.new('tmp.haml')
  # I should flag if any tags in this file have been linkized.
  linkized = false
  # I should note the href of this post.
  hrefp = fn.sub(/^.*\/posts\//,'/posts/').sub(/.haml$/,'')
  # Later I will build an anchor pointing to this post.
  # If this post has a question, 
  # later I should set acont to the question string.
  # Until then, I should give anchor content a default value.
  acont = hrefp
  File.open(fn, 'r') do |afile|
    afile.each_line{ |line| 
      # I should look for a both a question and tags in this file.
      # The question should come before any tags.
      # A question should look like this:
      # .q2 In Rails how do I implement a wildcard route?
      acont = line.sub(/\.q2/,'') if line =~ /^.q2 /

      # A tag can look like this:
      #   %a.xtag(href='/tags/rails') rails
      if line =~ /(^  %a.xtag.href=)(.+tags.)(.+)('.+)/
        # I should make a note of the tag string:
        tagstring = $3
        # I should build an anchor-elem and write it.
        fn2 = "#{tagdir}/_#{tagstring}.haml"
        fh = File.open(fn2, 'a+')
        fh.puts("%a(href='#{hrefp}') #{acont}")
        fh.close
      end #if 

      # Also, A tag can look like this:
      #   .tag Rails
      if line =~ /^  \.tag /
        # I should make a note of the tag string:
        tagstring = line.sub(/^  .tag /,'').gsub(/ /,'_').chomp.downcase
        # I should build an anchor-elem and write it.
        fn2 = "#{tagdir}/_#{tagstring}.haml"
        fh = File.open(fn2, 'a+')
        fh.puts("%a(href='#{hrefp}') #{acont}")
        fh.close
        # Now I should linkize line.
        line = "  %a.xtag(href='/tags/#{tagstring}') #{tagstring}"
        # I should note fn was linkized
        linkized = true
      end # if
      tmpfile.puts line
    } # afile.each_line
  end # File.open
  tmpfile.close
  # I should overwrite fn if I linkized any tags.
  FileUtils.mv(tmpfile.path, fn) if linkized
} # adir.each
