from app import app


def test():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test2():
    response = app.test_client().get('/edit')
    assert response.status_code == 200

# test for checking whether a text is present or not
def test3():
    response = app.test_client().get('/edit')
    # assert b"To" in response.data
    # assert b"Do" in response.data
    assert b"App" in response.data
