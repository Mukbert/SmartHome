from flask import Flask, render_template

try:
    from devices import steps
except:
    class X:
        def run(self, action):
            print("Run:", action)

        def actions(self):
            return ["Rainbow", "Pong"]
    steps = X()

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