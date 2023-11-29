from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_compras')
def calcularcomprastemplate():
    return render_template('calculocompras.html')

@app.route('/verificar_sesion')
def iniciodesesiontemplate():
    return render_template('iniciosesion.html')



@app.route('/calculocompras', methods=['GET','POST'])
def calculoCompras():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

    total_sin_descuento = cantidad * 9000

    if edad >= 18 and edad <= 30:
        descuento = total_sin_descuento * 0.15
    elif edad > 30:
        descuento = total_sin_descuento * 0.25
    else:
        descuento = 0

    total_a_pagar = total_sin_descuento - descuento

    return render_template('calculocompras.html', nombre=nombre, total_sin_descuento=total_sin_descuento, descuento=descuento, total_a_pagar=total_a_pagar)


@app.route('/iniciosesion', methods=['GET','POST'])
def inicioSesion():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
    if usuario == 'juan' and contrasena == 'admin':
        mensaje = 'Bienvenido administrador juan'
    elif usuario == 'pepe' and contrasena == 'user':
        mensaje = 'Bienvenido usuario pepe'
    else:
        mensaje = 'Usuario o contraseña incorrectos'

    return render_template('iniciosesion.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)


