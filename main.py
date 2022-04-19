from hashlib import sha256

from flask import Flask, request, render_template

app = Flask(__name__)
MAX_NONCE = 100000000000

#This function convert text to sha256 format .Standard function
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

@app.route('/')
def login():
    return (render_template("miner.html"))

@app.route('/miner', methods=['POST','GET'])
#Start mining
def mine():

#todo if statement if form is empty

    blocknumber = request.form.get('block_number')
    # nonce = request.form.get('nonce')
    merkelroot = request.form.get('transactions')

    previushash = request.form.get('previoushash')
    difficulty = request.form.get('diff')

    global new_hash
    difflast = int(difficulty)
    prefix_str = '0' * difflast


    for nonce in range(MAX_NONCE):
        text = str(blocknumber) + str(merkelroot )+ str(previushash) + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):

           break
        print(new_hash)


    return (render_template("miner.html",message=new_hash ))



if __name__ == "__main__":
    app.run(debug=True)