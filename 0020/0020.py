from flask import Flask,request,render_template
from flask_wtf import Form
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import  DataRequired

class CommentForm(Form):
    name = StringField("姓名",validators=[DataRequired()])
    content = TextAreaField("留言",validators=[DataRequired()])
    submit = SubmitField('提交')

app = Flask(__name__)
app.config["SECRET_KEY"] = "SOME STRING"

@app.route("/",methods=['GET','POST'])
def index():
    comments = []
    for i in range(5):
        comment = {}
        comment["name"] = "游客" + str(i)
        comment["date"] =  "2017-09-21"
        comment["content"] =  "something comment"
        comments.append(comment)

    form = CommentForm()
    if form.validate_on_submit():
        comment_new = {}
        comment_new["name"] = form.name.data
        comment_new["date"] = "2017-09-28"
        comment_new["content"] = form.content.data
        comments.append(comment_new)

    return render_template('index.html',form = form,comments = comments)

if __name__ == "__main__":
    app.run(debug=True)