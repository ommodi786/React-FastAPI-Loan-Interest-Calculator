# Simple Loan Interest Calculator

This project is a simple and interactive Loan Interest Calculator developed using React.js and FastAPI. It helps users quickly calculate the simple interest and total repayment amount by entering the loan amount, interest rate, and loan duration.

The application demonstrates how a React frontend can communicate with a FastAPI backend through REST APIs, making it a great beginner-friendly full-stack project.

## Features

* Calculate simple loan interest instantly
* Clean and responsive user interface
* FastAPI-powered backend services
* Real-time results
* Easy-to-use form inputs
* Frontend and backend integration using APIs

## Technologies Used

### Frontend

* React.js
* Axios
* CSS

### Backend

* FastAPI
* Python
* Uvicorn

## Interest Formula

Simple Interest = (Principal × Rate × Time) / 100

## Project Structure

```text
loan-interest-calculator/
├── frontend/
│   ├── src/
│   └── package.json
├── backend/
│   ├── main.py
│   └── requirements.txt
└── README.md
```

## Getting Started

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## API Endpoint

### POST /calculate

Request:

```json
{
  "principal": 100000,
  "rate": 10,
  "time": 2
}
```

Response:

```json
{
  "interest": 20000,
  "total_amount": 120000
}
```

## Purpose

The goal of this project is to understand full-stack web development by connecting a React frontend with a FastAPI backend and performing real-time calculations through API requests.

## Author

Om Modi
