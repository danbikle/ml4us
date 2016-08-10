# spec/features/chrome_spec.rb
# Demo:
# bin/rspec spec/features/chrome_spec.rb

# I should have executable:
# chromedriver
# in my path.
# I put it here: ~/bin/chromedriver

require 'rails_helper'

describe 'This should start Chrome', :js => true do
  it 'should visit some links' do
    visit '/about'
    sleep 1
    visit '/blog'
    sleep 1
    visit '/contact'
    sleep 1
    visit '/cclasses/class01'
    sleep 1
    visit '/cclasses/class01at'
    sleep 1
    visit '/cclasses/class01ch'
    sleep 1
    visit '/cclasses/class01cp'
    sleep 1
    visit '/cclasses/class01ml'
    sleep 1
    visit '/cclasses/class01ova'
    sleep 1
    visit '/cclasses/class01rl'
    sleep 1
    visit '/cclasses/class01rs2'
    sleep 1
    visit '/cclasses/class01rs'
    sleep 1
    visit '/cclasses/class01sl'
    sleep 1
    visit '/cclasses/class01td'
    sleep 1
    visit '/cclasses/class01uc'
    sleep 1
    visit '/cclasses/class01vb'
    sleep 1
    visit '/cclasses/class02'
    sleep 1
    visit '/cclasses/class03'
    sleep 1
    # I should see Chrome; then it should exit.
  end
end



