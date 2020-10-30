from flask import Flask, render_template
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for
from py2neo import Graph,Node, NodeMatcher
import os
# from neo4j import GraphDatabase

port = int(os.environ.get('PORT', 5000))

url = "bolt://localhost:7687"

#uncomment this if deploying on heroku
# url = "bolt://hobby-ijgbocbmijcpgbkejfelbpfl.dbs.graphenedb.com:24787"
username = os.environ.get("GRAPHENEDB_BOLT_USER","neo4j")
password = os.environ.get("GRAPHENEDB_BOLT_PASSWORD","password")

# driver = GraphDatabase.driver(url, auth=(username, password))
graph = Graph(url, auth=(username, password))
# session = driver.session()


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/showEmp',methods=["GET","POST"])
def show_emp():
    emps = graph.run("MATCH (n:Employee) RETURN n.name, n.id").data()
    return render_template('results.html',data=emps)

@app.route('/addEmp')
def add_emp():
    return render_template('form.html')

@app.route('/create', methods=['GET','POST'])
def create_employee():
    if request.method == 'POST':
        name = request.form['name']
        empid = request.form['empid']
        # session.run("CREATE (a:Employee { name: $name, id: $id})", name=name, id=empid)
        graph.create(Node("Employee", name=name, id=empid))
    else:
        render_template("./form.html")
    return render_template("./form.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)