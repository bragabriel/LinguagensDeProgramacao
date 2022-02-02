<?php 

/*************************************/
/*               CRUD                */
/*  Create - Read - Update - Delete  */
/*************************************/

/*  OBS: Utilizando PHP procedural.  */

//Conexão
include_once 'php_action/db_connect.php';

//Incluindo o header
include_once 'includes/header.php';

//Incluindo a mensagem de alerta (Cadastrado com sucesso! / Erro ao cadastrar!)
include_once 'includes/message.php';

?>


<div class="row">
    <div class="col s12 m6 push-m3">
        <h3 class="light">Clientes</h3>
        <table class="striped">
            <thead>
                <tr>
                    <th>Nome:</th>
                    <th>Sobrenome:</th>
                    <th>Email:</th>
                    <th>Idade:</th>
                </tr>
            </thead>

            <tbody>
                <?php
                    $sql = "SELECT * FROM clientes";

                    //Atribuindo o resultado da consulta para a variável $resultado
                    //                      "conexão", "consultaSQL"
                    $resultado = mysqli_query($connect, $sql);

                    //Abrindo WHILE
                    //Variável $dados recebe todos os dados de $resultado ($resultado é a consulta ao Banco de Dados)
                    while($dados=mysqli_fetch_array($resultado)):
                    
                ?>
                <tr>
                    <td><?php echo $dados['nome']; ?></td>
                    <td><?php echo $dados['sobrenome']; ?></td>
                    <td><?php echo $dados['email']; ?></td>
                    <td><?php echo $dados['idade']; ?></td>
                    <td><a href="#" class="btn-floating orange"><i class="material-icons">edit</i></a></td>
                    <td><a href="#" class="btn-floating red"><i class="material-icons">delete</i></a></td>
                </tr>

                <?php
                    //Fechando WHILE
                    endwhile; 
                ?>

            </tbody>
        </table>
        <br>
        <a href="adicionar.php" class="btn">ADICIONAR CLIENTE</a>
    </div>
</div>


<?php 
    //Incluindo o footer
    include_once 'includes/footer.php';
?>