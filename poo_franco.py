class Golondrina:
  def __init__(self, energia):          #INIT es para definir los estados.
    self.energia = energia            #ENERGIA no es un metodo, este seria el estado de la golondrina o un atributo

  def comer_alpiste(self, gramos):      #self es lo mismo que decir pepita'nombre del ave'
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_debil(self):    #si tiene menos de 10 de energia que diga true.
    if self.energia <= 10:
      return True
    else:
      return False  
      
  def esta_feliz(self):
    if self.energia > 500:
      return True
    else: 
      return False
class Dragon:     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10

pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)