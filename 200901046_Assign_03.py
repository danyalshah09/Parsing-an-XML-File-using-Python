#Danyal Shah
#200901046
#Parsing XML file using python and extracting the data to an excel file 
 
import xml.etree.ElementTree as ElementTree
import pandas as pd

tree = ElementTree.parse('compiler.xml')
root = tree.getroot()

# Create an empty list to store the data
data = [] 
print("-"*50)
# Iterate over the 'book' elements
for book in root.findall('book'):
    id = book.get('id')
    author = book.find('author').text
    title = book.find('title').text
    genre = book.find('genre').text
    try:
        price = float(book.find('price').text)
    except ValueError:
        price = None
    publish_date = book.find('publish_date').text
    description = book.find('description').text

    print("Book_ID: ", id)
    print("Author: ", author)
    print("Title: ", title)
    print("Genre: ", genre)
    print("Price: ", price)
    print("Publish_Date: ", publish_date)
    print("Description: ", description)
    print("\n")
    print("-"*50)
 
  
    # Append the data to the list
    data.append([id, author, title, genre, price, publish_date, description])

# Create a dataframe from the list
    df = pd.DataFrame(data, columns=['Book_ID', 'Author', 'Title', 'Genre', 'Price', 'Publish_Date', 'Description'])

# Write the dataframe to an Excel file
df.to_excel('200901046_Assign_03.xlsx', index=False)
    