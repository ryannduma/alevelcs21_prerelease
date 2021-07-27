# alevelcs21_prerelease
This repository contains solutions to the 9608 pre release A-Level CS 2021 June exams problem set

COMPUTER SCIENCE 9608/22 Paper 2 Fundamental Problem-solving and Programming Skills May/June 2021 PRE-RELEASE MATERIAL


TASK 1 – Arrays
Introduction
Candidates should be able to write programs to process array data in pseudocode and in their chosen programming language. Each task should be planned using pseudocode before writing it in program code.
TASK 1.1
Design a way to store multiple pieces of data about a student in a single string. For example, you could store each student’s name, email address and date of birth as follows:
<Student Name>'*'<Email address>'*'<Date of birth> Example: "Sam Arnold*SamArnold137@email.com*25Sep2005"
Use a 1D array of type STRING to store data about each student in the class. Each element of the array will store data for one student.
Write program code to:
1. declare the array
2. prompt and input for student name, email address and date of birth
3. form the string as shown
4. assign the string to the next available array index
5. repeat from step 2 for all members of the class
6. output each element of the array in a suitable format, together with explanatory text such as column headers.
TASK 1.2
Consider what happens when a student’s details are deleted from the array because the student has left the class.
Decide on a way of identifying unused array elements and only output elements that contain students’ details. Modify your program to include this.
TASK 1.3
Extend your program to:
• populate the array as in Task 1.1
• prompt the user to input a student name
• search the array to find that name and output the corresponding email address.

TASK 1.4
Extend Task 1.3 to output a list of all students who have a birthday in a given month.
TASK 1.5
Convert your design to use a 2D array and add additional pieces of data for each student. For example:
4
  Array element
MyArray[1,1]
MyArray[1,2]
MyArray[1,3]
MyArray[1,4]
MyArray[1,5]
Information
Student name
Email address
Date of birth
Student ID
Tutor ID
Example data
"Sam Arnold"
"SamArnold137@email.com"
"25 Sep 2005"
"C3452-B"
"CHL"

TASK 1.6
Modify your program to work with the new structure and extend the searches to work with any piece of data.

TASK 2 – Files
Introduction
Candidates should be able to write programs to process text file data in pseudocode and in their chosen programming language.
Each task should be planned using pseudocode before writing program code.
TASK 2.1
Define a structure for a text file used to store multiple pieces of data about each class member as a single string. Each line of the file will store data for one student.
Store at least three pieces of data. For example, you could store each student’s ID together with his or her email address and date of birth as follows:
   <Student ID><Email address><Date of birth>
Define a fixed format for the Student ID, for example, two letters followed by four digits. Define a fixed format for the date of birth, for example, "DDMMYY"
An example string using this formatting would be:
   "SA1234SamArnold137@email.com250905"
Write a program to:
1. open a new text file
2. prompt for the ID, email address and date of birth
3. form the string as shown
4. write the string to the file
5. repeat from step 2 for all members of the class
6. close the file.
Check the contents of the file using a text editor.
TASK 2.2
Write a second program to search the file for a given Student ID and output the email address if the ID was found, or a suitable message if the ID was not found.
TASK 2.3
Modify the search code to perform a substring match on the Student ID. For example, search for all the Student IDs that begin with "AB".

TASK 2.4
Modify the program to allow the details of additional students to be appended to the file.
TASK 2.5
Consider rules that could be applied to ensure the data entered is acceptable. Modify your program to incorporate these.


********************************************************************************************************************************************************


COMPUTER SCIENCE 9608/42 Paper 4 Further Problem-solving and Programming Skills May/June 2021 PRE-RELEASE MATERIAL
No additional materials are needed.
This material should be given to the relevant teachers and candidates as soon as it has been received at the centre.
INSTRUCTIONS
● You should use this material in preparation for the examination.
● You should attempt the practical programming tasks using your chosen high-level, procedural
  programming language.
  
  
Teachers and candidates should read this material prior to the June 2021 examination for 9608 Paper 4.
Reminders
The syllabus states:
• there will be questions on the examination paper which do not relate to this pre-release material
• you must choose a high-level programming language from:
Visual Basic (console mode) Python
Pascal / Delphi (console mode)
Note: A mark of zero will be awarded if a programming language other than those listed is used.
The practical skills for Paper 4 build on the practical skills covered in Paper 2. We recommend that candidates choose the same high-level programming language for this paper as they did for Paper 2. This will give candidates the opportunity for extensive practice and allow them to acquire sufficient expertise.
Questions on the examination paper may ask the candidate to write:
• structured English
• pseudocode
• program code
A program flowchart should be considered as an alternative to pseudocode for documenting a high- level algorithm design.
Candidates should be confident with:
• the presentation of an algorithm using either a program flowchart or pseudocode
• the production of a program flowchart from given pseudocode and vice versa.
Candidates will also benefit from using pre-release materials from previous examinations. These are available on the teacher support site.
Declaration of variables
The syllabus document shows the syntax expected for a declaration statement in pseudocode.
                     DECLARE <identifier> : <data type>
If Python is the chosen language, each variable’s identifier (name) and its intended data type must be documented using a comment statement.
Structured English – Variables
An algorithm in pseudocode uses variables, which should be declared. An algorithm in structured English does not always use variables. In this case, the candidate needs to use the information given in the question to complete an identifier table. The table needs to contain an identifier, data type and description for each variable.
© UCLES 2021 9608/42/PRE/M/J/21
3
TASK 1 – File storage
Jeff wants a program to help him manage his collection of books. He wants to be able to perform tasks such as search for specific books and add new ones. He has decided he wants a computer program to do this.
TASK 1.1
Design a record structure using pseudocode to store data about his books. He wants to store the following:
• unique code for each book (between 100 and 999)
• title of the book
• main author
• year of publication.
TASK 1.2
Write program code to:
• create your record structure
• create an array to store the records about the books
• input data for 10 books from the user
• store each book as a separate record in an array
• output the data in each record with an appropriate message.
TASK 1.3
The program needs to store the records in the array into a file.
Write a subroutine to store the records in a serial file.
TASK 1.4
Write a procedure to read the records from a serial file and output them with an appropriate message.
Key focus: Hashing algorithms Each book has a unique code. The unique code allows the book’s details to be stored in a random file
using a hashing algorithm.
Develop an appropriate hashing algorithm – you may need to research some examples of hashing algorithms.
TASK 1.6
Manually calculate the file location for several books using your hashing algorithm.
© UCLES 2021 9608/42/PRE/M/J/21 [Turn over
 TASK 1.5

TASK 1.7
Write a pseudocode algorithm to perform the hash calculation.
TASK 1.8
Key focus: Random files
4
 Write a pseudocode algorithm to store a record in its hashed location in the random file.
TASK 1.9
Write a pseudocode algorithm to read a record from its hashed location in the random file.
© UCLES 2021 9608/42/PRE/M/J/21

TASK 2 – Binary tree
The following is a binary tree, created from a set of data:
       amber
TASK 2.1
Identify the root node and leaf nodes in the binary tree.
TASK 2.2
Add the following data to the binary tree:
pink yellow blue purple
TASK 2.3
fuchsia
Key focus:
Binary tree
turquoise
indigo
5
maroon
   black
red
silver
violet
   grey
lime green
 Write program code to store the binary tree as a 1D array of records.
Each record should contain a pointer to the node on its left, a pointer to the node on its right and its data.
Store the binary tree shown in the array.
TASK 2.4
Write program code to add a new data item to the binary tree.
TASK 2.5
Write program code to find the position of a specific colour in the binary tree.
TASK 2.6
Write program code to output the contents of the binary tree in alphabetical order.
© UCLES 2021 9608/42/PRE/M/J/21 [Turn over

6 TASK 3 – Object-oriented programming (OOP)
A virtual shop in a computer game sells a range of tools such as a spade and a screwdriver. The tools are stored on shelves in the virtual shop.
TASK 3.1
The program needs a class for the tools.
 The information stored about each tool must include:
• name
• cost
• image file name (e.g. ‘spade.jpeg’).
Write program code for the class tools.
The constructor should take all of the attributes as parameters.
Write program code for the attributes and the constructor method.
TASK 3.2
Key focus:
Creating classes
Write program code to create a get and set method for each of the tool attributes.
TASK 3.3
The program needs a class for the shelves in the store.
Each shelf has the following information:
• position of the shelf on the wall (between 0 and 4)
• array of objects of type tool (maximum of 10 items per shelf).
Write program code for the class shelves.
The constructor should set the position of the shelf but should not set any tools.
Write program code for the attributes and the constructor method.
TASK 3.4
Write program code for a set method to add a new tool to the shelf in the next available position.
TASK 3.5
Write program code to define a procedure that takes a shelf object as a parameter and outputs the name and cost of each tool on that shelf.
