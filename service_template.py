import argparse
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


def get_parser():
    """Parse the CLI args."""
    parser = argparse.ArgumentParser(description="Configurable TTS service runner")
    parser.add_argument("--ip", type=str, default="0.0.0.0")
    parser.add_argument("--port", '-p', default="5000")
    return parser

#Hit post endpoint on the given ip/port, can be changed
@app.route('/post', methods=['POST'])
def post_route():
    '''Your code here'''

    if request.method == 'POST':
        data = request.get_json(force=True)
        image=data['data']
        data_dict = {'class':"category"}   
        return jsonify(data_dict)

if __name__ == "__main__":
    args = get_parser().parse_args()
    app.run(debug=True,host=args.ip,port=args.port)
