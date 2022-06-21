"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""


from flask import Flask

app = Flask(__name__)

app.config.update(ENV="development")

@app.route("/")
def root():
    return "<p>Hello, Roo000000000oot!</p>"


@app.route("/about")
def about():
    return "<p>About, Roo000000000oot!</p>"


if __name__ == '__main__':
    app.run(debug=True)
