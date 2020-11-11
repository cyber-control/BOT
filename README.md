# BOT
um bot para diversas automações


O BOT foi lançado 10/11/2020 ainda não esta completo e nem possui todas as funcionalidades, o bot é operante no unico site que ele possui agora (ganhar no insta, um site que lhe paga uma baixa porcentagem do dinheiro de seus patrocinadores para que você siga os tais patrocinadores no instagram ou curta suas publicações) com exceção da funcionalidade de curtir! provavelmente amanhã a noite ela já estará inclusa no bot tambem.
Modo de usar:
python BOT.py {opções de uso: -f -i} $seu_email_do_face_ou_insta $respectiva_senha {opções de uso: --gni} $seu_email_do_ganhar_no_insta $respectiva_senha {opções de uso: --headless -head}

parametros:
-f faz com que o BOT acesse seu insta pelo face
-i acessa pelo proprio insta
--gni é a função correspondente ao site no qual ele vai realizar a automação 
--head permite que o BOT abra uma janela do navegador para que você veja o processo
--headless tudo é feito sem que o navegador seja aberto, você sera orientado pela legenda no terminal

obs: somente sera possivel usar o BOT em sistemas linux e apenas com o firefox instalado!
você precisará do geckodriver que já esta disponivel no repositorio e do selenium e python3
caso não tenha o geckdriver faça o download e copie ele para /usr/local/bin
