from src.models.SistemaTransporteScript import SistemaTransporteScript
from src.factory.Creador import CreadorTransporte

def main():
    try:
        sistema_transporte = SistemaTransporteScript()
        sistema_transporte.conseguir_input_vehiculo()
        sistema_transporte.conseguir_input_origen_destino()

        creador = CreadorTransporte.get_creador(sistema_transporte.vehiculo)
        transporte = creador.get_transporte()
        
        print(transporte.transportar(sistema_transporte.origen, sistema_transporte.destino))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    
    
#Ejemplo para correrlo: python main_script.py --vehiculo dron --origen Arg --destino MX