# README

This app serves ML training content to students.

I followed these steps to install ml4.us on my laptop.

* I enhanced Ubuntu for install of Ruby 2.3.1

```bash
sudo apt-get install autoconf bison build-essential libssl-dev libyaml-dev  \
libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm3 libgdbm-dev \
sqlite3 libsqlite3-dev wget curl ruby ruby-dev

sudo mv /usr/bin/ruby /usr/bin/ruby_unused
sudo mv /usr/bin/gem /usr/bin/gem_unused
```

* Next I cloned a repo named rbenv to my home folder:

```bash
cd ~
git clone https://github.com/rbenv/rbenv.git      .rbenv
git clone https://github.com/rbenv/ruby-build.git .rbenv/plugins/ruby-build
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"'               >> ~/.bashrc
bash
```

* Then I issued shell commands to install Ruby 2.3.1 into my home folder:

```bash
rbenv install 2.3.1
rbenv global  2.3.1
which gem
gem install bundler
```

* Next I cloned the repo which you are looking at:

```bash
cd ~
git clone https://github.com/danbikle/ml4us
```

* Then I installed all of the Ruby software (called Gems) needed by ml4.us:

```bash
cd ~/ml4us
bundle
```

