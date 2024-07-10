# **Spencer's Phase 3 Project README **

## *Overview of project:*

This project is to create tables in SQL using ORM in python. These tables have a one to many relationship. These tables are then displayed in different ways in the CLI. The user is required to put in inputs to change and display the information in the CLI. A menu is shown with these different options. 

The attributes are get and set using different requirements and those requirements are then shown to the user in the CLI when they are in each option to make sure they understand what went wrong and inturn what went right. 

Some helper functions were used to keep the code DRY.

## *Use of project:*

The use of this project is to create two classes that are Travelers and Locations. Each traveler can go to multiple locations but each location does not have many travelers. Contained in the code are instant and class methods that iterate through the code to display all this information. A foriegn key is used to link these two classes as the location belongs to the traveler. This project helps show the relationships and display the data to the user in unique ways. 

## *Requirements: like verison and packages:*
You are required to have python installed. At least version 3.8. Additionally included is a ipdb which is located in the debugger file. This can be impliented by running pipenv install. 

