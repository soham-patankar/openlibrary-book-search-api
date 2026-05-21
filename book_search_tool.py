import requests
import json

def search_terms(book_name,num_limit):
    "The following type of books are to be searched"
    base_url = "https://openlibrary.org/search.json"
    params={
        "q":book_name,
        "limit":num_limit
    }

    response=requests.get(base_url,params=params)

    if response.status_code==200:
        data=response.json()
        print(f'There are {len(data.get("docs",[]))} books')
        books=data.get("docs",[])
        for book in books:
            print(book.get("title",{}))
    else:
        print("Something went wrong")

check_name=input("Enter the name: ")
give_limit=input("Enter the limit: ")

search_terms(check_name,give_limit)

