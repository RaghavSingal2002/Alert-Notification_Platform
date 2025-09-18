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
