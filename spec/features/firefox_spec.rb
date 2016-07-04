# spec/features/firefox_spec.rb
# Demo:
# bin/rspec spec/features/firefox_spec.rb
require 'rails_helper'
describe 'This should start Firefox', :js => true do
  it 'should start Firefox' do
    visit '/about/index'
    # I should briefly see Firefox; then it should exit.
  end
end
