# **LiwaaHaddara_T1A3. My Terminal Application (A Library Book Managment System)**

## **Code Styling Conventions**

- I have used the Pascal case naming convention for any classes created in my source code (e.g:  
  `'Class LibraryBook():'`)
- I've used the snake case naming convention for any functions created in my source code (e.g:  
  `'def print_a_book():'`)
- The camel case naming convention has been used to name all files in the project (e.g:  
  ` libraryCatalogue.py`)
- Using Python to implement my code, I have chosen to use the mainstream pep-8 styling convention and, making sure all the code has been indented correctly

## **List of features used in the app**

A description of how some of the features available in the program are implemented

### **1. Navigating the Main Menu**

- Once the program has begun, the user has multiple options to choose from in the navigation menu, with every option represented by a number (such as printing the catalogue, which is the first option, represented the by the string "1")
- The user will be asked to input a number between 1 and 6 (inclusive), as each number will trigger a certain function in the program
- A **_while loop_** is implemented to make sure that the user cannot exit the program until they've entered the number "6" as an input in order to exit the terminal app.
- A group of **_if-elif-else_** statements are used to execute certain functions, depending on the number the user chooses to input
- If a user enters anything other than an integer between 1 and 6, **_the program will handle the error_** by printing a statment that asks the user to re-attempt entering a valid value

### **2. Adding a Book to the Catalogue**

- When the user chooses the option of adding a book to the catalogue, the program will stop and ask them to re-try if they don't attempt to provide **_BOTH the title and author names_** for their book entry.
- This is implemented by using an **_if statement that includes the 'and' keyword_**, ensuring that the user fulfils both conditions in order for the book entry to be successfully added to the catalogue.

### **3. Finding the Initial Catalogue of Books**

- If a user inputs "1" in the main menu, they'll be presented with the catalogue, containing the title and author name of each currently available for renting.
- This is implemented through the help of the **_use of a variable (a global variable) declaration on line 5 of 'library.py'_** in order to access an instance of the LibraryCatalogue class so we can access each individual entry within the catalogue.

## **Link to Github Repository:**

[Github Repository](https://github.com/liwaahaddara/LiwaaHaddara_T1A3)

## **Link to Development Plan:**

[Software Development Plan (on Trello)](https://trello.com/invite/b/QMGqbeLo/76bade714f2a29e235d6cf15f203cd33/terminal-app-library-system-development-plan)

## **References**

1. stackoverflow. 2022. How can I capitalize the first letter of each word in a string?. [online] Available at: <https://stackoverflow.com/questions/1549641/how-can-i-capitalize-the-first-letter-of-each-word-in-a-string> [Accessed 17 July 2022].

2. Bilbao, J., 2022. JairoAussie/wd-std3-cafe. [online] GitHub. Available at: <https://github.com/JairoAussie/wd-std3-cafe> [Accessed 17 July 2022].
