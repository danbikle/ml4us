ruby '2.3.1'
source 'https://rubygems.org'

gem 'rails_12factor'
gem 'haml'          
gem 'haml-rails'    

gem 'rails', '~> 5.0.0'

gem 'pg', '~> 0.18'

gem 'puma', '~> 3.0'

gem 'sass-rails', '~> 5.0'

gem 'uglifier', '>= 1.3.0'

gem 'coffee-rails', '~> 4.2'

gem 'therubyracer', platforms: :ruby

gem 'jquery-rails'

gem 'turbolinks', '~> 5'

gem 'jbuilder', '~> 2.5'

# Use Redis adapter to run Action Cable in production
# gem 'redis', '~> 3.0'
# Use ActiveModel has_secure_password
# gem 'bcrypt', '~> 3.1.7'

group :development, :test do
  # Useful:
  gem 'sqlite3'
  # Needed by rspec-rails:
  gem 'diff-lcs',           '1.2.5'
  gem 'rspec-support',      '3.5'
  gem 'rspec-core',         '3.5'
  gem 'rspec-expectations', '3.5'
  gem 'rspec-mocks',        '3.5'
  gem 'rspec-rails',        '3.5'
  gem 'addressable',        '2.4.0'
  gem 'xpath',              '2.0.0'
  gem 'capybara',           '2.7.1'
  gem 'rubyzip',            '1.2.0'
  gem 'websocket',          '1.2.3'
  gem 'childprocess',       '0.5.9'
  gem 'selenium-webdriver', '2.53.4'
  # Above needed by rspec-rails.
  # Call 'byebug' anywhere in the code to stop execution and get a debugger console
  gem 'byebug', platform: :mri
end

group :development do
  # Access an IRB console on exception pages or by using <%= console %> anywhere in the code.
  gem 'web-console'
  gem 'listen', '~> 3.0.5'
  # Spring speeds up development by keeping your application running in the background. Read more: https://github.com/rails/spring
  gem 'spring'
  gem 'spring-watcher-listen', '~> 2.0.0'
end

# Heroku wants this:
# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem 'tzinfo-data', platforms: [:mingw, :mswin, :x64_mingw, :jruby]
# end
