# DarkHorse NFL Stock Market

DarkHorse is a full-stack web application that presents NFL players like stocks. It combines player and team information with real NFL performance data to create price history and candlestick charts. The application also includes user signup and login functionality.

The project has two main parts:

- A Python/Flask backend that provides the API, processes NFL data, and stores application data in SQLite.
- A React/TypeScript frontend that provides the user interface and interactive charts.

## Prerequisites

Install the following before setting up the project:

- [Git](https://git-scm.com/)
- Python 3.14
- [Node.js and npm](https://nodejs.org/)

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Saksham-Mandal/NFL-Stock-Market.git
cd NFL-Stock-Market
```

### 2. Create a Python virtual environment

From the project root, create a virtual environment named `.venv`:

```bash
python3.14 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install the backend dependencies

With the virtual environment activated, run:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Install the frontend dependencies

```bash
cd frontend
npm install
cd ..
```

## Initialize the database

The backend uses a local SQLite database. Before starting the application for the first time, run the backend launcher:

```bash
python backend/start_backend.py
```

Enter `i` to create the database and its tables. Run the launcher again, enter `p`, and then enter `tp` to download and populate the team and player data.

The generated database is stored locally at `backend/db/nfl.db` and is not committed to Git.

## Run the application

The backend and frontend need to run at the same time, so use two terminal windows.

### Start the backend

In the first terminal, from the project root:

```bash
source .venv/bin/activate
python backend/start_backend.py
```

Enter `s` when prompted. The Flask API will start at `http://127.0.0.1:5050`.

### Start the frontend

In the second terminal:

```bash
cd frontend
npm run dev
```

Vite will print the local frontend address, normally `http://localhost:5173`. Open that address in a browser.

## How it works

The React frontend requests player, team, and chart data from the Flask API. The backend reads player and team records from SQLite and uses NFL performance data to generate candlestick values for the selected player. The frontend then displays that information using interactive charts.

The backend also provides signup and login endpoints. Passwords are hashed before they are stored in the local database.

## Useful commands

The `backend/start_backend.py` launcher supports these commands:

- `i` — initialize the SQLite database
- `p` — choose data to populate
- `r` — refresh team and player data
- `c` — clear team and player data
- `s` — start the backend server

To stop either development server, press `Ctrl+C` in its terminal. To leave the Python virtual environment, run `deactivate`.
