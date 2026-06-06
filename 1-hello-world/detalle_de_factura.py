
def main():
    nombreFactura = "Productos de oficina"
    totalBruto = 134.78
    impuesto = (totalBruto * 0.19)
    montoTotal = totalBruto + impuesto

    print(f"La factura {nombreFactura} tiene un total bruto de {totalBruto}, con un"
          f"\nimpuesto de {impuesto} y el monto despues de impuestos es de {montoTotal}")

if __name__ == "__main__":
    main()