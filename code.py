import web

render = web.template.render('templates/')



web.config.smtp_server = 'smtp.gmail.com'
web.config.smtp_port = 25
web.config.smtp_username = '<mailserveremailgoeshere>'
web.config.smtp_password = '<passwordforemailgoeshere>'
web.config.smtp_starttls = True


urls = (
    '/', 'index',
    '/contactus','contactus'
)

class index:
    def GET(self):
        name = 'Bob'
        return render.index(name)

class contactus:
    def POST(self):
        msg = web.input()
        messagem = msg['message']
        subjectm = msg['name']
        emailm = msg['email']
        web.sendmail('<mailserveremailgoeshere>', '<emailwhereyouwantyourmailgoeshere>',str(subjectm),"this is from " + str(emailm) + " " + str(messagem))

        return render.contactus()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
