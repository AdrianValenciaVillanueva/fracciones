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
    
    page.title = "Routes Example"
    containerSuma = createContainer("+","suma", "#33915c", "#4bb36c", page)
    containerResta = createContainer("-", "resta", "#f8bc25", "#ffd633", page)
    containerDivision = createContainer("x", "multiplicacion", "#5c8ad6", "#5cb2e8", page)
    containerMultiplicacion = createContainer("÷", "division", "#c20829", "#eb2b47", page)
    containerInformacion = createContainer("?", "ayuda", "#a245f7", "#a552f2", page)

    def route_change(route):
    
       
        page.views.clear()


        #elementos de la pagina principal
        image = ft.Image(
            src="assets/ajoloteFeliz.png",
            width=500,
            height=500,
        )
        page.views.append(
            ft.View(
                "/",
                controls=[
                    ft.Row(controls=[title],
                           alignment=ft.MainAxisAlignment.CENTER,
                           ),
                    ft.Column(controls=[
                        ft.Row(controls=[
                            containerSuma,
                            containerResta,   
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(controls=[
                            containerDivision,
                            containerMultiplicacion,     
                        ],
                        alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[
                            containerInformacion,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(controls=[
                            image,
                        ],
                        alignment=ft.MainAxisAlignment.END,
                        ),
                        

                    ],),
                ],
                padding=50,
                bgcolor="#5271ff",
                
            )
        )

        #elementos de la pagina suma
        exterior = ft.Container(
        padding = 0,
        alignment = ft.alignment.bottom_center,
        bgcolor = "#33915c",
        width=100,
        height=100,
        border_radius=10,
        )
        interior = ft.Container(
        padding = 0,
        alignment = ft.alignment.center,
        bgcolor = "#4bb36c",
        width=100,
        height=88,
        border_radius=10,
        content=ft.Text(value="+", color="white", size=50,text_align=ft.TextAlign.START,),
        ink=True,
        on_click=lambda _: page.go("/"),
        top = 12,
        )
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
           
        ) 
        #base de los carteles (se usa para todos los carteles)
        base = ft.Container(
            width=20,
            height=20,
            bgcolor="brown",
        )
        #funcion para crear el contenedor de los carteles con texto(facilita crear el contenido de los carteles pasar nivel en numero)
        def createCartel(nivel,texto):
            cartel = ft.Container(
                width=90,
                height=90,
                bgcolor="#91d9ff",
                border_radius=10,
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
                ft.Stack([cartelBack,cartel1]),
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
                        )
                    ],
                    bgcolor="#5271ff",
                    padding=50,
                    
                )
            )

        #elementos de la pagina resta
        if page.route == "/resta":
            page.views.append(
                ft.View(
                    "/resta",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )


        #elementos de la pagina multiplicacion
        if page.route == "/multiplicacion":
            page.views.append(
                ft.View(
                    "/multiplicacion",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )


        #elementos de la pagina division
        if page.route == "/division":
            page.views.append(
                ft.View(
                    "/division",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
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
