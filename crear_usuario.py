import hashlib
from database import run_query

usuario = "Franco.guillen"
password = "Illescas2147"
rol = "admin"

# Crear hash SHA-256
password_hash = hashlib.sha256(password.encode()).hexdigest()

run_query("""
    INSERT INTO usuarios (usuario, password_hash, rol)
    VALUES (?, ?, ?)
""", (usuario, password_hash, rol))

print("Usuario creado correctamente.")