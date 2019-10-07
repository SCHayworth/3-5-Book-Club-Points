# Program 3-11 Book Club Points
# Shaun Hayworth
# CIS 2
# 10-07-2019
# Original source code and revision history can be found at https://github.com/SCHayworth/3-5-Book-Club-Points

# Calculates the amount of book club loyalty points based on the number of books purchased in a month.

# Initialize book_count and total_points variables and set them to 0.
book_count = 0
total_points = 0

# Prompt user for the number of books and assign input to book_count.
book_count = int(input('Enter the number of books purchased: '))

# Calculate the number of points earned based on book_count value.
if book_count == 2 or book_count == 3:
  total_points = 5
elif book_count == 4 or book_count == 5:
  total_points = 15
elif book_count == 6 or book_count == 7:
  total_points = 30
elif book_count >= 8:
  total_points = 60
else:
  total_points = 0
  
# Display the number of books purchased and the point total.
print(f'You have purchased {book_count} books.')
print(f'This earns you {total_points} points.')
