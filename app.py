from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story

app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True
app.config['SECRET_KEY'] = 'coolcode' # set a 'SECRET_KEY' to enable the Flask session cookies

toolbar = DebugToolbarExtension(app)

#Page where you input madlibs.
@app.route("/", methods=['GET'])
def madlib_form():

    id = request.args.get("id", type=int)

    #if type(id) == None:
    return render_template("madlibs_form.html", parts=story.prompts)
    
@app.route("/story", methods=['POST'])
def madlib_display():

    id = request.args.get("id", type=int)
    #if type(id) == None:
    return f"""{story.generate(request.form)}"""

