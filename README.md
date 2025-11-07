# Warehouse Scale Automation

Automate the paint weighing process in a production warehouse using Python, Wi-Fi, and RS232 communication.

##  Overview
This project aims to digitize and automate the process of tracking paint usage in a production environment. It connects an industrial scale via a Wi-Fi gateway to a tablet app and a central server with a database.

## Technologies
- Python 3.x
- Flask (for server-side API)
- SQLite (local data storage)
- MQTT / HTTP (for communication)
- Wi-Fi RS232 Gateway (Kern FCB 12K1 scale)

##  Status
 Building scale simulation script for testing and figuring out the logic

##  How to Run
```bash
pip install -r requirements.txt
python src/scale_reader.py
```

## Author
Stefan Babic  
[GitHub](https://github.com/stefan-devb)
