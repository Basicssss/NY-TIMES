def call_file():
    list = []
    #open the file with an error message if the user wants to open a wrong file.
    #make sure to use the right file path to the bestseller list
    try:
        file = open('bestsellers2.txt', "r")
    except:
        print("Error could not open file!")

    #Repeat for each book in the text file
    for line in file:
        #split the line into an array called "fields" using the '\t' for tab as a separator
        #remove of the new line characters /r/n
        fields = line.split('\t')
        correct = fields[4]
        fields[4] = correct[:-4]

        #add the book array to the all_list array
        list.append(fields)

    #we organised the file in a usable manner. So we can close it now
    file.close()
    return(list)


#function to print out the list of books.
def print_book_list():
    print('\033[1m' + line[0] + '\033[0m' + ", by " + line[1] + " (" + line[3] + ")")
#function to print out a statement if no book is found.
def print_no_book_list():
    if answer == False:
        print("No books found.")


##############################################################################################################################


#define an empty array at the very beginning. this will be filled later on
all_list = call_file()
import random

while True:
    #displaying list of menu options
    print('What would you like to do? ')
    print('1. Look up books in a range of years when they first hit number one')
    print('2. Look up books of a specific month and year they first hit number one')
    print('3. Search for an author')
    print('4. Search for a title')
    print('5. Give me a random title')
    print('Q. Quit')

    answer = False

    #reading users choice
    choice = input("Enter your choice (1/2/3/4/5/Q): ")

    #breaking out from menu loop if user enters q or Q
    if choice.lower() == 'q':
        print("Bye! Have a lovely day!")
        break

    #search books by in a range of starting and ending years. Only numbers are allowed.
    elif choice == '1':
        try:
            start_year = int(input('Start year: '))
            end_year = int(input('End year: '))
        except ValueError:
            print("This is not a valid input. Try again!")
            continue
        #loop thorugh the list for dates. date is the fourth element in every line.
        #year is the third element within the date splitted by slashes
        for line in all_list:
            date = line[3]
            date_ar = date.split("/")
            year = int(date_ar[2])

            if (year >= start_year) and (year <= end_year):
                answer = True
                print_book_list()

        print_no_book_list()
    #search books by month and year. similar to task 1
    elif choice == '2':
       try:
           month_input = int(input('Month: '))
           year_input = int(input('Year: '))
       except ValueError:
           print("This is not a valid input. Try again!")
           continue

       for line in all_list:
           date = line[3]
           date_ar = date.split("/")
           month = int(date_ar[0])
           year = int(date_ar[2])

           if (year == year_input) and (month == month_input):
               answer = True
               print_book_list()

       print_no_book_list()


    #search books by author. uppercase letters do not matter.
    elif choice == '3':
        author = input('Author: ')
        for line in all_list:
            if author.lower() in line[1].lower():
                answer = True
                print_book_list()

        print_no_book_list()

    #search books by title. uppercase letters do not matter.
    elif choice == '4':
        title = input('Title: ')
        for line in all_list:
            if title.lower() in line[0].lower():
                answer = True
                print_book_list()
        print_no_book_list()

    #Ranomiser that raturns a random item from the list. randomiser via import random
    elif choice == '5':
        random_item = random.choice(all_list)
        print("The book is:", random_item[0], "by " + random_item[1] + " (" + random_item[3] + ")")

    else:
        print("I can't execute that command. Try again!")