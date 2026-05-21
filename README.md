# OpenLibrary Book Search API

## Overview
This project uses Python and the OpenLibrary API to search for books and display book titles based on user input.

The program:
- Takes a book name from the user
- Takes a search limit
- Sends a GET request to the OpenLibrary API
- Retrieves book data in JSON format
- Extracts book titles
- Displays results in the terminal

## Technologies Used
- Python
- Requests library
- JSON handling
- REST API

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/openlibrary-book-search-api.git
```

Install dependencies:

```bash
pip install requests
```

Run the program:

```bash
python book_search.py
```

## Example Usage

Input:

```text
Enter the name: Lord of the rings
Enter the limit: 5
```

Output:

```text
There are 5 books

The Fellowship of the Ring
The Two Towers
The Return of the King
Lord of the Rings
The Lord of the Rings
```

## Skills Practiced

- API requests
- GET requests with parameters
- Working with JSON responses
- Extracting nested data
- Iterating through lists
- User input handling
- Basic error handling

## Future Improvements

- Add author names
- Add publication years
- Add exception handling
- Save results to CSV
- Build command-line options
