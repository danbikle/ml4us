# spec/features/chrome_spec.rb
# Demo:
# bin/rspec spec/features/chrome_spec.rb
require 'rails_helper'

describe 'This should start Chrome', :js => true do
  it 'should start Chrome' do
    visit '/about/index'
    # I should briefly see Chrome; then it should exit.
  end
end
