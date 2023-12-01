import flet as ft


def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_type = ft.TextField(
        value="Type", text_align=ft.TextAlign.LEFT, width=100)
    txt_board = ft.TextField(
        value="Board", text_align=ft.TextAlign.LEFT, width=100)

    def update(e):
        # print(txt_type.value + txt_board.value)
        print(f"{txt_type.value} {txt_board.value}")

    def read_csv():
        import csv
        datas = []
        with open("data/data.csv") as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                datas.append(row)
        f.close()
        return datas

    page.add(
        ft.Row(
            [
                ft.Container(
                    expand=1,
                    content=ft.Column(
                        [
                            txt_type,
                            txt_board,
                            ft.ElevatedButton(text="Read", on_click=read_csv),
                            ft.ElevatedButton(text="Update", on_click=update),
                            ft.ElevatedButton(text="Execute", on_click=update),
                        ],
                        width=500,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ),
                ft.Container(
                    expand=1,
                    content=ft.DataTable(
        
                        columns=[
                            ft.DataColumn(ft.Text("First name")),
                            ft.DataColumn(ft.Text("Last name")),
                            ft.DataColumn(ft.Text("Age"), numeric=True),
                        ],
                        rows=[
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(row[0])),
                                    ft.DataCell(ft.Text(row[1])),
                                    ft.DataCell(ft.Text(row[2])),
                                ],
                            ) for row in read_csv()
                        ],
                    ),
                ),
            ],
            # scroll=ft.ScrollMode.AUTO,

        )
    )


ft.app(target=main)
