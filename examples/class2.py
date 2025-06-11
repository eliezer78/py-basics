### Herencia múltiple
class Estudiante:
    def __init__(self,nombrecompleto,carrera,legajo):
        self.nombrecompleto = nombrecompleto 
        self.carrera = carrera 
        self.__legajo = legajo 
            
    def obtener_legajo(self):
        return self.__legajo
        
class Deportista:
    def __init__(self,apodo,disciplina,nivel):
        self.apodo = apodo
        self.disciplina = disciplina
        self.__nivel = nivel
        
    def obtener_nivel(self):
        return self.__nivel
class MathAtleta(Estudiante,Deportista):
    def __init__(self,nombrecompleto,carrera,legajo,apodo,disciplina,nivel,horarios):
        Estudiante.__init__(self,nombrecompleto,carrera,legajo)
        Deportista.__init__(self,apodo,disciplina,nivel)
        self.horarios = horarios
        
    def mostrar_informacion(self):
        return f"Nombre: {self.nombrecompleto}, \nCarrera: {self.carrera}, \nLegajo: {self.obtener_legajo()}, \nApodo: {self.apodo}, \nDisciplina: {self.disciplina}, \nNivel: {self.obtener_nivel()}, \nHorarios: {', '.join(self.horarios)}"  
        
estudiante = Estudiante("Lionel Messi","Letras",123456)
print(estudiante.nombrecompleto)
print(estudiante.carrera)
# print(estudiante.__legajo)
print(estudiante.obtener_legajo())

matleta = MathAtleta("Rodrigo De Paul","Sistemas",64238764,"Motorcito","Fútbol","Profesional",["lunes","miercoles","viernes"])
print(matleta.mostrar_informacion())

"""
class CuentaBancaria:
    def __init__(self, cliente, tipo, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado
        self._tipo = tipo # Atributo protegido
        self.cliente = cliente # Atributo público
        
    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            return True
        return False

    def obtener_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria("Lopez", "CC", 1000)
cuenta.depositar(500)
print(cuenta.obtener_saldo()) # 1500
cuenta.retirar(300)
print(cuenta.obtener_saldo()) # 1200
"""
# No se puede acceder directamente al saldo:
# print(cuenta.__saldo)  # Error: AttributeError