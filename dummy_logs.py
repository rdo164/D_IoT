import json
from datetime import datetime
import random

# Función para generar registros dummy
def generate_dummy_log():
    timestamp = datetime.utcnow().isoformat()
    log_level = random.choice(['INFO', 'ERROR', 'DEBUG'])
    message = f"Sample log message - {random.randint(1, 100)}"
    
    log_entry = {
        "@timestamp": timestamp,
        "log.level": log_level,
        "message": message
    }
    
    return log_entry

# Número de registros dummy a generar
num_logs = 10

# Ruta del archivo JSON de salida
output_file_path = "./logs/dummy_logs.json"
# Crear y guardar los registros en un archivo JSON, cada uno en una línea nueva
with open(output_file_path, 'w') as output_file:
    for _ in range(num_logs):
        log_entry = generate_dummy_log()
        json.dump(log_entry, output_file)
        output_file.write('\n')

print(f"Archivo JSON con {num_logs} registros dummy creado en {output_file_path}\n")
