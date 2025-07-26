'''
Se va a utilizar un diccionario para que guarde el atributo y su valor inventario={}
'''

inventario={}

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t\t\t\t\t.:::👉 Oprima una tecla para continuar:::.")


def agregarProducto():
     borrarPantalla()
     print("\n\t\t\t\t\t\t.:::➕ Agregar productos al inventario ➕ ")
     inventario["nombre"]=input("\n\t\t\t\t\t 🖊️  Ingresa el nombre del producto: ").upper().strip()
     inventario["cantidad"]=input("\n\t\t\t\t\t 🖊️  Ingresa la cantidad del producto: ").upper().strip()
     inventario["codigo"]=input("\n\t\t\t\t\t 🖊️  Ingresa el código del producto: ").upper().strip()
     inventario["precio_unitario"]=input("\n\t\t\t\t\t 🖊️  Ingresa el precio unitario del producto: ").upper().strip()
     print("\n\t\t\t\t\t\t .:::✅ El producto se agregó con éxito, tarea finalizada:::")


def modificarProducto():
    borrarPantalla()
    print("\n\t\t\t\t\t\t.:::🔄 Modificar productos del inventario 🔄")
    if len(inventario)>0:
        
        for i in inventario:
            print(f"\n\t\t\t\t\t{i} : {inventario[i]}") 
                   
            yes=input("\n\t\t\t\t\t.:::🧠 ¿Deseas modificar este apartado? (Si/No): ").lower().strip()
            if yes=="si":
                inventario[i]=input("\n\t\t\t\t\t🖊️  Ingresa el nuevo valor para este apartado: ").upper().strip()
                print("\n\t\t\t\t\t\t.:::✅ El producto se modificó con éxito:::.")
                esperarTecla()
    else:
        print("\n\t\t\t\t\t\t.:::❌ No hay ningún producto en el inventario")

def mostrarProducto():
    borrarPantalla()
    print("\n\t\t\t\t\t\t.:::✨ Mostrar productos del inventario ✨") 
    if len(inventario)>0:
        for i in inventario:
            print(f"\n\t\t\t\t\t\t📌 {i} : {inventario[i]}")
    else:
        print("\n\t\t\t\t\t\t.:::❌ No hay ningún producto en el inventario")         

        
def limpiarProducto(): 
    borrarPantalla()
    print("\n\t\t\t\t\t\t.:::🧹 Limpiar todos los productos del inventario 🧹")
    if len(inventario)>0:
        yes=input("\n\t\t\t\t\t.:::🤔 ¿Realmente deseas vaciar todo el inventario? (Si/No): ").lower().strip()
        if yes=="si":
            inventario.clear()
            print("\n\t\t\t\t\t\t.:::✅ El inventario se vació con éxito:::")
            
    else:
        print("\n\t\t\t\t\t\t.:::❌ No hay ningún producto en el inventario")        


def eliminarProducto():
    borrarPantalla()
    print("\n\t\t\t\t\t\t.:::⛔ Borrar producto del inventario ⛔\n")
    if len(inventario)>0:
        producto_a_borrar = input("\n\t\t\t\t\t.:::✏️  Escribe el nombre del producto que deseas borrar: ").upper().strip()
            
        if producto_a_borrar==inventario["nombre"]:
           
            inventario["nombre"]=""
            inventario["cantidad"]=""
            inventario["codigo"]=""
            inventario["precio_unitario"]=""

            print(f"\n\t\t\t\t\t\t.:::✅ El producto fue borrado con éxito:::.")

        else: 
            print("\n\t\t\t\t\t\t.:::🙅‍♀️ Ese producto no existe:::.")      
    else:
        print("\n\t\t\t\t\t\t.:::❌ No hay ningún producto en el inventario")   

