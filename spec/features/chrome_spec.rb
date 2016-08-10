# spec/features/chrome_spec.rb
# Demo:
# bin/rspec spec/features/chrome_spec.rb

# I should have executable:
# chromedriver
# in my path.
# I put it here: ~/bin/chromedriver

require 'rails_helper'

describe 'This should start Chrome', :js => true do
  it 'should start Chrome' do
    visit '/about'
    visit '/blog'
    visit '/contact'
    visit '/cclasses/class01'
    visit '/cclasses/class02'
    visit '/cclasses/class03'
    # I should briefly see Chrome; then it should exit.
  end
end
