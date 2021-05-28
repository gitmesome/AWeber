import os
from datetime import datetime
from config import db
from src.v0.models import Widget

# Init Widget
WIDGET = [
    {
        "name": "SpinnerDoo",
        "number_of_parts": 15,
    },
    {
        "name": "BouncerBon",
        "number_of_parts": 1,
    },
    {
        "name": "SideSmasher",
        "number_of_parts": 5,
    },
    {
        "name": "BobNSlide",
        "number_of_parts": 2,
    },
]

# Delete database file if it exists currently
if os.path.exists("db/widget.db"):
    os.remove("db/widget.db")

# Create the database
db.create_all()

# Populate the widget db
for widget in WIDGET:
    w = Widget(name=widget.get("name"), num_of_parts=widget.get("number_of_parts"))

    db.session.add(w)

for widget in Widget.query.all():
    for column in widget.__table__.columns:
        print(f"{column.name} = {getattr(widget, column.name)}")
    print("\n")

db.session.commit()
