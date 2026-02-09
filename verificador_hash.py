"""
verificador_hash.py — Verificación de integridad con SHA-256
=============================================================
BCY0010 · Fundamentos de Blockchain
EA1 · Act 1.1 · Encriptador simple y compraventa
IL1.2

Descripción:
    Calcula y compara hashes SHA-256 de dos archivos para verificar
    que su contenido es idéntico. Este es el mismo principio que usa
    blockchain para garantizar la integridad de cada bloque.

Uso:
    python verificador_hash.py <archivo_original> <archivo_descifrado>

Ejemplo:
    python verificador_hash.py mensaje.txt mensaje.txt.dec.txt

Autor: <TU NOMBRE>
Fecha: <FECHA>
"""

import hashlib
import sys
import os


def calcular_hash(ruta_archivo):
    """
    Calcula el hash SHA-256 de un archivo.

    SHA-256 produce un "fingerprint" (huella digital) de 64 caracteres
    hexadecimales (256 bits). Cualquier cambio en el archivo, por mínimo
    que sea, produce un hash completamente diferente.

    Args:
        ruta_archivo (str): Ruta al archivo.

    Returns:
        str: Hash SHA-256 en formato hexadecimal (64 caracteres).

    Proceso:
        1. Crear un objeto hashlib.sha256().
        2. Leer el archivo en bloques de 4096 bytes.
        3. Actualizar el hash con cada bloque.
        4. Retornar el hexdigest.
    """
    # TODO: Crear el objeto SHA-256
    # Pista: sha256 = hashlib.sha256()
    sha256 = None  # Reemplaza esto

    # TODO: Abrir el archivo en modo binario ("rb") y leer en bloques.
    #       Para cada bloque, actualizar el hash con sha256.update(bloque).
    #
    # Pista:
    #   with open(ruta_archivo, "rb") as f:
    #       for bloque in iter(lambda: f.read(4096), b""):
    #           sha256.update(bloque)
    pass  # Reemplaza esto

    # TODO: Retornar sha256.hexdigest()
    return None  # Reemplaza esto


def comparar_hashes(hash1, hash2):
    """
    Compara dos hashes y determina si los archivos son idénticos.

    Args:
        hash1 (str): Hash del primer archivo.
        hash2 (str): Hash del segundo archivo.

    Returns:
        bool: True si los hashes son iguales, False en caso contrario.
    """
    return hash1 == hash2


def mostrar_resultado(archivo1, archivo2, hash1, hash2, iguales):
    """Muestra el resultado de la verificación de forma visual."""
    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║        Verificación de Integridad — SHA-256             ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print(f"║  Archivo 1: {archivo1[:44]:<44} ║")
    print(f"║  Hash:      {hash1[:44]:<44} ║")
    print(f"║             {hash1[44:]:<44} ║")
    print("║                                                          ║")
    print(f"║  Archivo 2: {archivo2[:44]:<44} ║")
    print(f"║  Hash:      {hash2[:44]:<44} ║")
    print(f"║             {hash2[44:]:<44} ║")
    print("║                                                          ║")

    if iguales:
        print("║  Resultado: ✅ INTEGRIDAD VERIFICADA                    ║")
        print("║  Los archivos son idénticos.                             ║")
    else:
        print("║  Resultado: ❌ INTEGRIDAD FALLIDA                       ║")
        print("║  Los archivos son DIFERENTES.                            ║")

    print("╚══════════════════════════════════════════════════════════╝\n")


def main():
    if len(sys.argv) < 3:
        print("╔══════════════════════════════════════════════════════════╗")
        print("║  Verificador de Integridad SHA-256 · BCY0010            ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║  Uso:                                                   ║")
        print("║    python verificador_hash.py <original> <descifrado>   ║")
        print("║                                                         ║")
        print("║  Ejemplo:                                               ║")
        print("║    python verificador_hash.py msg.txt msg.txt.dec.txt   ║")
        print("╚══════════════════════════════════════════════════════════╝")
        sys.exit(1)

    archivo1 = sys.argv[1]
    archivo2 = sys.argv[2]

    # Verificar que los archivos existen
    for archivo in [archivo1, archivo2]:
        if not os.path.exists(archivo):
            print(f"❌ Error: No se encontró el archivo '{archivo}'")
            sys.exit(1)

    # Calcular hashes
    hash1 = calcular_hash(archivo1)
    hash2 = calcular_hash(archivo2)

    if hash1 is None or hash2 is None:
        print("❌ Error: calcular_hash() retornó None.")
        print("   Completa los TODO en la función calcular_hash().")
        sys.exit(1)

    # Comparar y mostrar
    iguales = comparar_hashes(hash1, hash2)
    mostrar_resultado(archivo1, archivo2, hash1, hash2, iguales)


if __name__ == "__main__":
    main()
