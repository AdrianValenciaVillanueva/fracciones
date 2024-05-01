import flet as ft

title =ft.Text(
    text_align=ft.TextAlign.CENTER,
    value=f"Fracciones",
    size=60,
    color = "black",
)


def createContainer(image_name, on_click,color1,color2):
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
        alignment=ft.alignment.center,
        bgcolor= color2,
        width=100,
        height=88,
        border_radius=10,
        content=ft.Image(src = f"{image_name}.png"),
        ink=True,
        on_click=on_click
    )

    outer_container.content = inner_container
    return outer_container

# Uso de la función
def on_click_handler(e):
    print("clicked")

containerSuma = createContainer("icon", on_click_handler,"#33915c","#4bb36c")
containerResta = createContainer("icon", on_click_handler,"#f8bc25","#ffd633")
containerDivision = createContainer("icon", on_click_handler,"#5c8ad6","#5cb2e8")
containerMultiplicacion = createContainer("icon", on_click_handler,"#c20829","#eb2b47")
def main(page: ft.Page):
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
         alignment=ft.MainAxisAlignment.CENTER)
    ]),
    
)


ft.app(main)
