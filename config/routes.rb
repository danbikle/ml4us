Rails.application.routes.draw do
  get 'syl/index'
  root 'syl#index'
  get 'syllabus' => 'syl#index'
  get 'contact'  => 'syl#contact'
  get ':controller(/:action)'
end
