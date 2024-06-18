from flask import Flask
from dbin import db
from models import User, Belonging, Sorcer, Technique
import data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.drop_all()  # Удалим все таблицы, чтобы избежать дублирования данных
    db.create_all()

    # Добавляем данные из data.py
    for belonging_data in data.belongings_data:
        belonging = Belonging(group=belonging_data["group"])
        db.session.add(belonging)

    db.session.commit()

    for sorcer_data in data.sorcers_data:
        belonging = Belonging.query.filter_by(group=sorcer_data["belonging"]).first()
        sorcer = Sorcer(
            name=sorcer_data["name"],
            status=sorcer_data["status"],
            belonging_id=belonging.id
        )
        db.session.add(sorcer)

    db.session.commit()

    for technique_data in data.techniques_data:
        sorcer = Sorcer.query.filter_by(name=technique_data["sorcer"]).first()
        technique = Technique(
            name=technique_data["name"],
            strength=technique_data["strength"],
            rate=technique_data["rate"],
            sorcer_id=sorcer.id
        )
        db.session.add(technique)

    db.session.commit()
