import flet as ft
#titulo de la pagina principal
title =ft.Text(
    text_align=ft.TextAlign.CENTER,
    value=f"Fracciones",
    size=60,
    color = "black",
)

#funcion para crear los contenedores de los botones
def createContainer(symbol,route, color1, color2, page):
    outer_container = ft.Container(
        padding = 0,
        alignment = ft.alignment.bottom_center,
        bgcolor = color1,
        width=100,
        height=100,
        border_radius=10,
    )

    inner_container = ft.Container(
        padding=10,
        alignment=ft.alignment.top_center,
        bgcolor= color2,
        width=100,
        height=88,
        border_radius=10,
        content=ft.Text(value=symbol, color="white", size=50, text_align=ft.TextAlign.CENTER),
        ink=True,
        on_click=lambda _: page.go("/"+route),
    )

    outer_container.content = inner_container
    return outer_container

def main(page: ft.Page):
    
    page.title = "fracciones"
    containerSuma = createContainer("+","suma", "#33915c", "#4bb36c", page)
    containerResta = createContainer("-", "resta", "#f8bc25", "#ffd633", page)
    containerDivision = createContainer("x", "multiplicacion", "#5c8ad6", "#5cb2e8", page)
    containerMultiplicacion = createContainer("÷", "division", "#c20829", "#eb2b47", page)
    containerInformacion = createContainer("?", "ayuda", "#a245f7", "#a552f2", page)

    def route_change(route):
    
       
        page.views.clear()


        #elementos de la pagina principal
        image = ft.Image(
            src="../assets/ajoloteFeliz.png",
            width=500,
            height=500,
        )
        page.views.append(
            ft.View(
                "/",
                controls=[
                    #titulo de la pagina
                    ft.Row(controls=[title],
                           alignment=ft.MainAxisAlignment.CENTER,
                           ),
                    #espacio de botones
                    ft.Column(controls=[
                        #primeros 2 botones
                        ft.Row(controls=[
                            containerSuma,
                            containerResta,   
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        #segundos 2 botones
                        ft.Row(controls=[
                            containerDivision,
                            containerMultiplicacion,     
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                        ),
                        #boton de informacion
                        ft.Row(controls=[
                            containerInformacion,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        #imagen de ajolote
                        ft.Row(controls=[
                            image,
                        ],
                        alignment=ft.MainAxisAlignment.END,
                        spacing=0,
                        ),
                        

                    ],),
                ],
                #espacio entre los elementos
                padding=50,
                #color de fondo
                bgcolor="#a6c3dc",
                
            )
        )

        #elementos de la pagina suma
        #funcion crear elemento exterior ejemplo: color #4bb36c se puede usar en los demas niveles
        def createExterior(color):
            return ft.Container(
            padding = 0,
            alignment = ft.alignment.bottom_center,
            bgcolor = color,
            width=100,
            height=100,
            border_radius=10,
            )
        #funcion crear elemento interior ejemplo: simbolo "+" se puede usar en los demas niveles el redirect es opcional por defecto envia a la pagina principal
        def createInterior(color,simbolo,redirect = ""):
            return ft.Container(
            padding = 0,
            alignment = ft.alignment.center,
            bgcolor = color,
            width=100,
            height=88,
            border_radius=10,
            content=ft.Text(value=simbolo, color="white", size=50,text_align=ft.TextAlign.START,),
            ink=True,
            on_click=lambda _: page.go("/"+redirect),
            top = 12,
            )
        #elemento de boton regresar
        exterior = createExterior("#33915c")
        #elemento interior boton regresar
        interior = createInterior("#4bb36c","+")
        #boton regresar completo
        botonRegresar = ft.Stack([
            exterior,interior
        ],
        alignment = ft.alignment.center,
        )

        #niveles
        #fondo blanco de los carteles (se usa para todos los carteles)
        cartelBack = ft.Container(
            width=100,
            height=100,
            bgcolor="white", 
            border_radius=10,
            border=ft.border.all(),
        ) 
        #base de los carteles (se usa para todos los carteles)
        base = ft.Container(
            width=20,
            height=20,
            bgcolor="brown",
            border = ft.border.all(),
        )
        #funcion para crear el contenedor de los carteles con texto(facilita crear el contenido de los carteles pasar nivel en numero)
        def createCartel(nivel,texto):
            cartel = ft.Container(
                width=90,
                height=90,
                bgcolor="#91d9ff",
                border_radius=10,
                border=ft.border.all(),
                left=5,
                top=5,
                content = ft.Column(
                    controls=[
                    ft.Text(value=nivel, color="white", size=30,text_align=ft.TextAlign.CENTER,width=90),
                    ft.Text(value=texto, color="black", size=30,text_align=ft.TextAlign.CENTER,width=90),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=0,
                )
            )
            return cartel
        
        #crear los carteles
        cartel1 = createCartel("1","Level")
        cartel2 = createCartel("2","Level")
        cartel3 = createCartel("3","Level")

        #contenedores de los niveles
        nivel1 = ft.Container(
            width=100,
            height=130,
            content=ft.Column(controls=[
            ft.Stack([cartelBack, cartel1]),
            ft.Row(controls=[
                base,
            ],
                width=100,
                alignment=ft.MainAxisAlignment.CENTER,
            )
            ],
            spacing=0,
            ),
            on_click=lambda _: page.go("/nivel1Suma"),
        )
        
        
        nivel2 = ft.Container(
            width=100,
            height=130,
            content=ft.Column(controls=[
                ft.Stack([cartelBack,cartel2]),
                ft.Row(controls=[
                    base,
                ],
                width=100,
                alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            spacing=0
            ),
            on_click=lambda _: page.go("/nivel2Suma"),
        )

        nivel3 = ft.Container(
            width=100,
            height=130,
            content=ft.Column(controls=[
                ft.Stack([cartelBack,cartel3]),
                ft.Row(controls=[
                    base,
                ],
                width=100,
                alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            spacing=0
            ),
            on_click=lambda _: page.go("/nivel3Suma"),
        )
        #agregar los elementos a la pagina  
        if page.route == "/suma":
            #cambiar imagen
            image.src = "../assets/ajoloteFeliz.png"
            page.views.append(
            ft.View(
                "/suma",
               controls= [
                   ft.Row(controls=[title],
                      alignment=ft.MainAxisAlignment.CENTER,
                   ),
                botonRegresar,
                ft.Row(controls=[
                    nivel1,
                    nivel2,
                    nivel3,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=50,
                ),
                ft.Row(controls=[
                    image,
                ],
                spacing=0,
                alignment=ft.MainAxisAlignment.CENTER,
                ),
                ],
                bgcolor="#5271ff",
                padding=50,
                
            )
            )
        
        if page.route == "/nivel1Suma":
            #cambiar imagen
            image.src = "../assets/ajoloteTriste.png"
            #redireccionar a la pagina siguiente
            interior.on_click = lambda _: page.go("/suma")
            page.views.clear()
            page.views.append(
            ft.View(
                "/nivel1Suma",
                controls=[
                ft.Row(
                    controls=[title],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                botonRegresar,
                ft.Row(
                    controls=[image],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[image],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=0,
                ),
                ],
                bgcolor="#5271ff",
                padding=50,
            )
            )

        #elementos de la pagina resta
        #boton regresar
        botonRegresarResta = ft.Stack([
            createExterior("#f8bc25"),createInterior("#ffd633","-")
        ],)
        if page.route == "/resta":
            #cambiar solo el contenido de los niveles para cambiar a donde redireccionar
            nivel1.on_click = lambda _: page.go("/suma")
            nivel2.on_click = lambda _: page.go("/suma")
            nivel3.on_click = lambda _: page.go("/suma")
            exterior.bgcolor = "#f8bc25"
            interior.bgcolor = "#ffd633"
            interior.content.value = "-"
            #cambiar la imagen
            image.src = "../assets/ajoloteFeliz.png"
            page.views.append(
                ft.View(
                    "/resta",
                    [
                        ft.Row(controls=[title],
                              alignment=ft.MainAxisAlignment.CENTER,
                           ),
                        botonRegresar,
                        ft.Row(controls=[
                            nivel1,
                            nivel2,
                            nivel3,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=50,
                        ),
                        ft.Row(controls=[
                            image,
                        ],
                        spacing=0,
                        alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    bgcolor="#5271ff",
                    padding=50,
                )
            )
        if page.route == "/nivel1Resta":
            #cambiar imagen
            image.src = "../assets/partes.png"
            page.views.clear()
            page.views.append(
            ft.View(
                "/nivel1Suma",
                controls=[
                ft.Row(
                    controls=[title],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                botonRegresar,
                ft.Row(
                    controls=[image],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=0,
                ),
                ],
                bgcolor="#5271ff",
                padding=50,
            )
            )


        #elementos de la pagina multiplicacion
        #boton regresar
        if page.route == "/multiplicacion":
            #cambiar solo el contenido de los niveles para cambiar a donde redireccionar
            nivel1.on_click = lambda _: page.go("/suma")
            nivel2.on_click = lambda _: page.go("/suma")
            nivel3.on_click = lambda _: page.go("/suma")
            exterior.bgcolor = "#5c8ad6"
            interior.bgcolor = "#5cb2e8"
            interior.content.value = "x"
            #cambiar la imagen
            image.src = "../assets/ajoloteFeliz.png"
            page.views.append(
                ft.View(
                    "/multiplicacion",
                    [
                        ft.Row(controls=[title],
                              alignment=ft.MainAxisAlignment.CENTER,
                           ),
                        botonRegresar,
                        ft.Row(controls=[
                            nivel1,
                            nivel2,
                            nivel3,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=50,
                        ),
                        ft.Row(controls=[
                            image,
                        ],
                        spacing=0,
                        alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    bgcolor="#5271ff",
                    padding=50,
                )
            )
        if page.route == "/nivel1Multiplicacion":
            #cambiar imagen
            image.src = "../assets/partes.png"
            page.views.clear()
            page.views.append(
            ft.View(
                "/nivel1Suma",
                controls=[
                ft.Row(
                    controls=[title],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                botonRegresar,
                ft.Row(
                    controls=[image],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=0,
                ),
                ],
                bgcolor="#5271ff",
                padding=50,
            )
            )

        #elementos de la pagina division
        
        if page.route == "/division":
            #modificar los niveles solo para la redireccion
            nivel1.on_click = lambda _: page.go("/suma")
            nivel2.on_click = lambda _: page.go("/suma")
            nivel3.on_click = lambda _: page.go("/suma")
            #modificar los elementos del boton regresar
            exterior.bgcolor = "#c20829"
            interior.bgcolor = "#eb2b47"
            interior.content.value = "÷"
            #cabiar la imagen 
            image.src = "../assets/ajoloteFeliz.png"
            page.views.append(
                ft.View(
                    "/division",
                    [
                        ft.Row(controls=[title],
                              alignment=ft.MainAxisAlignment.CENTER,
                           ),
                        botonRegresar,
                        ft.Row(controls=[
                            nivel1,
                            nivel2,
                            nivel3,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=50,
                        ),
                        ft.Row(controls=[
                            image,
                        ],
                        spacing=0,
                        alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    bgcolor="#5271ff",
                    padding=50,
                )
            )
        if page.route == "/nivel1Division":
            #cambiar imagen
            image.src = "../assets/partes.png"
            page.views.clear()
            page.views.append(
            ft.View(
                "/nivel1Suma",
                controls=[
                ft.Row(
                    controls=[title],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                botonRegresar,
                ft.Row(
                    controls=[image],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=0,
                ),
                ],
                bgcolor="#5271ff",
                padding=50,
            )
            )


        #elementos de la pagina ayuda
        
        if page.route == "/ayuda":
            page.views.append(
                ft.View(
                    "/ayuda",
                    controls=[
                       
                         
                    ],
                    bgcolor="#5271ff",
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
