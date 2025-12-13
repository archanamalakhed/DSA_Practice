
def test_api_post(playwright):
    request = playwright.request.new_context()
    response = request.post("https://jsonplaceholder.typicode.com/posts",
                            data={
                                "title": "Learning Playwright",
                                "body": "Hello, this is a test post",
                                "userId": 1
                            }       
                            
                            )
    assert response.status == 201
    json_data = response.json() 
    print(json_data)
    assert json_data["title"] == "Learning Playwright"
    assert json_data["body"] == "Hello, this is a test post"
    assert json_data["userId"] == 1
    request.dispose()
    print("Test completed successfully.")