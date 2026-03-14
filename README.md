Student Marks Analysis Using NumPy

Overview
This project demonstrates how NumPy can be used to analyze student marks efficiently using array operations. The program stores marks of multiple students across different subjects in a two dimensional NumPy array and performs several statistical operations to analyze the data.

The goal of this project is to practice numerical data processing using NumPy, which is an important library used in data science and scientific computing.

Technologies Used
Python
NumPy

Dataset Structure
Student marks are stored in a two dimensional NumPy array where

Each row represents a student
Each column represents a subject

Subjects included in the analysis

Maths
Science
English

Example dataset

Student 1: 78 85 90
Student 2: 92 88 95
Student 3: 65 70 72
Student 4: 88 90 84

Program Features

Displays marks of each student
Calculates the average marks of every student across all subjects
Calculates the average marks for each subject
Computes total marks for each student
Identifies the highest total score in the class
Filters and displays marks greater than 85

Key NumPy Operations Used

Mean calculation across rows to compute student averages
Mean calculation across columns to compute subject averages
Sum operation for total marks
Maximum value detection for highest marks
Boolean filtering to extract marks above a specific threshold

Program Workflow

Student marks are stored in a NumPy array
The program prints marks for each student
Average marks are calculated using NumPy mean functions
Subject wise averages are computed using column operations
Total marks of each student are calculated
The highest total marks are identified
Finally the program filters marks greater than a defined value

Learning Outcome

This project helps in understanding how numerical datasets can be processed efficiently using NumPy arrays. It introduces concepts such as axis based operations, aggregation functions, and data filtering which are essential for data analysis and machine learning workflows.

Author

Uday Bhaskar
Aspiring Data Science learner working with Python, NumPy, and data analysis concepts.
