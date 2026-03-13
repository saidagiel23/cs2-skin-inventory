CS2 Skin Inventory Tracker (V1.5)

A Python CLI application to manage and track Counter-Strike 2 skin trading inventory.

This tool allows traders to store their skins, calculate profit, and automatically update market prices.

Features

- Add skin to inventory
- Show all skins in database
- Search skins by name
- Update skin information
- Delete skins from inventory
- Sort skins by profit
- Inventory summary (total skins, total profit, average profit)
- JSON file database
- Automatic Steam Market price update

Technologies Used

- Python
- JSON database
- Steam Market API

How It Works

1. Add skins to your inventory with purchase price.
2. Update market price using the Steam Market API.
3. The program automatically calculates profit for each skin.
4. View summary statistics and sort skins by profitability.

Project Structure

cs2-skin-inventory
│
├── main.py
├── inventory.json
├── README.md
└── requirements.txt

Future Development

- Portfolio value tracker
- Top profitable skins
- Price comparison between markets
- Web dashboard
- REST API backend

Author

Personal learning project for Python backend development and trading tools for Counter-Strike 2 skins.