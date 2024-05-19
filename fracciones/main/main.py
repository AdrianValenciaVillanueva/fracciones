import flet as ft

title =ft.Text(
    text_align=ft.TextAlign.CENTER,
    value=f"Fracciones",
    size=60,
    color = "black",
)

def createContainer(symbol, on_click, color1, color2, page):
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
        on_click=lambda e: on_click(e, page)
    )

    outer_container.content = inner_container
    return outer_container

def on_suma_click(e, page: ft.Page):
    # Limpiamos la página
    page.clean()
    # Agregamos el nuevo contenido
    page.add(ft.Text(value="Estás en la ventana de suma", color="black", size=50, text_align=ft.TextAlign.CENTER))

def on_resta_click(e, page: ft.Page):
    # Limpiamos la página
    page.clean()
    # Agregamos el nuevo contenido
    page.add(ft.Text(value="Estás en la ventana de resta", color="black", size=50, text_align=ft.TextAlign.CENTER))

def on_multi_click(e, page: ft.Page):
    # Limpiamos la página
    page.clean()
    # Agregamos el nuevo contenido
    page.add(ft.Text(value="Estás en la ventana de multiplicacion", color="black", size=50, text_align=ft.TextAlign.CENTER))

def on_divi_click(e, page: ft.Page):
    # Limpiamos la página
    page.clean()
    # Agregamos el nuevo contenido
    page.add(ft.Text(value="Estás en la ventana de divi", color="black", size=50, text_align=ft.TextAlign.CENTER))

def on_informacion_click(e, page: ft.Page):
    # Limpiamos la página
    page.clean()
    image_path = "C:\\Users\\Dario\\Desktop\\partes.png"
    page.add(ft.Image(image_path, width=600, height=600))

def main(page: ft.Page):
    containerSuma = createContainer("+", on_suma_click, "#33915c", "#4bb36c", page)
    containerResta = createContainer("-", on_resta_click, "#f8bc25", "#ffd633", page)
    containerDivision = createContainer("x", on_multi_click, "#5c8ad6", "#5cb2e8", page)
    containerMultiplicacion = createContainer("÷", on_divi_click, "#c20829", "#eb2b47", page)
    containerInformacion = createContainer("?", on_informacion_click, "#a245f7", "#a552f2", page)

    page.adaptive = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    color = "#5271ff"
    page.bgcolor = color

    page.add(
        title,
        ft.Column([
            ft.Row(controls=[
                containerSuma,
                containerResta,   
            ],
            alignment=ft.MainAxisAlignment.CENTER
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

        ]),
    )

ft.app(main)