from flask import Flask,request,jsonify
app = Flask(__name__)

employee_list=[
    {
        "id":101,
        "name":"siva",
        "department":"it",
        "designation":"developer",
    },
    {
        "id":102,
        "name":"nag",
        "department":"it",
        "designation":"developer",
    },
    {
        "id":103,
        "name":"abhi",
        "department":"testing",
        "designation":"tester",
    },
    {
        "id": 104,
        "name": "sai",
        "department": "desing",
        "designation": "designer",
    },
    {
        "id": 105,
        "name": "vamsi",
        "department": "testing",
        "designation": "tester",
    },
    {
        "id": 106,
        "name": "kumar",
        "department": "graphics",
        "designation": "graphics",
    },
]

@app.route('/employees',methods=['GET','POST'])
def employees():
    if request.method=='GET':
        if len(employee_list)>0:
            return jsonify(employee_list)
        else:
            'Nothing found', 404
    if request.method=='POST':
        id=employee_list[-1]['id']+1
        name=request.form['name']
        dept=request.form['department']
        des = request.form['des']

        new_emp={
            'id':id,
            'name':name,
            'department':dept,
            'designation':des
        }
        employee_list.append(new_emp)
        return jsonify(employee_list),201

if __name__ == '__main__':
    app.run(debug=True)
