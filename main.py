from flask import Flask,request, jsonify, render_template
import random
import sys
import os
import shutil
import requests


#VARIABLE DE CONFIG
token_dir = "discordSECRETS/token.txt"

name = token_dir

token = os.environ.get('token')
linkweb = "http://127.0.0.1:5000/"

#TEMPLATES VAR
styles = ["../static/css/main.css",
          "../static/css/styles/green.css",
          "../static/css/styles/red.css",
          "../static/css/styles/purple.css",
          "../static/css/styles/orange.css"]



    
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/id')
def get_userinfo():
    user_id = request.args.get('')
    style = request.args.get("st")
    print(user_id)
    print(style)
    num_of_style = 0
    if style == None:
        num_of_style = 0
    else:
        num_of_style = int(style)
    print(num_of_style)
    headers = {
        'Authorization': f'Bot {token}'
    }
    try:
        response = requests.get(f'https://discord.com/api/users/{user_id}', headers=headers)
        if response.status_code == 200:
            user_info = response.json()
            if 'id' in user_info and 'avatar' in user_info:
                avatar_url = f'https://cdn.discordapp.com/avatars/{user_info["id"]}/{user_info["avatar"]}.png'
                username = user_info["username"]
                tag = user_info["discriminator"]
                copy = f"{username}#{tag}"
                if "None.png" in avatar_url:
                    avatarimg = "default.png"
                if "None.png" not in avatar_url:
                    avatarimg = avatar_url + "?size=1024"
                print(copy)
                print(user_info)
                print(avatar_url + "?size=1024")
                titlen = f"Discord-{username}"
                try:
                    return render_template("id.html",
                                       style = styles[num_of_style],
                                       title = titlen,
                                       username = username,
                                       tag = "#"+tag,
                                       copycomplete = copy,
                                       linkimg = avatarimg,
                                       linkweb = linkweb)
                except:
                    return render_template("404.html")
                """return jsonify({
                    'username': username,
                    "tag" : tag,
                    'avatar_url': avatar_url + "?size=1024"
                })"""
            else:
                return render_template("404.html")
                """return jsonify({
                    'error': 'Could not retrieve user information'
                }), 404"""
        else:
            return render_template("404.html")
            """return jsonify({
                'error': f'Request failed with status code {response.status_code}'
            }), 404"""
    except requests.exceptions.RequestException as e:
        return jsonify({
            'error': f'Request failed with exception {str(e)}'
        }), 404
    

    
@app.errorhandler(404)
def pagenotfound(e):
    print("404")
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

    





if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=8080)

