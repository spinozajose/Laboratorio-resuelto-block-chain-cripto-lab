# Blockchain Cripto Lab - BCY0010 (Resuelto)

Este repositorio contiene la resolución de la **Actividad 1.1: Encriptador simple**, donde se implementaron herramientas de criptografía simétrica y funciones hash utilizando Python.

| Campo | Detalle |
|-------|---------|
| **Asignatura** | BCY - Fundamentos de Blockchain 003D OLS |
| **Experiencia** | EA1 - Herramientas criptográficas y sistemas distribuidos |
| **Alumno** | (Jose ignacio Espinoza Espinoza) LJ (spinozajose) |
| **Escuela** | Informática y Telecomunicaciones - Duoc UC |

---

##  Tecnologías y Herramientas
* **Lenguaje:** Python 3.8+
* **Librería Criptográfica:** [PyCryptodome](https://pycryptodome.readthedocs.io/)
* **Entorno:** Linux (Arch Linux / CachyOS) en ThinkPad T480s
* **Editor:** Visual Studio Code

---

##  Descripción del Proyecto
Se ha completado el código base (boilerplate) para construir un sistema de cifrado robusto. Los objetivos alcanzados incluyen:

1.  **Cifrado Simétrico AES-256:** Generación de llaves seguras y manejo de archivos en modo CBC.
2.  **Integridad de Datos:** Implementación de SHA-256 para verificar que los archivos no hayan sido alterados.
3.  **Análisis Comparativo:** Evaluación de rendimiento y seguridad entre AES-256 y el estándar legado DES.

---

##  Estructura del Repositorio
* `encriptador.py`: Implementación de las funciones `generar_llave()`, `cifrar_archivo()` y `descifrar()`. **(Completado)**
* `verificador_hash.py`: Módulo para calcular y comparar hashes SHA-256. **(Completado)**
* `comparador_algoritmos.py`: Script para comparar tiempos de ejecución y seguridad entre algoritmos.
* `examples/`: Archivos de prueba y referencias de implementación.
* `tests/`: Scripts de validación automática para asegurar el correcto funcionamiento del código.

---

##  Uso e Instalación

### 1. Preparación del Entorno
```bash
# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Ejecucion del encriptador
# Cifrar un archivo
```bash
python encriptador.py cifrar examples/mensaje_prueba.txt
```
<img width="700" height="206" alt="image" src="https://github.com/user-attachments/assets/014dbd21-564c-48fc-8fea-a5591c4b3abd" />


# Descifrar el archivo resultante
```bash
python encriptador.py descifrar examples/mensaje_prueba.txt.enc
```
<img width="700" height="206" alt="image" src="https://github.com/user-attachments/assets/eb453ba9-182c-4342-9d6d-95aa3e91907a" />


### 3. Verificación de Integridad

```bash
# Comparar el archivo original con el descifrado
python verificador_hash.py examples/mensaje_prueba.txt examples/mensaje_prueba.txt.dec.txt
```
<img width="498" height="297" alt="image" src="https://github.com/user-attachments/assets/86ad28e6-c359-4e73-ac7c-82d5e6b3e9f6" />

### 4. Verificacion de Hash
```bash
# Verifica la integridad de el hash generado para cifrar los archivos
python verificador_hash.py examples/mensaje_prueba.txt examples/mensaje_prueba.txt.dec.txt
```
<img width="498" height="293" alt="image" src="https://github.com/user-attachments/assets/acaea225-ce47-4acb-b051-eb9ff6f3f0ba" />

### 5. Ejecucion de los tests, o pruebas de funcionamiento
```bash
python tests/test_encriptador.py && python tests/test_hash.py
```
<img width="624" height="794" alt="image" src="https://github.com/user-attachments/assets/cd921edc-697d-41ad-9d78-8038de2b8b4a" />

### 6. Comparaciones y observacion

<img width="624" height="471" alt="image" src="https://github.com/user-attachments/assets/0b47c32a-8573-4a20-9f66-f88dc62ef1fa" />


