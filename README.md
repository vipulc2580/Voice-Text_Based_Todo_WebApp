# 📝 Voice & Text Based To-Do Web Application
A dynamic and intuitive To-Do web application that allows users to manage tasks using both voice commands and text input. Built with Django and integrated with the Web Speech API, this application enhances productivity by enabling hands-free task management.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Acknowledgements](#acknowledgements)

## Introduction

The Voice & Text Based To-Do Web Application is designed to enhance productivity by allowing users to add and manage tasks using either voice commands or traditional text input. Leveraging modern web technologies, this application offers a responsive and user-friendly interface, ensuring accessibility across various devices.

## Features
- User Authentication & Authorization  
- Dual Input Modes: Add tasks using voice commands or text input.
- Real-Time Voice Recognition: Utilizes the Web Speech API for accurate and immediate transcription.
- Task Management: Create, view, and manage your to-do items efficiently.
- Responsive Design: Optimized for desktops, tablets, and smartphones.
- User-Friendly Interface: Clean and intuitive UI for seamless user experience.

## Technologies Used
- **Frontend:**
  - HTML5
  - CSS3
  - JavaScript (ES6)
  - Bootstrap

- **Backend:**
  - Python 3.x
  - Django Framework

- **APIs & Libraries:**
  - Web Speech API (for voice recognition)

- **Database:**
  - SQLite (default Django database)

## Installation & Setup
 ### 1. Clone the Repository:
   ```bash
        git clone https://github.com/vipulc2580/Voice-Text_Based_Todo_WebApp.git
        cd Voice-Text_Based_Todo_WebApp
  ```

### 2. Create and Activate a Virtual Environment:
 ```bash
      python3 -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies:
```bash
      pip install -r requirements.txt
```

### 4. Apply Migrations:
```bash
      python manage.py migrate
```

### 5. Run the Development Server:
```bash
      python manage.py runserver
```

### 6. Access the Application:
 Open your web browser and navigate to http://127.0.0.1:8000/

## Usage

### 🧑‍💼 User Journey:
  - Add Tasks: Use the text input field or click on the microphone icon to add tasks via voice.
  - View Tasks: All added tasks are displayed in a list format.
  - Manage Tasks: Mark tasks as completed or delete them as needed.

### 🎤 Voice Input Functionality:
  - Microphone Activation: Click on the microphone icon to start voice recognition.
  - Speech Transcription: Your spoken words are transcribed into text and populated into the task input field.
  - Task Addition: Submit the transcribed text to add it as a new task.
  - **Note:** Ensure your browser supports the Web Speech API (e.g., Google Chrome) and that microphone permissions are granted.

## Screenshots
![Todo Banner Home](https://github.com/vipulc2580/Voice-Text_Based_Todo_WebApp/blob/main/screenshots/homePage.png)  
![Todo Banner User DashBoard](https://github.com/vipulc2580/Voice-Text_Based_Todo_WebApp/blob/main/screenshots/user_dashbaord.png)

## Acknowledgements
Thanks to the developers and contributors of Django, Bootstrap, and the Web Speech API.

Gratitude to the open-source community for continuous support and inspiration.

