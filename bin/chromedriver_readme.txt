~/ml4us/bin/chromedriver_readme.txt

I got chromedriver from google:

http://chromedriver.storage.googleapis.com/2.22/chromedriver_linux64.zip

chromedriver is an executable which needs to be in my PATH when I run feature specs.

Here is an example feature spec command line:

bin/rspec spec/features/chrome_spec.rb

The above feature spec depends on a gem:
selenium-webdriver

When I setup a new Rails app,
before I try to run feature specs,
I should test the gem: selenium-webdriver

I wrote a test script and placed it here:

~/ml4us/script/seldemo.rb

This command line should run the above script:

export PATH=${HOME}/ml4us/bin:$PATH
bin/rails r script/seldemo.rb

The above script should start Chrome-browser and submit 'Cheese' to google.com

I should see something like this in my shell:

dan@hp1:~/ml4us $ 
dan@hp1:~/ml4us $ 
dan@hp1:~/ml4us $ export PATH=${HOME}/ml4us/bin:$PATH
dan@hp1:~/ml4us $ bin/rails r script/seldemo.rb
Running via Spring preloader in process 18030
Page title is Google
Page title is Cheese! - Google Search
dan@hp1:~/ml4us $
dan@hp1:~/ml4us $
dan@hp1:~/ml4us $

If the above script works then I might try this command line next:

bin/rspec spec/features/chrome_spec.rb

The above script should start Chrome-browser and then quickly exit.

I should see something like this in my shell:

dan@hp1:~/ml4us $
dan@hp1:~/ml4us $
dan@hp1:~/ml4us $
dan@hp1:~/ml4us $ bin/rspec spec/features/chrome_spec.rb 
  ActiveRecord::SchemaMigration Load (0.4ms)  SELECT "schema_migrations".* FROM "schema_migrations"
  ActiveRecord::SchemaMigration Load (0.4ms)  SELECT "schema_migrations".* FROM "schema_migrations"
  ActiveRecord::SchemaMigration Load (0.1ms)  SELECT "schema_migrations".* FROM "schema_migrations"
   (229.3ms)  DROP DATABASE IF EXISTS "ml4us_test"
   (663.8ms)  CREATE DATABASE "ml4us_test" ENCODING = 'unicode'
  SQL (0.3ms)  CREATE EXTENSION IF NOT EXISTS "plpgsql"
   (134.6ms)  CREATE TABLE "schema_migrations" ("version" character varying PRIMARY KEY)
   (0.8ms)  SELECT version FROM "schema_migrations"
   (8.9ms)  INSERT INTO "schema_migrations" (version) VALUES ('0')
   (125.2ms)  CREATE TABLE "ar_internal_metadata" ("key" character varying PRIMARY KEY, "value" character varying, "created_at" timestamp NOT NULL, "updated_at" timestamp NOT NULL)
  ActiveRecord::InternalMetadata Load (0.8ms)  SELECT  "ar_internal_metadata".* FROM "ar_internal_metadata" WHERE "ar_internal_metadata"."key" = $1 LIMIT $2  [["key", :environment], ["LIMIT", 1]]
   (0.3ms)  BEGIN
  SQL (0.5ms)  INSERT INTO "ar_internal_metadata" ("key", "value", "created_at", "updated_at") VALUES ($1, $2, $3, $4) RETURNING "key"  [["key", "environment"], ["value", "test"], ["created_at", 2016-07-04 20:34:51 UTC], ["updated_at", 2016-07-04 20:34:51 UTC]]
   (8.2ms)  COMMIT
  ActiveRecord::InternalMetadata Load (0.2ms)  SELECT  "ar_internal_metadata".* FROM "ar_internal_metadata" WHERE "ar_internal_metadata"."key" = $1 LIMIT $2  [["key", :environment], ["LIMIT", 1]]
   (0.1ms)  BEGIN
   (0.1ms)  COMMIT
  ActiveRecord::SchemaMigration Load (0.2ms)  SELECT "schema_migrations".* FROM "schema_migrations"
   (0.1ms)  BEGIN
Started GET "/about/index" for 127.0.0.1 at 2016-07-04 13:34:54 -0700
Processing by AboutController#index as HTML
  Rendering about/index.html.haml within layouts/application
  Rendered about/index.html.haml within layouts/application (1.7ms)
Completed 200 OK in 154ms (Views: 137.5ms | ActiveRecord: 0.0ms)
Started GET "/assets/application-e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.css" for 127.0.0.1 at 2016-07-04 13:34:54 -0700
Started GET "/assets/application-f300883d5979c844606775f9e3433ad3b2a847c3f2f305581f9b4394a3cc889f.js" for 127.0.0.1 at 2016-07-04 13:34:54 -0700
   (0.1ms)  ROLLBACK
.

Finished in 3.02 seconds (files took 4.43 seconds to load)
1 example, 0 failures

dan@hp1:~/ml4us $ 
dan@hp1:~/ml4us $ 
dan@hp1:~/ml4us $

