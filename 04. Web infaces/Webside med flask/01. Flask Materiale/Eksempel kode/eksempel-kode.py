#Terminal: sudo pip3 install flask

from flask import Flask, render_template

navne = ['Bob', 'Tyron', 'Stephen']
test = 'Test'


app = Flask(__name__)

@app.route('/') # roden af websiden Eks.: dr.dk <- http://dr.dk/index.html

def index():
    # Viser HTML kode
    return """
        <h1>Overskrift</h1>
        <h2>Overskrift 2</h2>
        <p>Afsnit</p>
        <ul>
            <li>Emne 1</li>
            <li>Emne 2</li>
        </ul>
        <a href="/data">Link</a>
        <p>{{test}}</p>
    """
@app.route('/data') # Ny data side

def data():
    return render_template('data.html', name='Bob', len=len(navne), navne=navne)

if __name__ == '__main__':
    # Server: mig-selv-ip: localhost <- 127.0.0.1
    # HTTP <- 80, HTTPS <-443
    app.run(debug=True, host='127.0.0.1')