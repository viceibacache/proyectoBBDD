import bcrypt

# Contraseña que queremos hashear
password = b"mi_super_contrasenha_secreta"

# Generar el hash de la contraseña
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print("Contraseña hasheada:", hashed)

# Verificar la contraseña contra el hash
if bcrypt.checkpw(password, hashed):
    print("¡El acceso es permitido!")
else:
    print("Acceso denegado.")
