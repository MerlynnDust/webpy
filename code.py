import web

render = web.template.render('templates/')



web.config.smtp_server = 'smtp.gmail.com'
web.config.smtp_port = 587
web.config.smtp_username = 'cookbook@gmail.com'
web.config.smtp_password = 'secret'
web.config.smtp_starttls = True


urls = (
    '/', 'index'
    '/add','add'
)

class index:
    def GET(self):
        name = 'Bob'
        return render.index(name)

class add:
    def ADD(self):
        message = web.input()
        web.sendmail('cookbook@gmail.com', 'email', 'subject', 'message')


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
