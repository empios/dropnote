import web
from web.template import ALLOWED_AST_NODES
from Models import RegisterModel, LoginModel, Note

web.config.debug = False
ALLOWED_AST_NODES.append('Constant')

urls = (
    '/', 'home',
    '/register', 'register',
    '/login', 'login',
    '/logout', 'logout',
    '/post-activity', 'noteActivity',
    '/login-activity', 'loginActivity',
    '/register-activity', 'registerActivity'
)

app = web.application(urls, globals())
sessions = web.session.Session(app, web.session.DiskStore("session"), initializer={'user': None})
session_data = sessions.initializer

render = web.template.render("Views/Templates", base="Main",
                             globals={'session': session_data, 'current_user': session_data['user']})


class home:
    def GET(self):
        noteMod = Note.Note()
        notes = noteMod.getAll()
        return render.Home(notes)


class register:
    def GET(self):
        return render.Register()


class registerActivity:
    def POST(self):
        data = web.input()
        regModel = RegisterModel.RegisterModel()
        regModel.save_user(data)


class login:
    def GET(self):
        return render.Login()


class loginActivity:
    def POST(self):
        data = web.input()
        logModel = LoginModel.LoginModel()
        isCorrect = logModel.check_user(data)
        if isCorrect:
            session_data["user"] = isCorrect
            return "success"
        return "error"


class logout:
    def GET(self):
        sessions['user'] = None
        session_data['user'] = None
        sessions.kill()
        return 'success'


class noteActivity:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']
        noteModel = Note.Note()
        noteModel.save_note(data)
        return "success"


if __name__ == "__main__":
    app.run()
