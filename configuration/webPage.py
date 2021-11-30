def web_page():
    html = """<!DOCTYPE htlm>
<html lang="es">

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta charset="utf-8" >
    <base href=\ target="_blank">
    <style>
        html {
            font-family: Arial;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
        }

        .button {
            background-color: #ce1b0e;
            border: none;
            color: white;
            padding: 16px 40px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }

        .button1 {
            background-color: #000000;
        }

        .par {
            border:#000000 5px solid;
            width: fit-content;
            margin: 10px;
            padding: 5px;
            text-align: center;
            display: inline-block;
        }
    </style>
</head>

<body>
    <h2>MicroPython Web Server</h2>
    <div class="par">
        <p>        
        Suavizado del acelerometro
        </p>
        <input type="text" id="suav" value="0.5"></input>
        <div>
            <button onclick="add_alpha()">+</button>
            <button onclick="subs_alpha()">-</button>
        </div>
    </div>
    <div class="par">
        <p>
        Fijar límite de ultrasonidos
        </p>
        <input type="text" id="ult" value="1"></input>
        <div>
            <button onclick="add()">+1</button>
            <button onclick="subs()">-1</button>
            <button onclick="mult()">x10</button>
            <button onclick="div()">/10</button>
        </div>
    </div>
        <p>
            <a href=# id="final"><button class="button" onclick="end_ult()">submit</button></a>
        </p>
    
    <script>
        var i = 1;
        var a = 0.5;
        function add() {
            document.getElementById('ult').value = ++i;
        }
        function subs(){
            document.getElementById('ult').value = --i;
        }
        function mult(){
            i = i*10 
            document.getElementById('ult').value = i;
        }
        function div(){
            i = i/10 
            document.getElementById('ult').value = i;
        }
        function add_alpha() {
            if(a<1)
                a = Number(a)+ 0.1;
            else
                a = 1;

           a = Number.parseFloat(a).toPrecision(1)

            document.getElementById('suav').value = a;
        }
        function subs_alpha(){
            if(a>0)
                a = Number(a) - 0.1;
            else   
                a = 0;

            a = Number.parseFloat(a).toPrecision(1)

            document.getElementById('suav').value = a;
        }
        function end_ult(){
            document.getElementById('final').href="?alpha="+a+ "?dist=" + i + "?endVar";
        }

    </script>
</body>

</html>"""
    return html