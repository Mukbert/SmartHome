from flask import Flask, render_template

from devices import steps

#from devices import steps

app = Flask(__name__)

@app.route("/")
def index():
    # Check the current status of lights in the room
    
    return render_template('index.html', actions=steps.actions())
     
@app.route("/<deviceName>/<action>", methods=['POST'])
def action(deviceName, action):    
    steps.run(action)

    return render_template('index.html', actions=steps.actions()), 200

 
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)