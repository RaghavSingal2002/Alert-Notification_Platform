# Alert & Notification Platform.
from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta
from typing import List, Dict
import uuid

app = FastAPI()

# ----------------- MODELS -----------------
class Alert:
    def __init__(self, title, message, severity, visibility, expiry_hours=24):
        self.id = str(uuid.uuid4())
        self.title = title
        self.message = message
        self.severity = severity
        self.visibility = visibility
        self.start_time = datetime.now()
        self.expiry_time = self.start_time + timedelta(hours=expiry_hours)
        self.active = True

class User:
    def __init__(self, user_id, name, team):
        self.id = user_id
        self.name = name
        self.team = team
        self.alert_prefs: Dict[str, Dict] = {}

# ----------------- SAMPLE DATA -----------------
alerts: Dict[str, Alert] = {}
users: Dict[str, User] = {
    "u1": User("u1", "Alice", "Engineering"),
    "u2": User("u2", "Bob", "Marketing"),
}
teams = {"Engineering": ["u1"], "Marketing": ["u2"]}

# ----------------- ADMIN APIS -----------------
@app.post("/admin/alerts")
def create_alert(title: str, message: str, severity: str, visibility: str):
    alert = Alert(title, message, severity, visibility)
    alerts[alert.id] = alert
    return {"message": "Alert created", "alert_id": alert.id}

@app.get("/admin/alerts")
def list_alerts():
    return [vars(alert) for alert in alerts.values()]

# ----------------- USER APIS -----------------
@app.get("/user/{user_id}/alerts")
def get_user_alerts(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    user = users[user_id]
    active_alerts = [
        vars(alert) for alert in alerts.values()
        if alert.active and alert.expiry_time > datetime.now()
    ]
    return active_alerts

@app.post("/user/{user_id}/snooze/{alert_id}")
def snooze_alert(user_id: str, alert_id: str):
    if user_id not in users or alert_id not in alerts:
        raise HTTPException(status_code=404, detail="User or alert not found")
    users[user_id].alert_prefs[alert_id] = {"snoozed": True, "date": datetime.now().date()}
    return {"message": f"User {user_id} snoozed alert {alert_id}"}

@app.post("/user/{user_id}/read/{alert_id}")
def mark_read(user_id: str, alert_id: str):
    if user_id not in users or alert_id not in alerts:
        raise HTTPException(status_code=404, detail="User or alert not found")
    users[user_id].alert_prefs[alert_id] = {"read": True}
    return {"message": f"User {user_id} marked alert {alert_id} as read"}
