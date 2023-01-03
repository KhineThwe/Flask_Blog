from flask import Blueprint,request,render_template
from flask_blog.models import Post
from flask_login import login_required

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
@login_required
def home():
    page = request.args.get('page',1,type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=5)
    return render_template('home.html',posts=posts)

@main.route("/about")
@login_required
def about():
    return render_template('about.html',title='About')