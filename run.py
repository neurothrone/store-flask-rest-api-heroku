from app import app
from management.database import db

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()
