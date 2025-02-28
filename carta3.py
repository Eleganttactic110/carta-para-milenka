import webbrowser
import os

# Mensaje de detalle en HTML con un sobre clicable
html = """
<!DOCTYPE html>
<html>
<head>
<title>Un pequeño detalle para ti</title>
<style>
    body { text-align: center; font-family: Arial, sans-serif; margin: 0; padding: 20px; }
    .envelope { cursor: pointer; margin-top: 50px; width: 100%; max-width: 200px; }
    .message { display: none; margin-top: 50px; }
    img { width: 100%; max-width: 250px; }
</style>
<script>
    function openMessage() {
        document.getElementById('message').style.display = 'block';
        document.getElementById('envelope').style.display = 'none';
    }
</script>
</head>
<body>
<h1>🌹Hola Milenka!🌹</h1>
<p>Por favor haga clic en el sobre para abrir su mensaje😉:</p>
<img id="envelope" class="envelope" src="https://i.pinimg.com/736x/b3/4d/34/b34d342d4fd2082809e0d221c82dcef6.jpg" alt="Sobre" onclick="openMessage()">
<div id="message" class="message">
    <p>Espero que este pequeño detalle te saque una sonrisa.😁🌹</p>
    <p>Me alegro haber podido hablar contigo despues mucho tiempo, la verdad el tiempo que paso lejos de ti parece una eternidad y ya que no tienes un cancel para dejarte cartas como antes decidi crear este detalle para ti, asi mismo te agradezco por tu tiempo para ver y leer este pequeño detalle.</p>
    <p><img src="https://img.freepik.com/vector-gratis/ilustracion-vector-dos-corazones-felices-mirando-al-otro-hablando-telefono_1150-40460.jpg" alt="Corazón"></p>
    <p>Siempre me ha fascinado la dedicación y responsabilidad que le pones a todas tus actividades. Eres una mujer maravillosa, nunca lo olvides y recuerda que eres muy valiosa e importante para mi. Le agradezco a Dios por tu vida, y estoy seguro de que seráa la más bella y amable de las profesionales del mundo. Nunca te rindas por conseguir tus metas y si necesita un apoyo siempre estare aqui para ti se que han pasado muchas cosas, pero prometo estar incondicionalmente para ti.❤🙌🌹</p>
    <p>Un abrazo y un beso para la dueña d emi corazon, y nunca olvides de sonreír y ser la luz que ilumina la vida de todos quienes te conocemos. Mientras llega el momento de encontrarnos de nuevo en el que permitas invitarte a salir, te dejo este pequeño detalle🙌. Espero sea de su agrado, disculpa si te molesto pero la verdad es que tu me gustas y quisiera preguntarte una vez mas si me podrias dar una oportunidad? yo la verdad si quiero conocerte pero no quiero ser solo tu amigo y el motivo de mi insistencia es por que considero que eres unica en el mundo y que de verdad te amo y no me da miedo decirlo por que es lo que siento por ti, nunca me vas a molestar <br>
    ¿Podrias darme una oportunidad de demostrarte lo mucho que me gustas y que mis sentimientos por ti son reales? (si?/no?) Estare esperando tu respuesta por que mi amor por ti es incondicional</p>
    <p>Att: Anthony R.😊</p>
    <p>🌹Ты самая красивая и никогда не меняешься.🌹</p>
</div>
</body>
</html>
"""

# Guarda el mensaje en un archivo HTML con codificación UTF-8
with open("detalle_para_milenka.html", "w", encoding="utf-8") as file:
    file.write(html)

# Abre el archivo HTML en una nueva pestaña del navegador
webbrowser.open("file://" + os.path.realpath("detalle_para_milenka.html"))
