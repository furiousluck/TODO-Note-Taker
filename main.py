from distutils.log import debug
from website import create_app
# if we put __init__.py in folder it acts as a package

app = create_app()

if __name__ == '__main__': #we only want to run web server if we insert this line
    app.run(debug=True)
    # debug = True : if we want to reload after every change, we should turn it off in production
