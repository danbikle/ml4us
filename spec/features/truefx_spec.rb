# spec/features/truefx_spec.rb
# Demo:
# bin/rspec spec/features/truefx_spec.rb

# I should have executable:
# chromedriver
# in my path.
# I put it here: ~/fx411/bin/chromedriver

require 'rails_helper'

describe 'This should start Chrome', :js => true do
  it 'should visit some links' do
    Capybara.app_host = 'https://www.truefx.com'
    ahost             = Capybara.app_host
    visit '/'
    sleep 1
    find(:xpath, "//a[@href='?page=logina']").click
    sleep 1
    within("#login-form") do
      fill_in 'USERNAME', with: 'bobsmithIV'
      sleep 1
      fill_in 'PASSWORD', with: 'eurosDOLLASy3n'
      sleep 1
      click_on 'Login'
      sleep 1
    end
    years_a    = [2010,2011,2012,2013,2014,2015,2016,2017]
    months_s_a = ['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    pairs_a    = ['AUDUSD','EURUSD','GBPUSD','USDCAD','USDJPY']
    for yr_i       in years_a    do
      for month_s  in months_s_a do
        for pair_s in pairs_a    do
          click_link('Downloads')
          sleep 2
          click_link(String(yr_i))
          sleep 2
          click_link(month_s.capitalize)
          sleep 2
          click_link(pair_s)
          sleep 33
        end
      end
    end
    
    # logout
    find(:xpath, "//a[@href='?page=logout']").click
    sleep 1
  end
end
