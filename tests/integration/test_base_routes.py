def test_root_route(test_app):
    """
    Test the root ('/') route of the Flask application.
    """
    # Create a test client using the Flask application configured for testing
    client = test_app.test_client()

    # Make a GET request to the root URL
    response = client.get('/')

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response contains the expected text
    assert b'<h2>Hello World</h2>' in response.data
