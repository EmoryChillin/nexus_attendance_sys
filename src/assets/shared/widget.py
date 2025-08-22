from flet import (
      Container,
      Row,
      Image,
      Text,
      padding,
      ControlEvent,
      Colors,
      Column
)

from typing import Optional


class NextButton(Container):
      def __init__(
                  self,
                  icon: Optional[str] = None,
            ):
            super().__init__()

            self.icon = "icons/user.svg" if icon is None else icon

            self.content = Row(
                  controls=[
                        Image(
                              src=self.icon,
                              height=16
                        ),
                        Column(width=0),
                        Text(
                              value="Button",
                              font_family="font_regular",
                              size=17
                        )
                  ]
            )

            self.bgcolor = "#F5F5F7"
            self.padding = padding.symmetric(
                  vertical=10,
                  horizontal=22
            )
            self.border_radius = 12
            self.on_hover = self.button_hover


      def button_hover(self, e: ControlEvent) -> None:
            self.bgcolor = Colors.GREY_300 if self.bgcolor == "#F5F5F7" else "#F5F5F7"
            self.update()
