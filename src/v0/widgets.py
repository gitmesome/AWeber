from .models import Widget
from flask import jsonify, abort

def get_all_from_db():
    """
        Helper functions moved out so they can be conveniently mocked
    """
    result = {'widgets': []}
    for widget in Widget.query.all():
        row = {}
        for column in widget.__table__.columns:
            row[column.name] = getattr(widget, column.name)
        result['widgets'].append(row)

    return result

def get_one_from_db(widget_id):
    """
        Helper functions moved out so they can be conveniently mocked
    """
    result = {'widgets': []}
    widget = Widget.query.get(widget_id)
    row = {}
    for column in widget.__table__.columns:
        row[column.name] = getattr(widget, column.name)
    result['widgets'].append(row)

    return result


def read_all():
    result = get_all_from_db()
    return jsonify(result)


def read_one(widget_id):
    try:
        result = get_one_from_db(widget_id)
        return jsonify(result)
    except Exception as err:
        abort(404, "Widget Not found")


def create(widget):
    pass


def update(widget):
    pass


def delete(widget_id):
    pass
