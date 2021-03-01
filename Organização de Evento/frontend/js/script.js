$(document).ready(function () {

    var urlX = "http://127.0.0.1:5000";
    $("#link_listar_pessoas").ready(function () {
        $.ajax({
            url: urlX + '/listar_pessoas',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listar_pessoas, // chama a função listar_pessoas para processar o resultado
            error: function () {
                alert("erro ao ler dados, verifique o backend");
            }
        });
        function listar_pessoas(pessoa) {
            // inicializar um acumulador
            linhas = ""
            // percorrer as plantas retornadas em json
            for (var i in pessoa) {

                // montar uma linha da tabela de plantas
                lin = "<tr id ='linha_" + "'>" +
                    "<td>" + pessoa[i].id_pessoa + "</td >" +
                    "<td>" + pessoa[i].p_nome + "</td >" +
                    "<td>" + pessoa[i].p_sobrenome + "</td>" +
                    "<td>" + pessoa[i].sala_1 + "</td>" +
                    "<td>" + pessoa[i].sala_2 + "</td>" +
                    "<td>" + pessoa[i].ecafe_1 + "</td>" +
                    "<td>" + pessoa[i].ecafe_2 + "</td>" +
                    "</tr >"
                // adicionar a linha da tabela em um acumulador
                linhas = linhas + lin;

            }
            // colocar as linhas na tabela
            $("#corpoTabelaPessoas").html(linhas);
        }
    });
    $("#link_listar_salas").ready(function () {
        $.ajax({
            url: urlX + '/listar_salas',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listar_salas, // chama a função listar_pessoas para processar o resultado
            error: function () {
                alert("erro ao ler dados, verifique o backend");
            }
        });
        function listar_salas(sala) {
            // inicializar um acumulador
            linhas = ""
            // percorrer as plantas retornadas em json
            for (var i in sala) {

                // montar uma linha da tabela de plantas
                lin = "<tr id ='linha_" + "'>" +

                    "<td>" + sala[i].id_sala + "</td >" +
                    "<td>" + sala[i].s_nome + "</td>" +
                    "<td>" + sala[i].lot1 + "</td >" +
                    "<td>" + sala[i].lot2 + "</td>" +
                    "</tr >"
                // adicionar a linha da tabela em um acumulador
                linhas = linhas + lin;

            }
            // colocar as linhas na tabela
            $("#corpoTabelaSalas").html(linhas);
        }
    });
    $("#link_listar_cafes").ready(function () {
        $.ajax({
            url: urlX + '/listar_cafe',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listar_cafe, // chama a função listar_pessoas para processar o resultado
            error: function () {
                alert("erro ao ler dados, verifique o backend");
            }
        });
        function listar_cafe(cafe) {
            // inicializar um acumulador
            linhas = ""
            // percorrer as plantas retornadas em json
            for (var i in cafe) {

                // montar uma linha da tabela de plantas
                lin = "<tr id ='linha_" + "'>" +

                    "<td>" + cafe[i].id_cafe + "</td >" +
                    "<td>" + cafe[i].cafe_nome + "</td>" +
                    "<td>" + cafe[i].lot1 + "</td >" +
                    "<td>" + cafe[i].lot2 + "</td>" +
                    "</tr >"
                // adicionar a linha da tabela em um acumulador
                linhas = linhas + lin;

            }
            // colocar as linhas na tabela
            $("#corpoTabelaCafe").html(linhas);
        }
    });
    $("#btn_add_pessoa").click(function () {
        //obter dados do formulário
        p_nome = $("#p_nome").val();
        p_sobrenome = $("#p_sobrenome").val();
        sala_1 = $("#sala_1").val();
        sala_2 = $("#sala_2").val();
        ecafe_1 = $("#ecafe_1").val();
        ecafe_2 = $("#ecafe_2").val();
        //dados pra envio(json)
        dados = JSON.stringify({

            p_nome: p_nome,
            p_sobrenome: p_sobrenome,
            sala_1: sala_1,
            sala_2: sala_2,
            ecafe_1: ecafe_1,
            ecafe_2: ecafe_2
        });
        // enviar ao back-end
        $.ajax({
            url: urlX + '/cadastar_Pessoa',
            type: 'POST',
            contentType: 'application/json',
            dataType: 'json',
            data: dados,
            success: cadastar_Pessoa,
            erro: erroAdicionarSpell
        });
        function cadastar_Pessoa(resposta) {
            //msg de sucesso
            if (resposta.resultado == "ok") {

                //limpar campos form
                $("#p_nome").val("");
                $("#p_sobrenome").val("");
                $("#sala_1").val("");
                $("#sala_2").val("");
                $("#ecafe_1").val("");
                $("#ecafe_2").val("");
            } else {
                alert("erro na comunicação")
            }

        }
    });

});
