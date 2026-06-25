# 🚀 CodeCollab AI

> An AI-Powered Real-Time Collaborative Coding Platform built using FastAPI, React, Monaco Editor, WebSockets, and Google Gemini AI.

![Status](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![License](https://img.shields.io/badge/License-MIT-orange)

---

# 📖 Overview

CodeCollab AI is a full-stack collaborative coding platform that enables developers to write, edit, save, and collaborate on code in real time while receiving AI-powered coding assistance.

The project combines modern web technologies with artificial intelligence to create an interactive software development environment similar to VS Code Live Share with integrated AI support.

---

# ✨ Features Implemented

## 🔐 Authentication

- JWT Authentication
- Secure Login
- User Registration
- Password Hashing using BCrypt
- Protected Routes

---

## 👤 User Management

- User Registration
- Login
- Current User Profile API

---

## 📂 Workspace Management

- Create Workspace
- View Workspaces
- Update Workspace
- Delete Workspace
- Owner-based Authorization

---

## 💻 Code Editor

- Monaco Editor Integration
- Syntax Highlighting
- Multi-file Support
- Persistent Code Storage

---

## 📁 File Management

- Create Files
- Load Files
- Save Files
- Update Existing Files
- SQLite Database Persistence

---

## 🤖 AI Assistant

Integrated Google Gemini AI

Capabilities:

- Explain Code
- Improve Code
- Optimize Logic
- Answer Programming Questions
- AI Code Analysis

---

## ⚡ Real-Time Collaboration

Implemented using FastAPI WebSockets

Features:

- Live Code Synchronization
- Multi-user Workspace Communication

---

## 🗄 Database

SQLite Database

Tables:

- Users
- Workspaces
- Files

---

## 🎨 Frontend

Built using

- React
- Vite
- Tailwind CSS
- Axios
- React Router
- Monaco Editor

---

## ⚙ Backend

Built using

- FastAPI
- SQLAlchemy
- JWT Authentication
- WebSockets
- Pydantic
- Passlib
- Google Gemini API

---

# 🏗 Project Architecture

```
React Frontend
        │
        │ REST APIs
        ▼
FastAPI Backend
        │
        ├──────── SQLite Database
        │
        ├──────── JWT Authentication
        │
        ├──────── Gemini AI
        │
        └──────── WebSockets
```

---

# 📂 Project Structure

```
CodeCollab-AI

backend/
│
├── app/
│   ├── auth/
│   ├── dependencies/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── websocket/
│   ├── database.py
│   └── main.py
│
├── requirements.txt
└── .env

frontend/
│
├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── assets/
│   └── App.jsx
│
└── package.json
```

---

# 🛠 Technologies Used

### Frontend

- React
- Vite
- Tailwind CSS
- Monaco Editor
- Axios
- React Router

### Backend

- FastAPI
- SQLAlchemy
- SQLite
- WebSockets
- JWT
- Passlib
- Pydantic

### AI

- Google Gemini API

---

# 🚀 Current Progress

## ✅ Completed

- User Authentication
- Dashboard
- Workspace CRUD
- File CRUD
- Monaco Code Editor
- AI Assistant
- File Persistence
- JWT Security
- SQLite Database
- WebSocket Foundation
- Multi-file Support

---

# 📅 Upcoming Features

## 🔜 Phase 2

- Route Protection
- Auto Login
- Logout
- Toast Notifications
- Better Error Handling
- Loading Animations
- UI Improvements

---

## 🔜 Phase 3

- Live User Presence
- Workspace Chat
- Live Cursor Tracking
- Online Members
- Notifications

---

## 🔜 Phase 4

- Docker-based Code Execution
- Java Support
- Python Support
- C++ Support
- JavaScript Runtime

---

## 🔜 Phase 5

- GitHub Integration
- Repository Clone
- Push & Pull
- Commit History
- Branch Management

---

## 🔜 Phase 6

Advanced AI Features

- AI Auto Completion
- AI Code Review
- AI Debugging
- AI Documentation
- AI Test Case Generation
- AI Commit Message Generator

---

## 🔜 Phase 7

Deployment

- Docker
- PostgreSQL
- Render
- Vercel
- GitHub Actions
- CI/CD Pipeline

---

# 🎯 Future Vision

Build a modern AI-first collaborative IDE combining the best features of:

- VS Code
- GitHub
- GitHub Copilot
- ChatGPT
- Replit
- VS Live Share

---

# 👩‍💻 Developer

**P. Vaishnavi**

B.Tech Electronics and Computer Engineering

VIT Chennai

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.
