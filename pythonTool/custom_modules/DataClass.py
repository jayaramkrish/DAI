class DataClass:
  def __init__(self, data):
    self.Tool = data['apiSpec']['tool']
    self.Type = data['apiSpec']['type']
    self.tokenMode = data['apiSpec']['tokenMode']
    self.sslMode = data['apiSpec']['sslMode']