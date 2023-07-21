class alumnos:
    def __init__(self,nombre,apellido,edad,nacionalidad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.notaAlumno=''
        self.nacionalidad=nacionalidad

    def leerNota(self):
        return self.notaAlumno

    def registrarNota(self, notaAlumno):      
        while True:
            if notaAlumno.isdecimal():  
                notaAlumno = int(notaAlumno)
                if 0 <= float(notaAlumno) <= 20:                  
                    self.notaAlumno = notaAlumno
                    break
                else:
                    print("La nota debe estar en un rango de 0 a 20.")
            else:
                print("La nota debe ser un número.")
            notaAlumno = input("Ingrese nuevamente la nota del alumno: ")  


        






















