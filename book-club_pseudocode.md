## Project Scope
Serendipity Booksellers has a book club that awards points to its customers based on the number of books purchased each month. The points are awarded as follows:

* 0 books = 0 points
* 2 books = 5 points
* 4 books = 15 points
* 6 books = 30 points
* 8 or more books = 60 points

Write a program that asks the user to enter the number of books that he or she has purchased this month, then displays the number of points awarded.

### Sample Run
    Enter the number of books purchased: 7
    You have purchased 7 books.
    This earns you 30 points.
    
## Pseudocode

    Set books to 0
    Set points to 0
    Prompt user for the number of books
    IF books == 2 or 3
      points = 5
    ELSE IF books == 4 or 5
      points = 15
    ELSE IF books == 6 or 7
      points = 30
    ELSE IF books >= 8
      points = 60
    ELSE
      points = 0
    Print "You have purchased [books] books."
    Print "This earns you [points] points."
