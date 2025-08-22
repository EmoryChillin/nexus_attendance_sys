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
                     size=30,
                     weight=FontWeight.BOLD),
                ElevatedButton("Record Attendance", icon=Icons.ADD)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )
    datepart = Container(
        content= Row(
            controls=[
                OutlinedButton("Date", icon=Icons.CALENDAR_MONTH),
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
