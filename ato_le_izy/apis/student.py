from bson import json_util
from flask import Flask, request, render_template, render_template_string
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename, redirect

import db_connect

app = Flask(__name__)
api = Api(app)


class Students(Resource):
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
                data[attr] = value[0]
        db_connect.db.students.insert_one(data)
        return redirect("/student")