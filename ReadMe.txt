#Spare Parts Management System using Python, Tkinter and SQL

This project is a Spare Parts Management System built using Python, Tkinter, and SQL. The system is designed to help businesses keep track of their inventory of spare parts and manage orders for replacement parts. The system allows users to add, update, and delete spare parts from the inventory, and create orders for replacement parts.

The system has a user-friendly graphical user interface (GUI) built using the Tkinter library in Python. The GUI allows users to interact with the system by clicking buttons and entering data into text fields. The system also uses a SQL database to store and manage data.

The code includes configuration files for setting up the SQL database Creating required files and fodlers, as well as the Python code for the GUI and backend logic.

Features:
- Add, update, and delete spare parts from the inventory
- Create orders for replacement parts
- View inventory and order history
- Vistalize data in graphical formate(uses matplotlib)
- Generate reports on inventory and orders store the order data as PDF to the local storead

Technologies used:
- Python
- Tkinter
- SQL
- Matplotlib

Installation:
To install this system, clone the GitHub repository and follow the instructions below. 
- The system requires Python 3.x and a SQL server MySQL(In case of any other server main code and config code need edit).
- Download the entries in the repository as zip file extract to local storage C:
  **Note: The Code fodler named "SparePartsManagementSystem" must to stored in the Open C: drive for the code to work properly**
- Edit SSPmanager_config.py file replace the MySQL username and password with your username and password.
- Run the SSPmanager_config.py it will install required modules create database and create Bill storage folder with in "SparePartsManagementSystem" folder.
- Wait until Configuration to complete.
- Edit the main code main.py repalce the SQL username and password.
- Run the main.py file GUI will appear asking for login 'User: admin', 'Password"12345'.
- Explore the interface!

Usage:
To use the system, run the Python script and follow the prompts in the GUI. The system allows users to perform various operations such as adding or updating spare parts, creating orders, and generating reports. Users can also search for spare parts by name or part number, and view their inventory and order history.

Contributing:
Contributions to this project are welcome. If you find a bug or have a suggestion for improvement, please submit a pull request or open an issue on GitHub.

License:
Nil