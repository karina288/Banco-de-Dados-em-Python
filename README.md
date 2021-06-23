# Banco-de-Dados-em-Python
Trabalho realizado para a disciplina de Programação de Computadores I ministrada pelo professor Luis Antônio Kowada, no semestre de 2019.1.

BANCO DE DORAMAS é um programa em python desenvolvido para funcionar como um organizador pessoal de uma dorameira(o). O programa permite que o usuário tenha seus doramas(séries asiáticas) listados, organizados e guardados em um banco de dados. Esse banco de dados é organizado em 6 campos, nome, tipo,gênero, nº de episódios, terminado[S/N] e episódios de parada. Com esses campos o usuário poderá ter um controle sobre os doramas que está assistindo ou que já assistiu.

O programa possui funções em seu código fonte que são responsáveis por permitir ao usuário desfrutar de um menu de opções quando estiver utilizando o  banco de doramas. As opções são variadas, como pode se ver a seguir:

MENU INICIAL:
[ 1 ] - Criar tabela
[ 2 ] - Gravar tabela no arquivo
[ 3 ] - Ler tabela do arquivo
[ 4 ] - Apagar tabela do arquivo
[ 5 ] - Listar dados da tabela 
[ 6 ] - Consultar um registro 
[ 7 ] - Inserir novo registro na tabela
[ 8 ] - Apagar registro
[ 9 ] - Listagem total ou filtrada
[ 0 ] - Sair do programa

Explicação acerca de cada função contida no código fonte:

Função criar_tabela:
Cria uma tabela/arquivo do zero com os campos. Permitindo ao usuário escolher o nome com que o arquivo será salvo.

Função  gravar_tabela:
Permite ao usuário gravar dados na tabela de um determinado arquivo, auxiliando o usuário no preenchemento dos campos.

Função ler_tabela:
Mostra na tela, os dados contidos na tabela, permitindo ao usuário escolher um arquivo para visualizar as informações dos doramas contidos na tabela.

Função apagar_tabela:
Permite ao usuário escolher entre duas opções. Apagar apenas os dados contidos na tabela, mas manter o arquivo ou apagar o arquivo inteiro.

Função listardados_tabela:
Permite ao usuário duas opções, ordenar os doramas por ordem alfabética ou por número de episódios e dependendo da escolha do usuário, mostrar 
na tela após a ordenação.

Função consultar_registro:
Permite ao usuário digitar o nome de um dorama e, a partir disso, a função irá procurar pelo nome no banco de doramas e mostrará apenas as informações daquele dorama em específico.

Função inserir_novoregistro:
Chama a função gravar_tabela, que permite ao usuário gravar um as informações de um novo dorama na lista.Comprindo assim, a função de inserir um novo registro na tabela.

Função apagar_registro:
Permite ao usuário digitar nome de um dorama e assim apagar o registro deste na tabela.

Função listagem_total_filtrada:
Permite ao usuário mostrar na tela a tabela, mas com duas opções de escolha. Listagem total, que mostrará todos os dados dos doramas contidos na tabela.Já a opção de listagem filtrada será feita baseada no tipo de dorama, oferecendo ao usuário opção de visualizar apenas seus doramas do tipo K-drama, J-drama,
C-drama ou Thai-drama.

Função sair_programa:
Encerra o programa se o usuário digitar 0, como indicado no menu inicial.



