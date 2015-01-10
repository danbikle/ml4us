require 'test_helper'

class PostsControllerTest < ActionController::TestCase
  test "should get linux101" do
    get :linux101
    assert_response :success
  end

end
