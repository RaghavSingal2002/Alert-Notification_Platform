Alert & Notification Platform 📣
Overview
This project is a lightweight and extensible alerting and notification platform designed to provide timely and targeted communication within an organization. It's built to solve the common problem of missed or overwhelming notifications by giving both administrators and users control. The system is designed with a strong focus on clean Object-Oriented Programming (OOP) principles, ensuring it's modular, scalable, and easy to maintain.

✨ Key Features
Configurable Alerts: Admins can create alerts with a title, message, and severity level (Info 🟢, Warning 🟡, Critical 🔴).

Granular Visibility: Alerts can be precisely targeted to the entire organization 🏢, specific teams 👥, or individual users 👤.

Smart Reminders: The system features a persistent reminder logic that re-sends alerts every two hours until a user explicitly snoozes it for the day or the alert expires.

User Control: End users can receive relevant alerts, mark them as read/unread, and snooze them for the day.

Extensible Architecture: The core design is built to be easily extended to support future features, such as new delivery channels (e.g., Email 📧, SMS 📱) or custom reminder frequencies.

🧠 Technical Design and Principles
The platform's architecture is built on a foundation of proven software design patterns to ensure robustness and extensibility.

Observer Pattern: This pattern is used for user subscription management. An Alert acts as the Subject, and Users act as Observers. When an alert is updated or triggered, it notifies all its subscribed users without being tightly coupled to their specific implementation.

Strategy Pattern: Notification delivery is handled using the Strategy Pattern. The system defines a DeliveryStrategy interface, and each delivery method (like InAppDelivery) implements this interface. This design allows for new delivery channels to be added seamlessly without altering the core alert management logic.

OOP Principles: The codebase adheres to core OOP principles like Encapsulation, Abstraction, and the Single Responsibility Principle (SRP), resulting in clean, readable, and maintainable code.
