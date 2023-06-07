from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    
'''
1) - Se importa la clase Flask del módulo flask: from flask import Flask. Esto permite utilizar las funcionalidades de Flask en nuestro programa.
2) - Se crea una instancia de la clase Flask y se asigna a la variable app: app = Flask(__name__). La instancia de Flask se utiliza para configurar y ejecutar la aplicación web.
3) - Se define una ruta de URL utilizando el decorador @app.route('/'). El decorador @app.route() se utiliza para asociar una función a una ruta específica. En este caso, la ruta '/' se asocia a la función home().
4) - Se define la función home() que se ejecutará cuando se acceda a la ruta '/'. En este ejemplo, simplemente devuelve el mensaje 'Hello World!'.
5) - Se define otra ruta de URL utilizando el decorador @app.route('/about'). En este caso, la ruta '/about' se asocia a la función about().
6) - Se define la función about() que se ejecutará cuando se acceda a la ruta '/about'. En este ejemplo, devuelve el mensaje 'About Page'.
7) - El bloque if __name__ == '__main__': se utiliza para asegurarse de que el servidor web se ejecute solo cuando se ejecute este archivo directamente (no cuando se importe en otro archivo). Dentro de este bloque, se llama al método app.run() para ejecutar el servidor web en modo de desarrollo.
'''