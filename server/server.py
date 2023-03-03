from flask  import Flask, request, jsonify

import util
from gevent.pywsgi import WSGIServer

app = Flask(__name__)



@app.route('/classify_image',methods=['GET','POST'])
def classify_image():
    image_data = request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def index():
    return "hi"



if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classifi cation")
    util.load_saved_artifacts()
    #print(util.classify_image(None, "./test_images/messi1.jpg"))
    #print(util.classify_image(util.get_b64_test_image_for_cris(), None))
    app.run(port=5000)

    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()