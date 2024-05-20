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
        page.views.append(
            ft.View(
                "/",
                controls=[
                    ft.Row(controls=[title],
                           alignment=ft.MainAxisAlignment.CENTER,),
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
                        alignment=ft.MainAxisAlignment.CENTER)

                    ],),
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                bgcolor="#5271ff",
            )
        )
        if page.route == "/suma":
            page.views.append(
                ft.View(
                    "/suma",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
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
        if page.route == "/ayuda":
            page.views.append(
                ft.View(
                    "/ayuda",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
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