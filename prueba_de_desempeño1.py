inventory = [
    {
        'producto': 'Panela', 
        'precio': 5000.00, 
        'cantidad': 1,
    },
    {
        'producto': 'Carne', 
        'precio': 16000.00, 
        'cantidad': 5,
    },
    {
        'producto': 'Pollo', 
        'precio': 14000.00, 
        'cantidad': 1,
    },
    {
        'producto': 'Salmon', 
        'precio': 20000.00, 
        'cantidad': 5,
    },
    {
        'producto': 'Arroz', 
        'precio': 8000.00, 
        'cantidad': 1,
    },

]


def watch_menu():
    while True:
        print('-----------------------------------------')
        print('            MENU PRINCIPAL \n')
        print('1. Añadir productos al inventario')
        print('2. Consultar inventario')
        print('3. Buscar productos en el inventario')
        print('4. Actualizar precios de productos')
        print('5. Eliminar productos del inventario')
        print('6. Calcular el valor total del inventario')
        print('7. Salir')
        print('-----------------------------------------')
        
        option = input('\nOpcion:')
        if option == '1':
            add_producto()
        if option == '2':
            whatch_products()
        if option == '3':
            search_products()
        if option == '4':
            update_products()
        if option == '5':
            delete_products()
        if option == '6':
            calculate_total_value()
        if option == '7':
            break
        
def get_product():
    print('-----------------------------------------')
    print('\n            NUEVO PRODUCTO')
    new_product = input('Nuevo producto:  ')
    
    products = []
    for product in inventory:
        products.append(product["producto"])
    
    if new_product in products:
        print ('\nEl producto ya esta registrado \n')
        return None
        
    cost = ask_number_float_positive('Precio: $')
    quantity = ask_number_int_positive('Ingrese la cantidad de productos: ')

    product = {
        'producto': new_product, 
        'precio': cost, 
        'cantidad': quantity, 
    }
    inventory.append(product)
    print('\nProducto agregado \n')
    
def add_producto():
    product = get_product()
    if product != None:
        inventory.update(product)
     
def whatch_products():
    print('-----------------------------------------')
    print('            INVENTARIO \n')
    print_row('PRODUCTO', 'PRECIO', 'CANTIDAD')
    for product in inventory:
        print_row(
            product['producto'],
            product['precio'],
            product['cantidad'],)
        
def search_products():
    print('            PRODUCTO ESPECIFICO \n')
    if len(inventory) == 0:
        print('El inventario esta vacio')
        
    name_product = input('Producto: ')
    
    located = False
    print_row('Producto', 'Precio', 'cantidad')
    for product in inventory:
        if name_product in product['producto']:
            print_row(
                product['producto'],
                product['precio'],
                product['cantidad'])
            
            located = True
    
    if not located:
        print('\nEl producto no esta en el inventario')
    
def update_products():
    print('            ACTUALIZAR PRODUCTO\n')
    name_update_product = input("Producto a actualizar: ")
    for i, product in enumerate(inventory):
        if name_update_product == product['producto']:
            cost = ask_number_float_positive('Precio: $')
            quantity = ask_number_int_positive("Cantidad: ")
            
            inventory[i]['producto'] = name_update_product
            inventory[i]['precio'] = cost
            inventory[i]['cantidad'] = quantity
            print('\n Producto actualizado')
            return
    print ('\nEl producto no esta en la lista')
    
def delete_products():
    print('-----------------------------------------')
    print('            ELIMINAR PRODUCTO\n')
    
    name_product = input('Producto a eliminar: ')
    
    for product in (inventory):
        if name_product == product['producto']:
            inventory.remove(product)
            print('\nProducto eliminado')
            return
        
    print("\n El Producto no esta en el inventario")

def calculate_total_value():
    counter = 0
    
    for product in (inventory):
        cost = product['precio']
        quantity = product['cantidad']
        multiplication = cost * quantity
        counter = counter + multiplication
    
    print('-----------------------------------------')    
    print(f"\nVALOR TOTAL DEL INVENTARIO \n${counter:,.2f}")
        
def ask_number_float_positive(prompt):
    while(True):
        try:
            number = float(input(prompt))
            if number > 0:
                return number
            else:
                print("\n||El numero no es positivo|| \n")
        except ValueError:
            print("\n||El numero es invalido|| \n")

def ask_number_int_positive(prompt):
    while(True):
        try:
            number = int(input(prompt))
            if number >= 0:
                return number
            else:
                print("\n||El numero no es positivo|| \n")
        except ValueError:
            print("\n||Ingresa un dato valido|| \n")

def print_row(a, b, c):
    print('{:<12}  {:<12}  {:<12}'.format(a, b, c) )
                    
watch_menu()
    


