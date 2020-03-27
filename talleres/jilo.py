si-> s no-> n """
MENSAJE_ERROR = " Su acción ha sido errada "
MENSAJE_CONTINUAR = " Si desea puede continuar \n "
 MENSAJE_PRODUCTO_ELIMINADO = " Se ha eliminado el producto"
 MENSAJE_ELIMINADO_ERROR = " El producto a eliminar no fue encontrado"
 SALIR = "Usted ha salido de la compra"
 GRACIAS = "GRACIAS POR SU COMPRA"

 #---------------Entradas----------------
 _numeroIngresado = ""
 _edadUsuario = ""
 #---------------Variables---------------
 respuesta = ""
 list_menu =[]
 posicionProducto = 1
 NE = "No existe"
 #----------------Código-----------------
 print (MENSAJE_BIENVENIDA)
 while ( _numeroIngresado != 5):
 @@ -57,12 +63,19 @@ def mostrar_lista(Lista):
                 print(posicionProducto,producto)
                 posicionProducto +=1
         mostrar_lista (list_menu)
     else:
     elif (_numeroIngresado == 4):
         _producto = input(MENSAJE_ELIMINAR)
         for _producto in range(len(list_menu)):
             if(_producto == list_menu):
         posicionProductoEliminar = NE
         for i in range(len(list_menu)):
             if(_producto == list_menu[i]):
                 input(MENSAJE_CONFIRMACION_ELIMINAR)
                 list_menu.pop(_producto) 
             print(list_menu)                   
                 posicionProductoEliminar = i       
         if (posicionProductoEliminar != NE) :
             eliminado = list_menu.pop(posicionProductoEliminar)
             print(MENSAJE_PRODUCTO_ELIMINADO, eliminado)
         else:
             print(MENSAJE_ELIMINADO_ERROR)
         print(list_menu)                  
         print(MENSAJE_CONTINUAR)
 print("GRACIAS POR SU COMPRA") 
     else: print(SALIR)
 print(GRACIAS