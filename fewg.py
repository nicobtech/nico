def consumoActualPorKm(self):
        if self.rpm > 3000:
            if self.cambio == 1:
                return (self.consumo) * ((self.rpm - 2500) / 500 * 3)
            elif self.cambio == 2:
                return (self.consumo) * ((self.rpm - 2500) / 500 * 2)
            elif self.cambio <= 5:
                return (self.consumo) * ((self.rpm - 2500) / 500 )
        elif self.cambio == 1:
            return (self.consumo * 3)
        elif self.cambio == 2:
            return (self.consumo * 2)
        else:
            return (self.consumo)
