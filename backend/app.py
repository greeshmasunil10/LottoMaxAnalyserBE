from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
from predictor import main
import os
import base64
 
app = Flask(__name__)
cors = CORS(app)

@app.route('/analyser')
@cross_origin()
def analyser():
    start_year = request.args.get('start_year')
    end_year = request.args.get('end_year')
    main(start_year, end_year)
    with open('NumberFrequencyGraph.png', 'rb') as f:
        image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode('utf-8')
    return {'numberFrequencyGraph': image_b64}

@app.route('/download')
def download():
    # Define the path to the data file
    data_file = os.path.join(app.root_path, 'DrawsDataWithDates.txt')
    
    # Check if the file exists
    if not os.path.exists(data_file):
        return 'Error: Required file not found.'
    
    # Send the file as an attachment for download
    return send_file(data_file, as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 