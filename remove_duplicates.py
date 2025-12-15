#!/usr/bin/env python3
"""
Script para eliminar duplicados del archivo custom_kanji.txt de forma eficiente.
Complejidad temporal: O(n) donde n es el número de caracteres.
Complejidad espacial: O(k) donde k es el número de caracteres únicos.
"""

def remove_duplicates_from_kanji_file(input_file='./custom_kanji.txt', output_file=None):
    """
    Elimina duplicados del archivo de kanji manteniendo el orden de primera aparición.
    
    Args:
        input_file (str): Ruta del archivo de entrada
        output_file (str): Ruta del archivo de salida (None para sobrescribir)
    
    Returns:
        tuple: (total_original, total_unique, duplicates_removed)
    """
    try:
        # Leer el archivo
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        
        # Separar por líneas y filtrar líneas vacías
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        # Usar set para tracking O(1) lookup + list para mantener orden
        seen = set()
        unique_kanjis = []
        
        total_original = len(lines)
        
        # Procesar cada línea (kanji)
        for kanji in lines:
            if kanji not in seen:
                seen.add(kanji)
                unique_kanjis.append(kanji)
        
        total_unique = len(unique_kanjis)
        duplicates_removed = total_original - total_unique
        
        # Escribir resultado
        output_path = output_file or input_file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(unique_kanjis) + '\n')
        
        return total_original, total_unique, duplicates_removed
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{input_file}'")
        return None, None, None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None, None, None


def analyze_duplicates(input_file='custom_kanji.txt'):
    """
    Analiza y muestra información sobre duplicados sin modificar el archivo.
    
    Args:
        input_file (str): Ruta del archivo a analizar
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        # Contar frecuencias
        frequency = {}
        for kanji in lines:
            frequency[kanji] = frequency.get(kanji, 0) + 1
        
        # Encontrar duplicados
        duplicates = {kanji: count for kanji, count in frequency.items() if count > 1}
        
        print(f"📊 Análisis del archivo '{input_file}':")
        print(f"   Total de líneas: {len(lines)}")
        print(f"   Kanjis únicos: {len(frequency)}")
        print(f"   Duplicados encontrados: {len(duplicates)}")
        
        if duplicates:
            print(f"\n🔍 Kanjis duplicados:")
            for kanji, count in sorted(duplicates.items(), key=lambda x: x[1], reverse=True):
                print(f"   '{kanji}' aparece {count} veces")
        else:
            print(f"\n✅ No se encontraron duplicados")
            
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{input_file}'")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    import sys
    
    print("🔧 Script de eliminación de duplicados para Kanji")
    print("=" * 50)
    
    # Primero analizar
    print("1️⃣ Analizando archivo actual...")
    analyze_duplicates()
    
    # Preguntar si proceder
    print(f"\n2️⃣ ¿Deseas eliminar los duplicados? (y/N): ", end="")
    
    # Si se ejecuta como script, pedir confirmación
    if len(sys.argv) > 1 and sys.argv[1] == "--auto":
        response = "y"
        print("y (modo automático)")
    else:
        response = input().lower().strip()
    
    if response in ['y', 'yes', 'sí', 'si']:
        print(f"\n3️⃣ Eliminando duplicados...")
        original, unique, removed = remove_duplicates_from_kanji_file()
        
        if original is not None:
            print(f"✅ Proceso completado:")
            print(f"   Kanjis originales: {original}")
            print(f"   Kanjis únicos: {unique}")
            print(f"   Duplicados eliminados: {removed}")
            
            if removed > 0:
                print(f"   Archivo 'custom_kanji.txt' actualizado")
            else:
                print(f"   No había duplicados que eliminar")
        else:
            print(f"❌ Error al procesar el archivo")
    else:
        print(f"\n⏹️ Operación cancelada")