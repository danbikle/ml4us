Rails.application.routes.draw do
  get 'posts/linux101'

  get 'syl/index'
  root 'syl#index'
  get 'syllabus' => 'syl#index'
  get 'contact'  => 'syl#contact'
  get ':controller(/:action)'
end
