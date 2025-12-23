# --- 1. Definimos las funciones Callback (Qué hacer con el resultado) ---
def mostrar_en_pantalla(valor):
    """Callback para definir el resultado"""
    print(f"El resultado final es {valor}")


def guardar_en_registro(valor):
    """Callback para registrar el resultado de una manera formal."""
    print(f"--- REGISTRO --- valor procesado: {valor}")


# --- 2. Definimos la Función Principal (El Proceso) ---
def realizar_operacion(a, b, callback_a_usar):
    """
        Función principal que suma 'a' y 'b', y luego pasa el resultado
        a la función callback que se le dé.
        """
    resultado = a + b

    # Llama el callback con el resultado
    callback_a_usar(resultado)

print("--- Ejecución 1 (Mostrar en pantalla) ---")
# Aquí, 'mostrar_en_pantalla' es el callback
realizar_operacion(10, 5, mostrar_en_pantalla)

print("\n--- Ejecución 2 (Guardar en registro) ---")
# Aquí, 'guardar_en_registro' es el callback
realizar_operacion(20, 8, guardar_en_registro)

