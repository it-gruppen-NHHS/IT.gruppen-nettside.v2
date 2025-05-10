from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime
from encryption import Encryption

db = SQLAlchemy()


encrypt = Encryption()


'''
Eksempel på hvordan man setter opp en tabell
'''
class Groups(db.Model):
    """ Table for groups"""
    __tablename__ = 'groups'
    groupId = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True)
    groupName = db.Column(db.String(150),
                         index = False,
                         unique = False,
                         nullable = False)
    timestamp = db.Column(db.DateTime,
                          index = False,
                          unique = False,
                          nullable = False)
    logoPath  = db.Column(db.String(150),
                          index = False,
                          unique = False,
                          nullable = True)

    def __init__(self, groupId, groupName):
        self.groupId = groupId
        self.groupName = groupName
        self.timestamp = datetime.now()

