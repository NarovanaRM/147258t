import db_connect
from bson import ObjectId
from flask import *
from flask_restful import Api
from apis import student, prof
import qrcode

app = Flask(__name__)
api = Api(app)


@app.route("/")
def prof_or_student():
    return render_template("auths.html")


@app.route("/student/signin")
def student_form():
    return render_template("form_student.html")


@app.route("/prof/signin")
def prof_form():
    return render_template("form_prof.html")


@app.route("/student")
def student_list():
    students = db_connect.db.students.find()
    list_student = list(students)
    return render_template("list_student.html", len=len(list_student), students=list_student)


@app.route("/prof")
def prof_list():
    profs = db_connect.db.profs.find()
    list_prof = list(profs)
    return render_template("list_prof.html", len=len(list_prof), profs=list_prof)


@app.route("/prof/<id>/details")
def prof_details(id):
    profs = db_connect.db.profs.find_one({"_id": ObjectId(id)})
    return render_template("prof_details.html", prof=profs)


@app.route("/prof/<id>/qrcode")
def prof_qrcode(id):
    img = qrcode.make(id)
    img_location = "pic_qr/" + id + ".jpg"
    img_path = "static/" + img_location
    img.save(img_path)
    newvalues = {"$set": {"qrcode": img_location}}
    db_connect.db.profs.update_one({"_id": ObjectId(id)}, newvalues)
    profs = db_connect.db.profs.find_one({"_id": ObjectId(id)})
    return render_template("prof_qr.html", prof=profs)


@app.route("/student/<id>/qrcode")
def student_qrcode(id):
    img = qrcode.make(id)
    img_location = "pic_qr/" + id + ".jpg"
    img_path = "static/" + img_location
    img.save(img_path)
    newvalues = {"$set": {"qrcode": img_location}}
    db_connect.db.students.update_one({"_id": ObjectId(id)}, newvalues)
    students = db_connect.db.students.find_one({"_id": ObjectId(id)})
    return render_template("student_qr.html", student=students)


@app.route("/scanner_e")
def scanner_e():
    return render_template("scanner_etudiant.html")


@app.route("/scanner_p")
def scanner_p():
    return render_template("scanner_prof.html")


api.add_resource(student.Students, "/student")
api.add_resource(prof.Profs, "/prof")
if __name__ == "__main__":
    app.run(debug=True)
