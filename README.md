# Neo4j-Flask-App
An application written in Python powered by Flask and Neo4j.

## Prerequisites
You must have Python3, Neo4j and Flask (for API) installed.

## Project Structure
This project has  major parts:

1. app.py - This contains Flask APIs that receives employee details such as Employee Name and Employee ID through GUI or API calls, and returns it.
2. templates - This folder contains the HTML template that allows user to enter Employee Name and Employee ID and displays it.
3. requirements.txt - It contains all the dependencies required by the app.

## Steps to run the app:
Execute in Terminal

```
git clone https://github.com/tyagik25/neo4j-flask-app.git
cd neo4j-flask-app/   
pip3 install virtualenv   
virtualenv -p python3 sandbox   
source <path-oneo-4j-flask folder>/sandbox/bin/activate
pip install -r requirements.txt     
neo4j start
```
**This will start the Neo4j server and you will be able to see the url similar to the one seen below:**

**Go to**:
[http://localhost:7474/browser/](http://localhost:7474/browser/)

Once you go to the above url, follow the below steps:

1. Change connect url from "neo4j://" to "bolt://"
2. Add username = neo4j
3. Password = neo4j
4. Click connect
5. Set the new password as password
6. You will get connected to neo4j

Then execute ```python app.py``` from the root directory

Go to the url [http://0.0.0.0:5000/](http://0.0.0.0:5000/), you will see the application running.





