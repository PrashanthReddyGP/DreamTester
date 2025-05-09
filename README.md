# DreamTester
Crypto Trade Backtesting Application

## REQUIREMENTS
- python
- binance account (api, secret)
- git
- pip

## INSTALLATION GUIDE
Open up the terminal and type the following command:

    git clone https://github.com/PrashanthReddyGP/DreamTester.git

    cd DreamTester

    python -m venv .venv // Optional: If you want to keep your dependencies organized. Create a new Virtual Environment

    .venv\scripts\activate // Optional: Activate the created Virtual Environment

    pip install -r requirements.txt

Create a .env file and add the following:

    BINANCE_API = 'your_api_key'

    BINANCE_SECRET = 'your_api_secret'

Now run the main.py file by typing the following in your terminal:

    python main.py

## Phase 1: Setup
- [x] Initialize Git repository
- [x] Create GitHub repository
- [x] Push v1 to Git Repo

## Phase 2: Development
- [ ] Add multi-strategy files selection/import
- [ ] Add "Script Editor" editing features
    - [ ] Strategy Selection
    - [ ] Save and Save As options

## Phase 3: Docker Deployment
- [ ] Modify the codebase to migrate to Docker Setup