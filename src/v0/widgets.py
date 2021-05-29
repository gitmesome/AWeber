from .models import Widget
from flask import jsonify, abort, make_response
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
        .filter(Widget.number_of_parts == widget_number_of_parts)
        .one_or_none()
    )


def create_db_widget(widget_name, widget_number_of_parts):
    widget = Widget(name=widget_name, number_of_parts=widget_number_of_parts)

    db.session.add(widget)
    db.session.commit()

    return widget


def update_db_widget(widget, body):
    widget.name = body.get('name')
    widget.number_of_parts = body.get('number_of_parts')

    db.session.add(widget)
    db.session.commit()

    return widget

def delete_db_widget(widget):
    db.session.delete(widget)
    db.session.commit()


def get_widget_by_id(widget_id):
    return (
        Widget.query.filter(Widget.widget_id == widget_id)
        .one_or_none()
    )


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


def update(body):
    widget_id = body.get('widget_id')

    widget_exists = get_widget_by_id(widget_id)

    if widget_exists is not None:
        widget = update_db_widget(widget_exists, body)
        result = wrap_to_dict(widget)
        return jsonify(result), 200
    else:
        abort(404, "Widget Not found")


def delete(widget_id):
    widget_exists = get_widget_by_id(widget_id)

    if widget_exists is not None:
        delete_db_widget(widget_exists)
        return make_response(f"Widget {widget_id} deleted", 200)
    else:
        abort(404, "Widget Not found")
