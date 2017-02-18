import web

render = web.template.render('templates/')

urls = (
    '/', 'index'

)

class index:
    def GET(self):
        name = 'Bob'
        return render.index(name)


#testing around with this class, not sure if this is the right direction
class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i. title)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
