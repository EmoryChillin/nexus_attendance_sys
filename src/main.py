import flet as ft
from flet import (
    Container,
    FontWeight,
    TextField,
    CupertinoButton,
    Icons,
    app,
    Page,
    ElevatedButton,
    Column,
    Row,
    Stack,
    Text,
    CupertinoTextField,
    Padding,
    Colors,
    OutlinedButton,
    Alignment,
    alignment,
    MainAxisAlignment,
    ButtonStyle,
    FilledButton
)

import utils.date_picker_example as date_picker_example
# import Widget
from assets.shared.widget import *

def main(page: Page):
    page.title = "Nexus Attendance"
    page.padding = 20
    
    page.fonts = {
        "font_light" : "fonts/proximanova_light.ttf",
        "font_regular" : "fonts/proximanova_regular.ttf",
        "font_bold" : "fonts/proximanova_bold.ttf",
    }

    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.appbar = ft.AppBar(
        leading=Row(
            controls=[
                Text('Nexus',weight=FontWeight.BOLD, color='red'),
                Text('BI',weight=FontWeight.BOLD, color='blue')
            ]
        ),
        bgcolor=Colors.WHITE
    )

    upper_ = Container(
        content= Row(
            controls=[
                Text(
                    value="Time and Attendance",
                    size=27,
                    font_family='font_bold',
                    weight=FontWeight.W_500
                ),
                FilledButton(
                    text="Record Attendance",
                    height=40,
                    width=190,
                    color='white',
                    icon=Icons.ADD,
                    style=ButtonStyle(
                        bgcolor="blue"
                    )
                )
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
        ),
        bgcolor=Colors.GREY_300,
        border_radius=17,
        width=800,
        height=80,
        padding=15
    )

    datepart = Container(
        content= Row(
            controls=[
                OutlinedButton(
                    text="Date",
                    icon=Icons.CALENDAR_MONTH_ROUNDED
                ),
                OutlinedButton(
                    text="Search Employee",
                    icon=Icons.SEARCH_OUTLINED
                ),
                NextButton()
            ],
            alignment=MainAxisAlignment.START
        )
    )

    page.add(
        Column(
            controls=[
                upper_,
                datepart
            ]
        )
    )

if __name__=='__main__':
    app(target=main, assets_dir='assets')
