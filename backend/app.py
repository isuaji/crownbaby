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
    uuid = db.Column(db.String(36), nullable=False, unique=True)
    events = db.relationship('Event', backref='user', lazy=True)
class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), db.ForeignKey('users.uuid'), nullable=False)
    eventTitle = db.Column(db.Text, nullable=False)
    eventDesc = db.Column(db.Text, nullable=False)
    eventDateTime = db.Column(db.DateTime, default=dt.now)
    eventDay = db.Column(db.Integer, nullable=False)
    eventMonth = db.Column(db.Integer, nullable=False)
    eventYear = db.Column(db.Integer, nullable=False)
    eventTime = db.Column(db.String(5), nullable=False)

def init_db():
    with app.app_context():
        print("База данных инициализирована")

init_db()

@app.route('/calendar/<uuid>', methods=['POST'])
def add_uuid(uuid):
    try:
        if not User.query.filter_by(uuid=uuid).first():
            newUser = User(uuid=uuid)
            db.session.add(newUser)
            db.session.commit()
            return jsonify({"status": "success", "uuid": uuid})
        else:
            return jsonify({"status": "failure", "uuid": uuid, "error": "Пользователь уже существует"})
    except Exception as e:
        return jsonify({"status":"failure", "uuid": uuid, "error": str(e)})

@app.route('/api/users/<uuid>', methods=['GET'])
def get_user_events(uuid):
    try:
        user = User.query.options(db.joinedload(User.events)).filter_by(uuid=uuid).first()
        if user:
            return jsonify([{
                "id": event.id,
                "eventTitle": event.eventTitle,
                "eventDesc": event.eventDesc,
                "eventDateTime": event.eventDateTime.isoformat(),
                "eventDay": event.eventDay,
                "eventMonth": event.eventMonth,
                "eventYear": event.eventYear,
                "eventTime": event.eventTime
            } for event in user.events])
        return jsonify([])
    except Exception as e:
        print(f"Ошибка при получении событий: {str(e)}")
        return jsonify([])

@app.route('/events/<uuid>', methods=['POST'])
def addUserEvent(uuid):
    try:
        user = User.query.filter_by(uuid=uuid).first()
        if not user:
            return jsonify({"status": "error", "message": "Пользователь не найден"}), 404
            
        data = request.get_json() 
        try:
            new_event = Event(
                uuid=uuid,
                eventTitle=data['eventTitle'],
                eventDesc=data['eventDesc'],
                eventDateTime=dt.strptime(data['eventDateTime'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                eventDay=data['eventDay'],
                eventMonth=data['eventMonth'],
                eventYear=data['eventYear'],
                eventTime=data['eventTime']
            )
            
            db.session.add(new_event)
            db.session.commit()
        except Exception as e:
            return jsonify({"status": "error", "message": f"Ошибка при создании события: {str(e)}"}), 400
            
        
        return jsonify({
            "status": "success",
            "message": "Событие успешно создано",
            "data": {
                "id": new_event.id,
                "eventTitle": new_event.eventTitle,
                "eventDesc": new_event.eventDesc,
                "eventDateTime": new_event.eventDateTime.isoformat(),
                "eventDay": new_event.eventDay,
                "eventMonth": new_event.eventMonth,
                "eventYear": new_event.eventYear,
                "eventTime": new_event.eventTime
            }
        }), 200
    except Exception as e:
        print(f"Полная ошибка: {str(e)}")
        return jsonify({"status": "error", "message": f"Ошибка при создании события: {str(e)}"}), 400

@app.route('/events/delete/<int:event_id>/<uuid>', methods=['DELETE'])    
def deleteUserEvent(uuid, event_id):
    try:
        event = Event.query.filter_by(uuid=uuid, id=event_id).first()
        if event:
            db.session.delete(event)
            db.session.commit()
            return jsonify({"status": "success", "message": "Событие успешно удалено"})
        return jsonify({"status": "error", "message": "Событие не найдено"}), 404
    except Exception as e:
        print(f"Ошибка при удалении события: {str(e)}")
        return jsonify({
            "status": "error",
            "message": f"Ошибка при удалении события: {str(e)}"
        }), 400

@app.route('/events/update/<int:event_id>/<uuid>', methods=['PUT'])
def updateUserEvent(uuid, event_id):
    try:
        event = Event.query.filter_by(uuid=uuid, id=event_id).first()
        if event:
            data = request.get_json()
            event.eventTitle = data['eventTitle']
            event.eventDesc = data['eventDesc']
            event.eventTime = data['eventTime']
            db.session.commit()
            return jsonify({"status": "success", "message": "Событие успешно обновлено"})
        return jsonify({"status": "error", "message": "Событие не найдено"}), 404
    except Exception as e:
        print(f"Ошибка при обновлении события: {str(e)}")
        return jsonify({"status": "error", "message": f"Ошибка при обновлении события: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(debug=True)