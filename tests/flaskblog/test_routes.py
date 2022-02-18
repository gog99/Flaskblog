from http import HTTPStatus

# @bmll-Henri said it was incredibly important to make sure people are getting to the about page
def test_about_page(app_client):
    resp = app_client.get('/about')
    assert resp.status_code == HTTPStatus.OK
