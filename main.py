from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/formularionotas', methods=['GET', 'POST'])
def formularionotas():
    if request.method == 'POST':
        nota1 = int(request.form['Nota1'])
        nota2 = int(request.form['Nota2'])
        nota3 = int(request.form['Nota3'])
        asistencia = int(request.form['Asistencia'])
        promedio = int((nota1 + nota2 + nota3)/3)

        if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70):
            mensaje_notas = "Las notas deben estar entre 10 y 70"
            return render_template('formularionotas.html', nota1=nota1, nota2=nota2, nota3=nota3, asistencia=asistencia, mensaje_notas=mensaje_notas)

        if not (0 <= asistencia <= 100):
            mensaje_asistencia = "La asistencia debe ser un número entre 0 y 100"
            return render_template('formularionotas.html', nota1=nota1, nota2=nota2, nota3=nota3, asistencia=asistencia, mensaje_asistencia=mensaje_asistencia)

        if promedio >= 40 and asistencia >= 75:
            estado = 'APROBADO'
        else:
            estado = "REPROBADO"

        return render_template('formularionotas.html', nota1=nota1, nota2=nota2, nota3=nota3, asistencia=asistencia, promedio=promedio, estado=estado)

    return render_template('formularionotas.html')

@app.route('/formularionombres', methods=['GET', 'POST'])
def formularionombres():
    if request.method == 'POST':
        nombre1 = request.form['txtNombre1']
        nombre2 = request.form['txtNombre2']
        nombre3 = request.form['txtNombre3']
        if len(nombre1) > len(nombre2) and len(nombre1) > len(nombre3):
            resultado = nombre1
            cant_caracteres = len(nombre1)
        elif len(nombre2) > len(nombre1) and len(nombre2) > len(nombre3):
            resultado = nombre2
            cant_caracteres = len(nombre2)
        else:
            resultado = nombre3
            cant_caracteres = len(nombre3)

        return render_template('formularionombres.html', nombre1=nombre1, nombre2=nombre2, nombre3=nombre3, resultado=resultado, cant_caracteres=cant_caracteres)
    return render_template('formularionombres.html')

if __name__ == '__main__':
    app.run(debug=True)