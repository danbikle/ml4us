# spec/features/southwest_spec.rb
# Demo:
# bin/rspec spec/features/southwest_spec.rb

# I should have executable:
# chromedriver
# in my path.
# I put it here: ~/bin/chromedriver

require 'rails_helper'

describe 'This should start Chrome', :js => true do
  it 'should visit some links' do
    Capybara.app_host = 'http://www.southwest.com'
    visit '/'
    sleep 2
    visit '/flight/flight-status-select.html'
    sleep 2
    visit '/air/flight-status/results.html?destinationAirportCode=LAX&flightNumber=&originationAirportCode=SJC'
    sleep 2
    visit '/'
    sleep 2
    visit '/flight/routemap_dyn.html'
    sleep 2
    visit '/'
    sleep 2
    # I should see Chrome; then it should exit.
  end
end



