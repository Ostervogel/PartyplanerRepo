#!/bin/bash
export FLASK_DEBUG=0
export FLASK_APP=main.py
python3 -m flask run --host=0.0.0.0 --port=80
