from eve import Eve

app = Eve()

# TODO: set up custom action to upload images
@app.route('/hello')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
