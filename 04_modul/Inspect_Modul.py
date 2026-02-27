# Mit inspect-Modul (für erweiterte Funktionalität)
import inspect

def get_frame_variables():
    """
    Nutzt das inspect-Modul für detaillierte Variable-Inspektion
    """
    print("\n=== Mit inspect-Modul ===")

    # Aktueller Frame (diese Funktion)
    frame = inspect.currentframe()
    # Vorheriger Frame (aufrufende Funktion/Hauptprogramm)
    caller_frame = frame.f_back

    variable_info = []
    for var_name, var_value in caller_frame.f_locals.items():
        if not var_name.startswith('_'):
            variable_info.append({
                'name': var_name,
                'type': type(var_value).__name__,
                'value': var_value
            })

    return variable_info

# Hilfsfunktion zum schönen Ausgeben der Ergebnisse
def print_variable_info(variable_list, title="Variablen-Information"):
    """
    Gibt die Variableninformationen formatiert aus
    """
    print(f"\n{title}")
    print("-" * 50)
    for var_info in variable_list:
        print(f"Name: {var_info['name']:<15} | Typ: {var_info['type']:<10} | Wert: {var_info['value']}")
        
if __name__ == "__main__":
    inspect_vars = get_frame_variables()
    print_variable_info(inspect_vars, "Variablen via inspect")