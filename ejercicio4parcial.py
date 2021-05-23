class Titan:
    def _init_(self, vida):
        self.vida = vida
    
    def recibir_ataque(self, puntos):
        self.vida -= puntos * 1.5
    
    def salud_actual(self):
        return self.vida
    
    def cuantas_casas(self):
        return self.vida * 0.06
    
    def esta_vivo(self):
        if self.vida <= 0:
            return False
        else:
            return True
    
    def grito(self):
        print("¡Aaaarrrg!")

class Supertitan(Titan):
    def _init_(self, vida):
        self.vida = vida
    
    def recuperarse(self, tiempo):
        self.vida += (tiempo*(20/15))


print('coso')
