import urllib.request, json

class Quote():
    def __init__(self,quote,author):
        self.author = author
        self.quote = quote


def fetch_quotes():
    with urllib.request.urlopen('http://quotes.stormconsultancy.co.uk/random.json') as url:
        response = json.loads(url.read())
        author = response['author']
        quote = response['quote']
        
        quote_object= Quote(quote,author)
    return quote_object

        