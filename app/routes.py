from . import app,db
from .models import Medico, Paciente, Consultorio, Cita
from flask import render_template, request, flash, redirect
from datetime import datetime, time


#crear ruta para ver los medicos
@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html" , medicos=medicos)

@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html" , pacientes=pacientes)

@app.route("/consultorios")
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template("consultorios.html" , consultorios=consultorios)

@app.route("/citas")
def get_all_citas():
    citas = Cita.query.all()
    return render_template("citas.html" , citas=citas)


@app.route("/medicos/<int:id>")
def get_medico_by_id(id):
    medico = Medico.query.get(id)
    return render_template("medico.html",
                            med = medico )

@app.route("/pacientes/<int:id>")
def get_paciente_by_id(id):
    paciente = Paciente.query.get(id)
    return render_template("paciente.html",
                           pac = paciente )
    
@app.route("/consultorios/<int:id>")
def get_consultorio_by_id(id):
    consultorio = Consultorio.query.get(id)
    return render_template("consultorio.html",
                           con = consultorio)
    
@app.route("/citas/<int:id>")
def get_cita_by_id(id):
    cita = Cita.query.get(id)
    return render_template("cita.html",
                           cit = cita)

#--------------------------------------------------------------------------------------------------------------------------------#

#crear ruta para crear nuevo medico
@app.route("/medicos/create" , methods = [ "GET" , "POST"] )
def create_medico():
    ####### mostrar el formulario : get ###########
    if( request.method == "GET" ):
        #el usuario ingreso con navegador con https://localhost.....
        especialidades = [
            "Cardiologia",
            "Pediatria",
            "Oncologia"
        ]
        return render_template("medico_form.html",
                            especialidades = especialidades)
    

#### Cuando el usuario presiona el boton de guardar#####
#### los datos del formulario viajan al servidor
    
    elif(request.method == "POST"):
        #cuando se presiona "guardar"
        new_medico = Medico(nombre = request.form["nombre"],
                            apellido = request.form["apellidos"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion = request.form["ni"],
                            registro_medico = request.form["rm"],
                            especialidad = request.form["es"]
                            )
        #añadirlo a la sesion sqlalchemy
        db.session.add(new_medico)
        db.session.commit()
        flash("medico registrado correctamente")
        return redirect("/medicos")

#Actualizar Medico
@app.route('/medicos/update/<int:id>', methods=['GET','POST'])
def update_medico(id):
    especialidades = [
           "Cardiologia",
            "Pediatria",
            "Oncologia",
            "Urologa"
    ]
    medico_update = Medico.query.get(id)
    
    if(request.method == 'GET'):
        return render_template('medico_update.html' , 
                                medico_update = medico_update, 
                                especialidades=especialidades)
    elif(request.method == 'POST'):
        #actualizar el medico con los datos del formulario
        medico_update.nombre = request.form['nombre']
        medico_update.apellido = request.form['apellidos']
        medico_update.tipo_identificacion = request.form['ti']
        medico_update.numero_identificacion = request.form['ni']
        medico_update.registro_medico = request.form['rm']
        medico_update.especialidad = request.form['es']
        db.session.commit()
        return redirect('/medicos')
    
# Eliminar Medico
@app.route('/medicos/delete/<int:id>', methods=['GET','POST'])
def delete_medico(id):
    medico_delete = Medico.query.get(id)
    db.session.delete(medico_delete)
    db.session.commit()
    return redirect('/medicos')
    
#--------------------------------------------------------------------------------------------------------------------------------#

#crear ruta para crear nuevo paciente
@app.route("/pacientes/create" , methods = [ "GET" , "POST"] )
def create_paciente():
    ####### mostrar el formulario : get ###########
    if( request.method == "GET" ):
        #el usuario ingreso con navegador con https://localhost.....
        tipo_sangres = [
            "A+",
            "O+",
            "A-",
            "O-",
            "AB+",
            "AB-"
        ]
        return render_template("paciente_form.html",
                            tipo_sangres = tipo_sangres)
    

#### Cuando el usuario presiona el boton de guardar#####
#### los datos del formulario viajan al servidor
    
    elif(request.method == "POST"):
        #cuando se presiona "guardar"
        new_paciente = Paciente(nombre = request.form["nombre"],
                            apellido = request.form["apellido"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion = request.form["ni"],
                            altura = request.form["al"],
                            tipo_sangre = request.form["rh"]
                            )
        #añadirlo a la sesion sqlalchemy
        db.session.add(new_paciente)
        db.session.commit()
        flash('Paciente creado')
        return redirect('/pacientes')
    
#Actualizar Paciente
@app.route('/paciente/update/<int:id>', methods=['GET','POST'])
def update_paciente(id):
    tipo_sangres = [
            "A+",
            "O+",
            "A-",
            "O-",
            "AB+",
            "AB-"
        ]
    paciente_update = Paciente.query.get(id)
    
    if(request.method == 'GET'):
        return render_template('paciente_update.html' , 
                                paciente_update = paciente_update, 
                                tipo_sangres=tipo_sangres)
    elif(request.method == 'POST'):
        #actualizar el paciente con los datos del formulario
        paciente_update.nombre = request.form['nombre']
        paciente_update.apellido = request.form['apellido']
        paciente_update.tipo_identificacion = request.form['ti']
        paciente_update.numero_identificacion = request.form['ni']
        paciente_update.altura = request.form['al']
        paciente_update.tipo_sangre = request.form['rh']
        db.session.commit()
        flash('Paciente Actualizado')
        return redirect('/pacientes')
    
#Eliminar Paciente
@app.route('/pacientes/delete/<int:id>', methods=['GET','POST'])
def delete_paciente(id):
    paciente_delete = Paciente.query.get(id)
    db.session.delete(paciente_delete)
    db.session.commit()
    flash('Paciente Eliminado')
    return redirect('/paciente')


#------------------------------------------------------------------------------------------------------------------------#
    
#crear ruta para crear nuevo consultorio
@app.route("/consultorios/create" , methods = [ "GET" , "POST"] )
def create_consultorio():
    ####### mostrar el formulario : get ###########
    if( request.method == "GET" ):
        numero = Consultorio.query.all()
        return render_template("consultorio_form.html", numero = numero)
#### Cuando el usuario presiona el boton de guardar#####
#### los datos del formulario viajan al servidor
    elif(request.method == "POST"):
        #el usuario ingreso con navegador con https://localhost.....
        numero = int(request.form["nu"])
        new_consultorio = Consultorio( numero = request.form["nu"])                            
        #añadirlo a la sesion sqlalchemy
    db.session.add(new_consultorio)
    db.session.commit()
    flash('Consultorio creado')
    return redirect('/consultorios')

#Actualizar Consultorio
@app.route('/consultorios/update/<int:id>', methods=['GET','POST'])
def update_consultorio(id):
    consultorio_update = Consultorio.query.get(id)
    if(request.method == 'GET'):
        return render_template('consultorio_update.html', consultorio_update = consultorio_update)
    elif(request.method == 'POST'):
        consultorio_update.numero = request.form['num']
        db.session.commit()
        flash('Consultorio Actualizado')
        return redirect('/consultorios')

#Eliminar Consultorio
@app.route('/consultorios/delete/<int:id>', methods=['GET','POST'])
def delete_consultorio(id):
    consultorio_delete = Consultorio.query.get(id)
    db.session.delete(consultorio_delete)
    db.session.commit()
    flash('Consultorio Eliminado')
    return redirect('/consultorios')
#--------------------------------------------------------------------------------------------------------------------------------#
#Crear Citas
@app.route("/citas/create", methods = ['GET', 'POST'])
def show_create_cita():
    if(request.method == 'GET'):
        valores = [
           4500,
            0,
            20000]
        fecha = datetime.now()
        pacientes = Paciente.query.all()
        medicos = Medico.query.all()
        consultorios = Consultorio.query.all()
        return render_template("cita_form.html" , pacientes=pacientes , medicos=medicos, consultorios=consultorios, valores = valores, fecha = fecha )
    
    
    elif(request.method == 'POST'):
        fecha = datetime.strptime(request.form['fecha'], "%Y-%m-%dT%H:%M")
        new_cita = Cita(fecha=fecha,
                        paciente_id = request.form['pa'],
                        medico_id = request.form['med'],
                        consultorio_id = request.form['con'],
                        valor = request.form['val'])
        db.session.add(new_cita)
        db.session.commit() 
        flash('cita creada')
        return redirect('/citas')


#Actualizar Citas
@app.route('/citas/update/<int:id>', methods=['GET','POST'])
def update_cita(id):
    valores = [
           4500,
            0,
            20000]
    cita_update = Cita.query.get(id)
    
    
    if(request.method == 'GET'):
        pacientes = Paciente.query.all()
        medicos = Medico.query.all()
        consultorios = Consultorio.query.all()
        return render_template('cita_update.html' , 
                                cita_update = cita_update, 
                                valores = valores, pacientes = pacientes, medicos = medicos, consultorios = consultorios)
    elif(request.method == 'POST'):
        #actualizar el paciente con los datos del formulario
        
        cita_update.fecha = datetime.strptime(request.form['fecha'], "%Y-%m-%dT%H:%M")
        cita_update.paciente_id = request.form['pa']
        cita_update.medico_id = request.form['med']
        cita_update.consultorio_id = request.form['con']
        cita_update.valor = request.form['val']
        db.session.commit()
        flash('Cita Actualizado')
        return redirect('/citas')
    
#Eliminar Cita
@app.route('/citas/delete/<int:id>', methods=['GET','POST'])
def delete_cita(id):
    cita_delete = Cita.query.get(id)
    db.session.delete(cita_delete)
    db.session.commit()
    flash('Cita Eliminado')
    return redirect('/citas')
