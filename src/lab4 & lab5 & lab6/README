# Lab4

The focus is on classes and objects
So far in the course we have worked with existing data types in Python. In this lab, you will instead create your own composite data type by writing your first class.
You will practice creating objects of your type and saving them in a container that you will then iterate through.

In the lab, you will practice representing an object with a string. The advantage of representing objects in a better way is that it makes it easier for the programmer.
It can make the code more intuitive, more readable. This reduces the risk of errors (bugs).
Before you begin coding please read the below:

[classes](https://docs.python.org/3/tutorial/classes.html)
[lists](https://docs.python.org/3/library/stdtypes.html#lists)
[while](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)

## Task

Define a class “Student” that has at least three attributes: first name, last name, and social security number. The class should have at least two methods, __init__ and __str__.

Create at least three objects of type “Student” by asking the user to enter information about students. Consider the best way to save the created objects.
When all objects are created, the program should print all created objects

Output example:

What is the student's name? Jan Jansson
What is the student's social security number? 0404040010

Object created!

What is the student's name? Per Persson
What is the student's social security number? 0303030030

Object created!

What is the student's name? Emma Emilsson
What is the student's social security number? 010101000a
The social security number must only contain numbers, try again!
What is the student's social security number? 0101010000

Object created!

Here are all saved objects:
Name: Jan Jansson Social Security Number: 0404040010
Name: Per Persson Social Security Number: 0303030030
Name: Emma Emilsson Social Security Number: 0101010000

## Requirements

The program must meet all requirements mentioned in the description.
All input must be error-handled using appropriate helper functions.


## Optional additional tasks

### 1-Edit the list

In the basic task, we can only add objects of type Student. Add so that the user can change and remove objects from the list.

Output example 
Do you want to add (l), change (a) or remove (t) an object? a

Enter the personal identification number of the object you want to change: 0101010000
Do you want to change the name of Emma Löv (y/n)? y
Enter the new name: Ebba Löv

### 2– Adding many students

Change so that the program can ask n  numbers of 
students instead of just three.

Sample printout
How many students do you want to add? 2

What is the student's name? Jan Jansson
What is the student's social security number? 0404040010

Object created!

What is the student's name? Per Persson
What is the student's social security number? 0303030030

Object created!

Here are all the saved objects:

Name: Jan Jansson Social Security Number: 0404040010

Name: Per Persson Social Security Number: 0303030030


# Lab5

In the previous lab, we used a class whose objects we saved in a container in the main program. Now we will instead use two classes,
where the first class has a container as an attribute, where we save objects from the second class.

The advantage of saving objects in this way is that we can create a more structured and usable code, which makes the code more readable and flexible.

Before you start coding 
Read about: [Dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

## Task

Now we are going to write a class “School” that has at least one attribute called students.

Create an object of type School. Again, let the user enter information about at least three students and create objects of type Student.

Save the objects in the attribute students of the School object.

Think about what is the best type of container to save the objects. What are the disadvantages and advantages of different containers?

Now add a method to the School class that allows the user to search for a student who attends the school and that prints out whether the student exists and the Student object found. You can choose whether to search using first name, last name or social security number.

Output example
...
What is the student's name? Emma Emilsson
What is the student's social security number? 010101000a
The social security number must only contain numbers, try again!
What is the student's social security number? 0101010000

The student has been added!

Which student do you want to search for? Jan

That student studies at KTH:
Name: Jan Jansson Social security number: 0404040010


## Requirements

The program must meet all requirements mentioned in the description.
All input must be error-handled using appropriate helper functions.
Your code must meet the requirements in the correction matrix.


## Optional additional tasks

### 1-Manage teachers

Add a class Person that the class Student inherits from, see inheritanceLinks to an external site.. Create another class Teacher that also inherits from Person. Add so that the class School has two attributes, one for students and one for teachers, or find your own way to separate students and teachers in your program.

Output example
...
What role does the person have? Teacher
What is the person's name? Albert Einstein
What is the person's personal identification number? 7903140050

Person added!

Here are all the students at KTH:
Name: Jan Jansson Personal identification number: 0404040010
Name: Per Persson Personal identification number: 0303030030
Name: Emma Emilsson Personal identification number: 0101010000

Here are all the teachers at KTH:
Name: Albert Einsten Personal identification number: 7903140050

# Lab6

Previously, we have let the user enter all the information about the students. However, this does not seem entirely reasonable for administrative staff at a large school to do, so we will now instead let the program read that information from a file.

Before you start coding 
Read about: [file handling](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

You have the file called: 'students.txt' 

## Task

In this lab, you will have the user enter the name of a file that contains all the students' assignments. You will then read the assignments into the file and use them in your program that you wrote in the previous lab. If the file does not exist, the user will enter a new filename.

Output example:

What is the name of the file with all students? students.cs
That file did not exist! Enter a new file: students.txt

These students are enrolled at KTH:
Name: Johan Tierney Personal no.: 8411285597
Name: Erik Bolin Personal no.: 9910247016
Name: Per Edenström Personal no.: 8410024155

...

Which student do you want to search for? Jan

That student studies at KTH:
Name: Jan Jansson Personal no.: 0404040010


## Requirements

The user should be allowed to enter a new filename if the file is not found.
The requirements for lab 5 should be met. 
Your code should meet the requirements in the correction matrix.

Presentation
This laboratory work must be presented to a teaching assistant at a laboratory session. Information about booking a presentation session will be posted on Canvas.
During the presentation, you must be able to run your program and describe your code in detail.

## Optional extra task:

Give the user the ability to add, change, or delete objects. At the end of the program, all objects should be read back into a file that the user can enter the name of.

Output example
What is the name of the file with all students? students.cs
That file did not exist! Enter a new file: students.txt
These students are enrolled at KTH:
Johan Tierney 8411285597
Erik Bolin 9910247016
Per Edenström 8410024155
...

Do you want to add (l), change (a) or delete (t) an object? a

Enter the personal identification number of the object you want to change: 0101010000
Do you want to change the name of Emma Lov (y/n)? j
Enter the new name: Ebba Lov

The name for 0101010000 has now been changed to Ebba Lov!

Enter the name of the file to which the data should be saved: students.txt

All data is now saved to the file students.txt
