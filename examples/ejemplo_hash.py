"""
ejemplo_hash.py — Ejemplo RESUELTO de verificación SHA-256
===========================================================
Referencia para completar verificador_hash.py.
"""

import hashlib


def demo_hash():
    """Demostración del uso de funciones hash SHA-256."""

    print("=" * 60)
    print("  DEMO: Funciones Hash SHA-256")
    print("=" * 60)

    # ── 1. Hash de un string ──
    mensaje1 = "Hola Blockchain"
    hash1 = hashlib.sha256(mensaje1.encode("utf-8")).hexdigest()
    print(f"\n1. Mensaje:  '{mensaje1}'")
    print(f"   SHA-256:  {hash1}")

    # ── 2. Cambiar un solo carácter ──
    mensaje2 = "hola Blockchain"  # 'H' → 'h'
    hash2 = hashlib.sha256(mensaje2.encode("utf-8")).hexdigest()
    print(f"\n2. Mensaje:  '{mensaje2}' (solo cambió H→h)")
    print(f"   SHA-256:  {hash2}")
    print(f"   ¿Iguales? {'Sí' if hash1 == hash2 else 'No — completamente diferente!'}")

    # ── 3. Hash de un archivo ──
    print(f"\n3. Hash de archivo (lectura por bloques):")

    def calcular_hash_archivo(ruta):
        sha256 = hashlib.sha256()
        with open(ruta, "rb") as f:
            for bloque in iter(lambda: f.read(4096), b""):
                sha256.update(bloque)
        return sha256.hexdigest()

    # Crear archivos de prueba
    with open("/tmp/test_hash_a.txt", "w") as f:
        f.write("Contenido idéntico")
    with open("/tmp/test_hash_b.txt", "w") as f:
        f.write("Contenido idéntico")
    with open("/tmp/test_hash_c.txt", "w") as f:
        f.write("Contenido diferente")

    hash_a = calcular_hash_archivo("/tmp/test_hash_a.txt")
    hash_b = calcular_hash_archivo("/tmp/test_hash_b.txt")
    hash_c = calcular_hash_archivo("/tmp/test_hash_c.txt")

    print(f"   Archivo A: {hash_a}")
    print(f"   Archivo B: {hash_b} (mismo contenido que A)")
    print(f"   Archivo C: {hash_c} (contenido diferente)")
    print(f"   A == B? {'✅ Sí' if hash_a == hash_b else '❌ No'}")
    print(f"   A == C? {'✅ Sí' if hash_a == hash_c else '❌ No'}")

    # ── 4. Propiedades de las funciones hash ──
    print(f"\n{'=' * 60}")
    print("  Propiedades de SHA-256:")
    print("=" * 60)
    print("  • Determinista:    El mismo input siempre produce el mismo hash.")
    print("  • Efecto avalancha:Un cambio mínimo cambia todo el hash.")
    print("  • Unidireccional:  No se puede obtener el mensaje desde el hash.")
    print("  • Resistente a colisiones: Dos inputs distintos → hashes distintos.")
    print("  • Tamaño fijo:    Siempre 256 bits (64 caracteres hex).")
    print()


if __name__ == "__main__":
    demo_hash()
