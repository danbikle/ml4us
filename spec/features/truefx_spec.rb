# spec/features/truefx_spec.rb
# Demo:
# bin/rspec spec/features/truefx_spec.rb

# I should have executable:
# chromedriver
# in my path.
# I put it here: ~/bin/chromedriver

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
      fill_in 'USERNAME', with: 'bosmith1990'
      sleep 1
      fill_in 'PASSWORD', with: 'java4PYTHON'
      sleep 1
      click_on 'Login'
      sleep 1
    end
    #months_s_a = ['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    months_s_a = ['SEPTEMBER']
    #months_i_a = ['01','02','03','04','05','06','07','08','09','10','11','12']
    months_i_a = ['09']
    m_i        = -1 # I should use this to count months in the loop below.
    #years_a    = [2010,2011,2012,2013,2014,2015,2016]
    years_a    = [2016]
    #pairs_a    = ['AUDUSD','EURUSD','GBPUSD','USDCAD','USDJPY']
    pairs_a    = ['EURUSD','USDJPY']
    for month_s in months_s_a do
      m_i += 1
      for yr_i in years_a do
        for pair in pairs_a do
          p "#{ahost}/dev/data/#{yr_i}/#{month_s}-#{yr_i}/#{pair}-#{yr_i}-#{months_i_a[m_i]}.zip"
          visit     "/dev/data/#{yr_i}/#{month_s}-#{yr_i}/#{pair}-#{yr_i}-#{months_i_a[m_i]}.zip"
          sleep 60
        end
      end
    end
    
    # logout
    find(:xpath, "//a[@href='?page=logout']").click
    sleep 1
  end
end
