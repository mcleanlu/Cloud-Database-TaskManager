# Overview

This software is a simple yet effective task manager application written in Python. It integrates with Google's Cloud Firestore database to store and manage tasks. With the program, you can create, retrieve, update, mark as complete, and delete tasks. These tasks are then reflected in the Firestore database in real-time. The software is designed for individuals who need an efficient and straightforward way to manage their tasks in their daily routines.

The purpose of writing this software is to demonstrate how to integrate a local Python application with a cloud-based NoSQL database, Firestore, effectively and efficiently. This provides a practical solution for managing data that can be accessed and manipulated in real-time.

[Software Demo Video](https://drive.google.com/file/d/1i19rVYw_Td4U-0q8CFCChlmyltCTFksi/view?usp=sharing)

# Cloud Database

The cloud database used in this application is Google's Cloud Firestore. Firestore is a flexible, scalable NoSQL cloud database that can store and sync data for client- and server-side development. Firestore data is split into collections, documents, fields, and subcollections, organized in a way that facilitates and streamlines data management.

The structure of the database is relatively simple: We have a main collection of 'tasks', where each document represents a unique task. Each task document contains fields for 'name', 'description', 'due_date', 'priority', and 'complete'.

# Development Environment

The tools used to develop this software include:

- Visual Studio Code as the code editor
- Python as the programming language
- Firestore for the database
- Firebase Admin SDK for Python to interface with the Firestore database

# Useful Websites

- [Firebase Admin Python SDK Documentation](https://firebase.google.com/docs/reference/admin/python/)
- [Firestore Documentation](https://firebase.google.com/docs/firestore)

# Future Work

- Incorporate more complex database structures with multiple related collections
- Add a user-friendly interface using a framework like Flask or Django
- Enable sharing tasks between multiple users
- Incorporate real-time updates using Firebase's on_snapshot feature
- Implement further authentication methods and user management features.