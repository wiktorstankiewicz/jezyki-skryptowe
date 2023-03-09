
import wikipedia
from wikipedia.exceptions import PageError

def run():
    print("Welcome to wiki! Please type your desired article name: ")
    articleName = str(input())
    print("Processing...")
    try:
        page = wikipedia.page(title=articleName,auto_suggest=False)
        summary = page.summary
        url = page.url
        print(summary)
        print(url)
    except PageError as e:
        print("Requested article was not found!")
        return
    
    
