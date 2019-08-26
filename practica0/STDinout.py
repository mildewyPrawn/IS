import sys

class Animal:
  def __init__(self, kingdom, phylum, clas, order, family, genus, specie):
    self.kingdom = kingdom
    self.phylum = phylum
    self.clas = clas
    self.order = order
    self.family = family
    self.genus = genus
    self.specie = specie

for line in sys.stdin:
  print(line)
# Ten cuidado con los espacios que tienes en python. En los otros archivos utilizaste 4 estacios
# y en este utilizaste 2.
