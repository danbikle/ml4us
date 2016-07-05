Rails.application.routes.draw do
  get 'cclasses/class01'

  get 'cclasses/class02'

  get 'cclasses/class03'

  get 'contact/index'

  get 'blog/index'

  get  'about/index'
  root 'about#index'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
