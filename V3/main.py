from flask import Flask, render_template, request, jsonify
from requests import get
from database import conectToDB, addRow, getRows, addRowIFnotExist







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

    data = request.get_json()
    print(data)
    addRow(GMeinCursor, Gconn, data['Gjmeno'], data['pamatovani_Pi'], data['pamatovani_E'], data['pamatovani_Fi'], Gip)

    return dekuji()

@app.route('/dekuji')
def dekuji():
    return render_template('dekuji.html')

@app.route('/api/ip', methods=['POST'])
def handleIP():
    global Gip, Gconn, GMeinCursor


    data = request.get_json()
    #print('doing something')
    # Access the username and email parameters sent from the frontend
    ip = data.get('ip')
    Gip = ip
    
    addRowIFnotExist(GMeinCursor, Gconn, Gip)
    return ip



if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    #app.run(debug=True, host='0.0.0.0')
    

