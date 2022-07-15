from flask import Flask, request, render_template, redirect
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename
import db_connect

app = Flask(__name__)
api = Api(app)


class Profs(Resource):
    def post(self):
        data = {}
        if "photo" in request.files:
            file = request.files["photo"]
            if file:
                file_name = secure_filename(file.filename)
                file_path = 'uploads/' + file_name
                file.save('static/' + file_path)
                data["photo"] = file_path
        body = request.form.to_dict(flat=False)
        for attr, value in body.items():
            if attr == "module":
                data[attr] = value
            else:
                data[attr] = value[0]
        db_connect.db.profs.insert_one(data)
        return redirect("/prof")
