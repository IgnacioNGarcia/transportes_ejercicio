from src.factory.Creador import CreadorTransporte

def main():
    
    try:
        metodo = input("Ingrese el tipo de transporte (auto/dron):")
        
        creador = CreadorTransporte.get_creador(metodo)
        transporte = creador.get_transporte()
        
        origen = input("Ingrese el origen: ")
        destino = input("Ingrese el destino: ")
        
        print(transporte.transportar(origen, destino))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    
    