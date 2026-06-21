# Student Performance Analyzer

A beginner data analysis project built with Python, Pandas, and NumPy.

## Overview

This project analyzes student performance data stored in a CSV file. It cleans the dataset, validates grades, calculates statistics, generates rankings, and produces a summary report.

## Features

* Load student data from a CSV file
* Remove duplicate and missing records
* Remove invalid grades (less than 0 or greater than 100)
* Calculate student averages
* Assign letter grades (A, B, C, D, F)
* Determine pass/fail status
* Generate student rankings using NumPy
* Find top and bottom students
* Calculate subject averages
* Group students by grade and status
* Filter students based on custom criteria

## Technologies Used

* Python
* Pandas
* NumPy

## Dataset Structure

The CSV file contains:

* ID
* Name
* Math
* Physics
* Programming
* Database
* Attendance

The Attendance column is removed during analysis because it is not used in the final report.

## Example Analyses

* Best-performing student
* Lowest-performing student
* Average score per subject
* Grade distribution
* Pass/fail distribution
* Students with A grades
* Students who excel in Programming
* Students who struggle in Math

## What I Learned

* Reading and processing CSV files with Pandas
* Data cleaning and validation
* Creating derived columns
* Grouping and filtering data
* Using NumPy for ranking calculations
* Building a simple data analysis workflow

## How to Run

1. Install the required libraries:

   * pandas
   * numpy

2. Place `Students.csv` in the project directory.

3. Run:

   `python main.py`
