import flask
import os
# this requires the lib flask installed
# pip3 install flask
# import json

app = flask.Flask(__name__)

@app.route("/escritorio/")
@app.route("/escritorio/<string:action>")
def office(action = "list"):
    print("the application is running")
    if (action == "list"):
        file = open("state.txt", "r")
        state_light = eval(file.read().strip())
        # print(state_light)
        return { "lights": state_light }
    if (action == "on"):
        file = open("state.txt", "w")
        file.write("True")
        return { "error": False, "message": "ok" }
    if (action == "off"):
        file = open("state.txt", "w")
        file.write("False")
        return { "error": False, "message": "ok" }
    return { "error": True, "message":  "option not found" }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
