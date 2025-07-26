'''
Menú para paletería
'''
import paleteria


op=True
while op:
    print("\n\t\t\t.:::🍦 Sistema de Gestión de inventario de la paletería La Auténtica Mich Dgo 🍦:::.\n\n\t\t\t\t\t\t1.-➕ Agregar producto\n\t\t\t\t\t\t2.-🔄 Modificar producto\n\t\t\t\t\t\t3.-\U0001F4DB Eliminar Producto\n\t\t\t\t\t\t4.-\U0001F6AA Mostrar producto\n\t\t\t\t\t\t5.-🧹 Limpiar inventario\n\t\t\t\t\t\t6.-🔚 SALIR")
    opcion=input("\n\t\t\t .:::👉 Elige una opción : ").upper().strip()

    match opcion: 
        case "1":
            paleteria.agregarProducto()
            paleteria.esperarTecla()

        case "2":
            paleteria.modificarProducto()
            paleteria.esperarTecla()

        case "3":
            paleteria.eliminarProducto()
            paleteria.esperarTecla()

        case "4":
            paleteria.mostrarProducto()
            paleteria.esperarTecla() 

        case "5":
            paleteria.limpiarProducto()
            paleteria.esperarTecla()


        case "6":
            op=False
            paleteria.borrarPantalla()
            print("\n\t\t\t.:::🔚 Saliste del inventario de la paletería La Auténtica Mich Dgo:::.")

        case _:
            opcion=True
            paleteria.esperarTecla()
            print("\n\t\t\t.:::🙅‍♀️ Opción no válida, vuelve a intentar:::.")                      


    