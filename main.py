from flask import request, Flask, jsonify
from google.appengine.ext import ndb

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get():
    key = request.args.get('id')
    account_key = ndb.Key(Profile, key)
    profile = account_key.get()
    return jsonify(profile.to_dict())

@app.route('/save', methods=['POST'])
def save():
    profile = Profile(id=request.json['id'])
    profile.data = request.json['data']
    profile.put()
    return 'ok', 204


if __name__ == '__main__':
    app.run()


class Profile(ndb.Model):
    data = ndb.StringProperty()
