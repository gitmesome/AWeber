import pytest
import src.v0.widgets as widgets

one_row = {
    "widgets": [
        {
            "created_at": "2021-05-28T17:32:53.031448Z",
            "name": "SpinnerDoo",
            "num_of_parts": 15,
            "updated_at": "2021-05-28T17:32:53.031454Z",
            "widget_id": 1
        }
    ]
}


def test_read_one_not_found(mocker):
    mocker.patch(
        'src.v0.widgets.get_one_from_db',
        return_value=Exception("not present")
    )
    with pytest.raises(Exception):
        widgets.read_one(1)


def test_read_one_with_data(app, mocker):
    mocker.patch(
        'src.v0.widgets.get_one_from_db',
        return_value=one_row
    )
    with app.app_context():
        result = widgets.read_one(1)
        assert result.status == '200 OK'

def test_create_one(app, mocker):
    mocker.patch(
        'src.v0.widgets.does_widget_exists',
        return_value=None
    )
    mocker.patch(
        'src.v0.widgets.create_db_widget',
        return_value=one_row
    )
    mocker.patch(
        'src.v0.widgets.wrap_to_dict',
        return_value=one_row
    )
    with app.app_context():
        body = {'name': 'SpinnerDoo', 'num_of_parts': 3}
        result = widgets.create(body)
        assert result[1] == 201


def test_create_duplicate(app, mocker):
    mocker.patch(
        'src.v0.widgets.does_widget_exists',
        return_value=True
    )
    with app.app_context():
        with pytest.raises(Exception):
            body = {'name': 'SpinnerDoo', 'num_of_parts': 3}
            result = widgets.create(body)
            assert result[1] == 409
