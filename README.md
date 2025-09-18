🚨 Alert & Notification Platform
📌 Project Overview

The Alert & Notification Platform is a real-time system designed to manage, distribute, and monitor alerts within an organization. It ensures that critical information such as system downtimes, policy updates, or urgent announcements, is delivered promptly to the right audience.

This project demonstrates scalable backend design using FastAPI, role-based access control (RBAC), and real-time notification delivery, making it highly suitable for enterprise-grade alerting systems.

🎯 Features

Admin Functionality

Create, update, and delete alerts

Define severity levels (Info, Warning, Critical)

Set visibility (Global, Department, Individual)

Monitor delivery status

User Functionality

Receive alerts based on role and department

View history of past alerts

Mark alerts as read/unread

Filter alerts by severity or category

System Features

Role-based Access Control (RBAC)

Priority handling for critical alerts

REST API endpoints with auto-generated Swagger UI

Modular, scalable architecture

🏗️ Architecture

Backend: FastAPI (Python)

Database: SQLite (can be extended to PostgreSQL/MySQL)

Authentication: Role-based access for Admin/User

API Testing: Swagger UI, Postman

Future Enhancements: WebSockets/Push notifications for real-time alerts

🛠️ Technologies Used

FastAPI – High-performance Python framework

Uvicorn – ASGI server for running FastAPI apps

SQLite – Lightweight database

Python – Core programming language

Swagger UI – Auto-generated API documentation

⚡ Project Workflow

Admin logs in → Creates alert with severity & visibility

System stores alert → Routes it based on RBAC rules

Users receive alerts → Can filter, mark as read/unread

Admin monitors status → Ensures delivery & acknowledgment

System stores alert → Routes it based on RBAC rules

Users receive alerts → Can filter, mark as read/unread

Admin monitors status → Ensures delivery & acknowledgment

🚀 Installation & Setup

Clone the repository:

git clone https://github.com/your-username/alert-notification-platform.git
cd alert-notification-platform


Create a virtual environment & install dependencies:

python -m venv venv
source venv/bin/activate   # On Windows use venv\Scripts\activate
pip install -r requirements.txt


Run the server:

uvicorn app: app --reload


Open API docs at:

http://127.0.0.1:8000/docs

📊 Example API Calls

Create Alert (Admin)

POST /admin/alerts


Request Body:

{
  "title": "Server Down",
  "message": "Database connection lost",
  "severity": "Critical",
  "visibility": "Global"
}

Fetch Alerts (User)

GET /user/{user_id}/alerts

📌 Future Scope

Real-time push notifications using WebSockets

Integration with Slack/Email/SMS APIs

Advanced analytics dashboard

Multi-language support

📜 License

This project is licensed under the MIT License.
