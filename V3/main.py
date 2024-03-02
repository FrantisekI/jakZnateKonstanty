from flask import Flask, render_template, request, jsonify
from requests import get
from database import conectToDB, addRow, getRows







#GpiNaCoZna = GPlaceholder_Pi = GeNaCoZna = GPlaceholder_E = GfiNaCoZna = GPlaceholder_Fi = 0
#Gjmeno = 'Anonym'


Gconn, GMeinCursor = conectToDB()
Gip = 'idk'


app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')

@app.route("/konstanty")
def konstanty():
    
    return render_template("konstanty.html")




@app.route("/submit", methods=['POST'])
def submit():
    global Gconn, GMeinCursor, Gip
    #addRow(GMeinCursor, Gconn, Gjmeno, GPlaceholder_Pi, GPlaceholder_E, GPlaceholder_Fi, Gip)

    if request.method == 'POST':
        data = request.get_json()
        print(data)
        addRow(GMeinCursor, Gconn, data['Gjmeno'], data['pamatovani_Pi'], data['pamatovani_E'], data['pamatovani_Fi'], Gip)


    

    return render_template("konstanty.html")


@app.route('/api/ip', methods=['POST'])
def handleIP():
    global Gip, Gconn, GMeinCursor
    if request.method == 'POST':

        data = request.get_json()
        print('doing something')
        # Access the username and email parameters sent from the frontend
        ip = data.get('ip')
        Gip = ip
        
        # Perform any necessary backend processing with the received data
        response_data = {
            'message': 'Data received successfully!',
            'ip': ip,
        }
        
        addRow(GMeinCursor, Gconn, 'just saving IP', 0, 0, 0, Gip)
        return jsonify(response_data)



if __name__ == '__main__':
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True, host='0.0.0.0')
    

