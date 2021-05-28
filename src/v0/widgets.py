from .models import Widget
from flask import jsonify

def read_all():
    result = {'data': []}
    for widget in Widget.query.all():
        row = {}
        for column in widget.__table__.columns:
            row[column.name] = getattr(widget, column.name)
        result['data'].append(row)

    return jsonify(result)


def read_one(widget_id):
    pass


def create(widget):
    pass


def update(widget):
    pass


def delete(widget_id):
    pass
