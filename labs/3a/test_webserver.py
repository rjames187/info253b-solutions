import requests

def test_home():
    page = requests.get('http://localhost:5000')
    true_content = '<h1>Hello!</h1><p>Congrats on building your own server!' +\
        '</p><br /></br /><a href="/page2">Go to the next page</a>'

    assert str(page.text) == true_content
 
def test_page2():
    page = requests.get('http://localhost:5000/page2')
    true_content = '<h1>This is page 2!</h1><p>let us move to page three</p>' +\
        '<br /></br /><a href="/page3">Go to the next page</a>'

    assert str(page.text) == true_content

def test_page3():
    page = requests.get('http://localhost:5000/page3')
    true_content = '<h1>This is page 3!</h1><p>And of end of our journey!</p>'

    assert str(page.text) == true_content