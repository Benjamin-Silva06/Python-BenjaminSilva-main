class Usuario:

    def __init__(self , name, email_address,balance_cuenta):
        self.name = name
        self.email = email_address
        self.balance_cuenta = balance_cuenta
        
    def hacer_depósito(self,amount):   # toma un argumento que es el monto del depósito
        self.balance_cuenta += amount   # la cuenta del usuario específico aumenta en la 


    def hacer_deposito(self,amount):
        self.balance_cuenta += amount
        return self

    def hacer_giro(self,amount):
        self.balance_cuenta -= amount


guido = Usuario("guido","email@email",0)
benja = Usuario("benja","@email",20)

guido.hacer_depósito(150)
benja.hacer_depósito(150)
print("el usuario",guido.name,"tiene en su cuenta",guido.balance_cuenta)

guido.hacer_giro(150)
print("el usuario", guido.name,"disminuyo a",guido.balance_cuenta)
print("el usuario",benja.name,"tiene en su cuenta",benja.balance_cuenta)