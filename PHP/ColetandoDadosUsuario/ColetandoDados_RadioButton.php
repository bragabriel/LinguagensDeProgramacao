<!--
Vídeo aula disponível pelo canal: "DFILITTO"
Link da vídeo aula: https://www.youtube.com/watch?v=Zo1H2TKsTQg&ab_channel=DFILITTO

PHP Básico - 20 Coletando dados do usuário Radio Button
-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
</head>
<body>
    <form method="post" action="Alomundoform.php">
        <p>Qual o seu nome?: </p>
        <input type="text" name="usuario"><br><br>
        <input type="radio" name="gender" value="Masculino" checked> Male<br>
        <input type="radio" name="gender" value="Feminino" > Female<br><br>
        <input type="submit" value="Enviar">
    </form>
</body>
</html>

