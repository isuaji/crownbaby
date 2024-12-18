from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime as dt
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:MosPolytech@localhost:5432/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), nullable=False)
    eventTitle = db.Column(db.Text, nullable=False)
    eventDesc = db.Column(db.Text, nullable=False)
    eventDateTime = db.Column(db.DateTime, default=dt.now)
    eventDay = db.Column(db.Integer, nullable=False)
    eventMonth = db.Column(db.Integer, nullable=False)
    eventYear = db.Column(db.Integer, nullable=False)

def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("База данных инициализирована")

init_db()

@app.route('/api/users/<uuid>', methods=['GET'])
def get_user_events(uuid):
    try:
        events = User.query.filter_by(uuid=uuid).all()
        return jsonify([{
            "id": event.id,
            "uuid": event.uuid,
            "eventTitle": event.eventTitle,
            "eventDesc": event.eventDesc,
            "eventDateTime": event.eventDateTime.isoformat(),
            "eventDay": event.eventDay,
            "eventMonth": event.eventMonth,
            "eventYear": event.eventYear
        } for event in events])
    except Exception as e:
        print(f"Ошибка при получении событий: {str(e)}")
        return jsonify([])

@app.route('/events/<uuid>', methods=['POST'])
def addUserEvent(uuid):
    try:
        data = request.get_json()
        print(f"Получены данные: {data} для UUID: {uuid}")
        
        new_event = User(
            uuid=uuid,
            eventTitle=data['eventTitle'],
            eventDesc=data['eventDesc'],
            eventDateTime=dt.strptime(data['eventDateTime'], '%Y-%m-%dT%H:%M:%S.%fZ'),
            eventDay=data['eventDay'],
            eventMonth=data['eventMonth'],
            eventYear=data['eventYear']
        )
        
        db.session.add(new_event)
        db.session.commit()
        
        return jsonify({
            "status": "success",
            "message": "Событие усп��шно создано",
            "data": {
                "id": new_event.id,
                "uuid": new_event.uuid,
                "eventTitle": new_event.eventTitle,
                "eventDesc": new_event.eventDesc,
                "eventDateTime": new_event.eventDateTime.isoformat(),
                "eventDay": new_event.eventDay,
                "eventMonth": new_event.eventMonth,
                "eventYear": new_event.eventYear
            }
        }), 200
        
    except Exception as e:
        print(f"Ошибка при добавлении события: {str(e)}")
        return jsonify({
            "status": "error",
            "message": f"Ошибка при создании события: {str(e)}"
        }), 400

@app.route('/debug/all-data', methods=['GET'])
def get_all_data():
    try:
        all_events = User.query.all()
        return jsonify([{
            "id": event.id,
            "uuid": event.uuid,
            "eventTitle": event.eventTitle,
            "eventDesc": event.eventDesc,
            "eventDateTime": event.eventDateTime.isoformat(),
            "eventDay": event.eventDay,
            "eventMonth": event.eventMonth,
            "eventYear": event.eventYear
        } for event in all_events])
    except Exception as e:
        print(f"Ошибка при получении данных: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)