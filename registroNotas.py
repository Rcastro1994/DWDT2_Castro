from alumnos import *

print("Bienvenidos al registro de notas elaborado por el Alumno Renzo Castro")

if __name__=='__main__':
    notasSistemas = []
    comandosSistema = ['R','C','P','S', 'M', 'X']
    while True:
        comandoInformacion = input("Ingrese comando : ")
        #print(f"El comando ingresado es {comandoInformacion}")
        if comandoInformacion in comandosSistema:
            if comandoInformacion == 'R':
                print(f"Se selecciono el comando {comandoInformacion} donde se registrara un nuevo alumno: ")
                nombre = input("Ingrese el nombre del alumno: ")
                apellido = input("Ingrese el apellido del alumno: ")
                edad = input("Ingrese la edad del alumno: ")
                nacionalidad = input("Ingrese la nacionalidad del alumno: ")
                objAlumno = alumnos(nombre,apellido,edad,nacionalidad)
                notasSistemas.append(objAlumno)
                print(f"Comando {comandoInformacion} finalizado, se registro el alumno")
            elif comandoInformacion == 'C':                                
                print(f"Se selecciono el comando {comandoInformacion} donde se registrara las notas de los alumnos: ")
                alumnosCantidad = 0
                for alumnoInfo in notasSistemas:
                    alumnosCantidad = alumnosCantidad + 1
                    if alumnoInfo.notaAlumno == '':
                        notaAlumno = input(f"Alumno {alumnoInfo.nombre} {alumnoInfo.apellido}, Ingrese nota : ")
                        alumnoInfo.registrarNota(notaAlumno)
                print(f"Comando {comandoInformacion} finalizado, se registraron las notas de los {alumnosCantidad} alumnos ")                          
            elif comandoInformacion == 'P':   
                print(f"Se selecciono el comando {comandoInformacion} donde se obtendra el promedio de los alumnos")   
                #cantidadNotas = 0
                cantidadAlumno = 0
                sumaPromedio = 0                
                for alumnoInfo in notasSistemas:                    
                    cantidadAlumno = cantidadAlumno + 1
                    sumaPromedio = sumaPromedio + float(alumnoInfo.notaAlumno)
                print(f"El promedio de notas para {cantidadAlumno} alumno(s) es: {sumaPromedio/cantidadAlumno}")
                print(f"Comando {comandoInformacion} finalizado, se obtuvo el promedio de todas las notas")
            elif comandoInformacion == 'S':
                print(f"Se selecciono el comando {comandoInformacion} donde se obtendra la suma de notas de todos los alumnos registrados") 
                cantidadAlumno = 0
                sumaNota = 0      
                for alumnoInfo in notasSistemas:                    
                    cantidadAlumno = cantidadAlumno + 1
                    sumaNota = sumaNota + float(alumnoInfo.notaAlumno)
                print(f"La Suma de notas de {cantidadAlumno} alumnos es: {sumaNota}")
                print(f"Comando {comandoInformacion} finalizado, se obtuvo la suma de todas las notas")
            elif comandoInformacion == 'M':       
                 print(f"Se selecciono el comando {comandoInformacion} donde se obtendra la información de los alumnos registrados")  
                 i = 0 
                 for alumnoInfo in notasSistemas:
                    i = i + 1
                    print(f"***Mostrando informacion del Alumno {i}***")
                    print(f"Nombre del Alumno : {alumnoInfo.nombre}")
                    print(f"Apellido del Alumno : {alumnoInfo.apellido}")
                    print(f"Edad del Alumno : {alumnoInfo.edad}")
                    print(f"Nota del Alumno : {alumnos.leerNota(alumnoInfo)}")
                    print(f"Nacionalidad del Alumno : {alumnoInfo.nacionalidad}")            
            else:
                print("Comando de finalizacion")
                break
        else:
            print('Comando incorrecto, vuela a ingresarlo')


