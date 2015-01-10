Rails.application.routes.draw do
  get 'syl/index'
  root 'syl#index'
  get 'syllabus' => 'syl#index'
  get 'contact'  => 'syl#contact'
  get 'posts'     => 'posts#index'
  get 'tags'      => 'posts#tags'
  get 'questions' => 'questions#index'
  get 'tags(/:tag)' => 'tags#tag'
  get ':controller(/:action)'
end
