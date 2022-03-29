- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **Github**: https://github.com/ghimiresdp
# Project: School Management System

> This project aims students to prepare them for a understanding of core python features and an object oriented programming.

## prerequisites:
- json module
- Python Level 1 Course


Create a software that keeps record of students in a file. The software should initialize when it is executed from the file `main.py`.

The folder structure should be as follows:

```
📂 project
 ┣ 📂 records
 ┃ ┣ 📜 grade1.json
 ┃ ┣ 📜 grade2.json
 ┃ ┗ 📜 grade3.json
 ┃
 ┣ 🐍 main.py
 ┗ 📜 log.txt

```
### 🐍 `main.py` File

This file should contain 2 classes `Grade`, and `Student`.

#### The class `Student` should have the following attributes:
- `first_name`: `str` public instance attribute
- `lase_name`: `str` public instance attribute
- `roll`: `int` public instance attribute
- `age`: `int` public instance attribute
- `major`: `computer` or `math` or `science`
- `get_full_name()`: public `method`
- `__str__()`


#### The class `Grade` should have the following attributes:

- `name`: `str` (public instance attribute)
- `students`: `List[Student]` (public instance attribute)
- `list_students`: `function` this should show all the students in the
  tabular format. The output should be of the following format:

  ```
  ------------------------------------
  Roll  Full Name   Age     Major
  ------------------------------------
    1   Jon Doe      20     Math
    2   Jane Doe     22     Science
    3   Jin Doe      19     Computer
  ------------------------------------
  ```
    **Hint for columns length**
    - **Roll**: 5 (justify Right)
    - **Full Name**: 40 (Justify Left)
    - **age**: 3 (Justify Right)
    - **Major**: 20 (Justify Left)

    You can use column spacing of 2 if you want.

- `add_student()`: `function` that adds a student with all detail entered in the console.
- `remove_student(roll)` `function` that takes the roll number and removes the student with the roll number specified.

    _Add more as per your interests._

- Use `json` library for storing contents to the json file.

Sample console screens (Reference only):

#### Creating a class

```
=================================================================
Student Management System:

1. create a class
2. manage a class
3. delete a class
9. Quit application


Please select an option:  1

=================================================================
Creating Class

Enter Class Name: Grade 1

Class 'Grade 1' Created Successfully !!
Student's records will be stored in records/grade1.json

```

#### Managing the class


```
=================================================================
Student Management System:

1. create a class
2. manage a class
3. delete a class
9. Quit application


Please select an option:  2

=================================================================
Select Available classes

1. Grade 1
2. Grade 2
3. Grade 3
0. Go to main menu
9. Quit application


Please select an option: 2

=================================================================
Grade 2 Management Console:

1. Rename the class
2. List Students
3. Add Student
4. Remove Student
5. Modify Student
0. Go to main menu
9. Quit application

=================================================================

```

#### Listing students

```
=================================================================

Grade 2 Management Console:

1. Rename the class
2. List Students
3. Add Student
4. Remove Student
5. Modify Student
0. Go to main menu
9. Quit application

Please select an option:  2


------------------------------------
Roll   Full Name   Age     Major
------------------------------------
   1   Jon Doe      20     Math
   2   Jane Doe     22     Science
   3   Jin Doe      19     Computer
------------------------------------


Please select an option:

=================================================================


```

#### Modifying the student

```
Grade 2 Management Console:

1. Rename the class
2. List Students
3. Add Student
4. Remove Student
5. Modify Student
0. Go to main menu
9. Quit application

Please select an option:  5


Please select the roll number of student: 2

Modifying Jane Doe:

Roll: 2
First Name: Jane
Last Name:  Doe
Age: 22
Major: Science

Enter First Name (blank for 'Jane'):
Enter Last Name (blank for 'Doe'):
Enter Age (blank for '22'): 24
Enter Major (blank for 'Science'): Math
Enter Roll (blank for '2'): 5

Record saved successfully !!
The new Detail is:

Roll: 5
First Name: Jane
Last Name:  Doe
Age: 24
Major: Math


1. Rename the class
2. List Students
3. Add Student
4. Remove Student
5. Modify Student
0. Go to main menu
9. Quit application

Please select an option:
```


Use more options as you can.


Sample JSON file

```json
{
    "name": "Grade 1"
    "students":[
        {
            "first_name": "John",
            "last_name": "Doe",
            "roll": 1,
            "age": 20,
            "major": "Math"
        },
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "roll": 2,
            "age": 22,
            "major": "Science"
        }
    ]
}
```

Bonus Options:

- you can create a different module for `Student` and `Grade` classes and import in the `main.py` file.
- You can password protect your classes so that whenever someone tries to access the class, they need to enter the password.
- you can try saving hashed password using some hashing or encryption methods.
- you can use file formats other than json Eg: XML, or csv file.
