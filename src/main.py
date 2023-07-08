import uvicorn
from fastapi import FastAPI
import flet as ft
from fastapi.responses import RedirectResponse

app = FastAPI()
is_app_run = False


def main(page: ft.Page):
    """ Интерфейс главной страницы """
    global is_app_run
    if not is_app_run:
        is_app_run = True
        uvicorn.run(app, host='localhost', port=8001)
    page.title = 'Home page'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(ft.Text('Тестовая страница'))


@app.get('/api/ping')
def home_page():
    """ Главная страница """
    print('Отработал FastApi')
    return RedirectResponse('http://localhost:8000')


if __name__ == '__main__':
    is_uvicorn_run = False
    ft.app(target=main, view=None, port=8000)

