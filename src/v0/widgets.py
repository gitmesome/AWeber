from .models import Widget
from flask import jsonify, abort
from config import db


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
    widget = Widget.query.get(widget_id)
    result = wrap_to_dict(widget)

    return result


def wrap_to_dict(widget):
    result = {'widgets': []}
    row = {}
    for column in widget.__table__.columns:
        row[column.name] = getattr(widget, column.name)
    result['widgets'].append(row)

    return result


def does_widget_exists(widget_name, widget_number_of_parts):
    return (
        Widget.query.filter(Widget.name == widget_name)
        .filter(Widget.num_of_parts == widget_number_of_parts)
        .one_or_none()
    )


def create_db_widget(widget_name, widget_number_of_parts):
    widget = Widget( name = widget_name, num_of_parts = widget_number_of_parts)

    db.session.add(widget)
    db.session.commit()

    return widget


def read_all():
    result = get_all_from_db()
    return jsonify(result)


def read_one(widget_id):
    try:
        result = get_one_from_db(widget_id)
        return jsonify(result)
    except Exception:
        abort(404, "Widget Not found")


def create(body):
    widget_name = body.get('name')
    widget_number_of_parts = body.get('number_of_parts')

    widget_exists = does_widget_exists(widget_name, widget_number_of_parts)

    if widget_exists is None:
        widget = create_db_widget(widget_name, widget_number_of_parts)
        result = wrap_to_dict(widget)
        return jsonify(result), 201

    # Otherwise, widget exists
    else:
        abort(
            409,
            f"Widget {widget_name} {widget_number_of_parts} already exists"
        )


def update(widget):
    pass


def delete(widget_id):
    pass
