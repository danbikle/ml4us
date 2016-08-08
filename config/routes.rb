Rails.application.routes.draw do
  get  'home/index'
  root 'home#index'
  get 'about/index'
  get 'blog/index'
  get 'cclasses/class01'
  get 'cclasses/class02'
  get 'cclasses/class03'
  get 'contact/index'

  get 'about'   => 'about#index'
  get 'blog'    => 'blog#index'
  get 'contact' => 'contact#index'
  get ':controller(/:action)'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
