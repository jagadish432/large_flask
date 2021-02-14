import os
from config import PROJECT_ROOT, DATABASE_NAME
from flask_sqlalchemy import SQLAlchemy


database_file = os.path.join(PROJECT_ROOT, 'db', DATABASE_NAME)
db = SQLAlchemy()


class BookTypes(db.Model):
    __tablename__ = 'BookTypes'
    type = db.Column(db.String(20), unique=True, nullable=False, primary_key=True)
    charge = db.Column(db.Float, nullable=False)  # original charge per day
    minimumCharge = db.Column(db.Float, nullable=True)  # minimum charge to be paid
    minimumRetention = db.Column(db.Integer, nullable=True)  # minimumDays to avoid minimum charge
    trialCharge = db.Column(db.Float, nullable=True)  # discounted charge per day in trial period
    trialPeriod = db.Column(db.Integer, nullable=True)  # no. of days for trial period

    def __repr__(self):
        return "<Type: {} Charge: {}>".format(self.type, self.charge)
