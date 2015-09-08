#!/usr/bin/env python

from app import app


""" Register BluePrint here"""

    
app.run(host='0.0.0.0', debug=True, port=5000, threaded=True)  # Start the server
