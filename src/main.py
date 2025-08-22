import flet as ft
import utils.date_picker_example as date_picker_example
from flet import (
Container, FontWeight,
TextField,CupertinoButton,
Icons,app,ElevatedButton,
Column,Row,Stack,
Text,CupertinoTextField,
Padding,Colors,OutlinedButton,
Alignment,alignment
)


def main(page: ft.Page):
    page.title = "Nexus Attendance"
    page.padding = 20
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER

    upper_ = Container(
        content= Row(
            controls=[
                Text("Time and Attendance",
                     size=27,font_family='Poppins',
                     weight=FontWeight.W_500),
                ft.FilledButton(text = "Record Attendance",
                                height=40,
                                width=190,
                                color = 'white',
                                icon=Icons.ADD,
                                style=ft.ButtonStyle(bgcolor=Colors.BLUE_900))
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
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
                OutlinedButton("Date", icon=Icons.CALENDAR_MONTH_ROUNDED),
                OutlinedButton("Search Employee", icon=Icons.SEARCH_OUTLINED)
            ],
            alignment=ft.MainAxisAlignment.START
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
    app(target=main,assets_dir='assets')
