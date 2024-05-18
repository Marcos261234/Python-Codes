Algoritmo "SweetFly"

tipo
   reserva = registro
      nr_aviao: inteiro
      passageiro: caractere
   fimregistro

   //OPCAO 1
procedimento registrar_aviao()
inicio
   escreval("...REGISTRO DE AVIÕES...")
   para i de 0 ate 3 faca
      escreval("Informe o nr do avião ", i+1)
      leia(checkin[i].nr_aviao)
      aviao[i] <- checkin[i].nr_aviao
   fimpara
fimprocedimento

//OPCAO 2
procedimento registrar_assentos()
inicio
   escreval("...REGISTRO DE ASSENTOS...")
   para i de 0 ate 3 faca
      escreval("Informe a quantidade de assentos do aviao ", i+1)
      leia(assentos[i])
   fimpara
fimprocedimento


//FUNÇÃO VERIFICA AVIÃO
funcao verifica_aviao(aviao_reserva: inteiro):logico
var
   achou: logico
inicio

   achou <- falso

   para i de 0 ate 3 faca
      se aviao[i] = aviao_reserva entao
         indice_reserva <- i
         achou <- verdadeiro
      fimse
   fimpara

   retorne achou
fimfuncao

//FUNÇÃO VERIFICA ASSENTOS
funcao verifica_assentos(aviao_reserva: inteiro): logico
var
   tem_assentos: logico
inicio

   tem_assentos <- falso

   se assentos[indice_reserva] > 0 entao
      escreval("Avião tem ", assentos[indice_reserva], " assentos disponíveis.")
      tem_assentos <- verdadeiro
      assentos[indice_reserva] <- assentos[indice_reserva] - 1
   fimse

   retorne tem_assentos
fimfuncao

//OPCAO 3
procedimento fazer_reserva()
var
   aviao_reserva: inteiro
   passageiro_reserva: caractere

inicio
   escreval("...RESERVAS...")
   escreval("Informe o nr do aviao para reserva")
   leia(aviao_reserva)

   se verifica_aviao(aviao_reserva) entao
      se verifica_assentos(aviao_reserva) entao
         escreval("Faça sua Reserva")
         escreval("Diga o seu nome: ")
         leia(checkin[i].passageiro)
         escreval("Obrigador sr/a ",checkin[i].passageiro," por fazer sua reserva com nossa Companhia")
         nome_passageiro[i] <- checkin[i].passageiro
         //implementar
      senao
         escreval("Não existem mais assentos disponíveis")
      fimse
   senão
      escreval("Avião não localizado")
   fimse
fimprocedimento

procedimento consulta_aviao()
var
   aviao_consulta: inteiro
   encontrado: logico
inicio
   encontrado <- falso
   escreval("...CONSULTA DE AVIÃO...")
   escreval("Informe o número do avião que deseja consultar:")
   leia(aviao_consulta)

   para i de 0 ate 3 faca
      se aviao[i] = aviao_consulta entao
         escreval("Avião encontrado! Nr. Avião: ", aviao_consulta, " Assentos disponíveis: ", assentos[i])
         encontrado <- verdadeiro
      fimse
   fimpara

   se nao encontrado entao
      escreval("Avião não encontrado.")
   fimse
fimprocedimento

procedimento consulta_passageiro()
var
   passageiro_consulta: caractere
   encontrado: logico
   aviao_consulta: inteiro
inicio
   encontrado <- falso
   escreval("...CONSULTA DE PASSAGEIRO...")
   escreval("Informe o nome do passageiro que deseja consultar:")
   leia(nome_passageiro[i])
   escreval("Digite o numero do avião em qual o passageiro se encontra:")
   leia(aviao_consulta)

   para i de 0 ate 3 faca
      se nome_passageiro[i] = passageiro_consulta entao
         encontrado <- verdadeiro
      fimse
   fimpara
   escreval("Passageiro encontrado! Nr. Avião: ",aviao_consulta, " Nome do Passageiro: ", nome_passageiro[i])

   se nao encontrado entao
      escreval("Passageiro não encontrado.")
   fimse
fimprocedimento

Var
   aviao: vetor[0..3] de inteiro
   assentos: vetor[0..3] de inteiro
   nome_passageiro: vetor[0..39] de caractere
   checkin: vetor[0..19] de reserva
   opcao, i, indice_reserva: inteiro

Inicio

   repita
      escreval("SWEET FLY")
      escreval("MENU:")
      escreval("1: Registrar o número de cada avião.")
      escreval("2: Registrar o quantitativo de assentos disponíveis em cada avião.")
      escreval("3: Reservar passagem aérea.")
      escreval("4: Realizar consulta por avião.")
      escreval("5: Realizar consulta por passageiro.")
      escreval("6: Encerrar.")
      leia(opcao)
      limpatela

      escolha opcao
      caso 1
         registrar_aviao()
      caso 2
         registrar_assentos()
      caso 3
         fazer_reserva()
      caso 4
         consulta_aviao()
      caso 5
         consulta_passageiro()
      fimescolha

   ate opcao = 6

   escreval("Obrigado por utilizar o SWEET FLY!")

Fimalgoritmo