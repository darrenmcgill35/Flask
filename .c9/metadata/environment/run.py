{"filter":false,"title":"run.py","tooltip":"/run.py","undoManager":{"mark":30,"position":30,"stack":[[{"start":{"row":0,"column":0},"end":{"row":13,"column":23},"action":"insert","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return \"Hello World\"","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":1}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"remove","lines":["'"],"id":2}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["\""],"id":3}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"remove","lines":["'"],"id":4}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["\""],"id":5}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"remove","lines":["'"],"id":6}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["\""],"id":7}],[{"start":{"row":10,"column":24},"end":{"row":10,"column":25},"action":"remove","lines":["'"],"id":8}],[{"start":{"row":10,"column":24},"end":{"row":10,"column":25},"action":"insert","lines":["\""],"id":9}],[{"start":{"row":11,"column":32},"end":{"row":11,"column":33},"action":"remove","lines":["'"],"id":10}],[{"start":{"row":11,"column":32},"end":{"row":11,"column":33},"action":"insert","lines":["\""],"id":11}],[{"start":{"row":11,"column":35},"end":{"row":11,"column":36},"action":"remove","lines":["'"],"id":12}],[{"start":{"row":11,"column":35},"end":{"row":11,"column":36},"action":"insert","lines":["\""],"id":13}],[{"start":{"row":12,"column":36},"end":{"row":12,"column":37},"action":"remove","lines":["'"],"id":14}],[{"start":{"row":12,"column":36},"end":{"row":12,"column":37},"action":"insert","lines":["\""],"id":15}],[{"start":{"row":12,"column":41},"end":{"row":12,"column":42},"action":"remove","lines":["'"],"id":16}],[{"start":{"row":12,"column":41},"end":{"row":12,"column":42},"action":"insert","lines":["\""],"id":17}],[{"start":{"row":0,"column":0},"end":{"row":13,"column":23},"action":"remove","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route(\"/\")","def hello():","    return \"Hello World\"","","if __name__ == \"__main__\":","    app.run(host=os.environ.get(\"IP\"),","            port=int(os.environ.get(\"PORT\")),","            debug=True)"],"id":18}],[{"start":{"row":0,"column":0},"end":{"row":13,"column":23},"action":"insert","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route(\"/\")","def hello():","    return \"Hello World\"","","if __name__ == \"__main__\":","    app.run(host=os.environ.get(\"IP\"),","            port=int(os.environ.get(\"PORT\")),","            debug=True)"],"id":19}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":9},"action":"remove","lines":["hello"],"id":20},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["i"]},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["n"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["d"]},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["e"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["x"]}],[{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":[","],"id":21}],[{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":[","],"id":22}],[{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":[" "],"id":23},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"insert","lines":["r"]},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"insert","lines":["e"]},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"insert","lines":["n"]},{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"insert","lines":["d"]},{"start":{"row":1,"column":29},"end":{"row":1,"column":30},"action":"insert","lines":["e"]},{"start":{"row":1,"column":30},"end":{"row":1,"column":31},"action":"insert","lines":["r"]}],[{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"insert","lines":["_"],"id":24},{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"insert","lines":["t"]},{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"insert","lines":["e"]},{"start":{"row":1,"column":34},"end":{"row":1,"column":35},"action":"insert","lines":["m"]}],[{"start":{"row":1,"column":35},"end":{"row":1,"column":36},"action":"insert","lines":["p"],"id":25},{"start":{"row":1,"column":36},"end":{"row":1,"column":37},"action":"insert","lines":["l"]},{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"insert","lines":["a"]},{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"insert","lines":["t"]},{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":25},"action":"remove","lines":["\"Hello, World\""],"id":26},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["r"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["e"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["n"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["d"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["e"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["r"]}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":17},"action":"remove","lines":["render"],"id":27},{"start":{"row":8,"column":11},"end":{"row":8,"column":26},"action":"insert","lines":["render_template"]}],[{"start":{"row":8,"column":26},"end":{"row":8,"column":28},"action":"insert","lines":["()"],"id":28}],[{"start":{"row":8,"column":27},"end":{"row":8,"column":29},"action":"insert","lines":["\"\""],"id":29}],[{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["i"],"id":30},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"insert","lines":["n"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["d"]},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["e"]},{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"insert","lines":["x"]}],[{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"insert","lines":["."],"id":31},{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"insert","lines":["h"]},{"start":{"row":8,"column":35},"end":{"row":8,"column":36},"action":"insert","lines":["t"]},{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["m"]},{"start":{"row":8,"column":37},"end":{"row":8,"column":38},"action":"insert","lines":["l"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":23},"end":{"row":13,"column":23},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1568814455062,"hash":"9037fdedea93fac961357eb2e9cce63bd633d73d"}