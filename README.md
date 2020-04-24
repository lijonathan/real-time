# Real Time Project

CSE 520 - Real Time Systems
  - Justin Marshall
  - Jeremy Manin
  - Jonathan Li

# Directory Structure

  - real-time/certs
  - real-time/glove
  - real-time/learn
  - real-time/webapp/backend
    - python scripts that are triggered by the javascript functions to subscribe and trigger the application
  - real-time/webapp/public
    - /css - custom styles outside Bootstrap library
    - /js - Javascript functions called from the HTML
    - index.html - main webpage
    - hand_data.txt -  written to during the subscription process
  - server.js - Node,js launches this script which creates a node for the app to run on


# Prerequistes

### Front End
  - Node,js
  - Other dependencies run the following
     ```
     $ npm install jquery semantic-ui-css handlebars vanilla-router express dotenv axios
     ```

### Backend
   - In the cmd prompt navigate to \real-time\web-app\backend
        ```
        pip install flask
        pip install flask-cors
        pip install AWSIoTPythonSDK
        ```
   
# Starting App

### Front End
  - Navigate to the following path and run the below command
   ```
   ~/real-time/web-app
   $ node server.js or npm start
   ```
  - App will run on http://localhost:8080/
 
 ### Backend
   - Navigate to the following path and run the below commands
   ```
   ~/real-time/web-app/backend
   set FLASK_APP=backend.py
   flask run
   ```
