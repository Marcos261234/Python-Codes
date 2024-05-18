Algoritmo "Sweet Fly"


//opcao1
procedimento registrar_aviao()
inicio

   se (opc_aviao = 11) ou (opc_aviao = 22) ou (opc_aviao = 33) ou (opc_aviao = 44) entao
      escreval("Reserva feita para avião: ",opc_aviao)
   senao
      escreval("Número do avião não reconhecido!")
   fimse

fimprocedimento

Var
   opc, opc_aviao, opcao_2, qtd: inteiro
   aviao: vetor [0..3] de inteiro
   qtd_cadeira: vetor [0..3] de inteiro


Inicio
   aviao[0] <- 11
   aviao[1] <- 22
   aviao[2] <- 33
   aviao[3] <- 44

   repita opc

      escreval("Agendamento para aviões:")
      escreval("1) Registrar o número de cada avião.")
      escreval("2) Registrar o quantitativo de assentos disponíveis em cada avião.")
      escreval("3) Reservar passagem aérea.")
      escreval("4) Realizar consulta por avião.")
      escreval("5) Realizar consulta por passageiro.")
      escreval("6) Encerrar")
      leia(opc)

      limpatela

      escolha opc

      caso 1
         Escreval("Quantos aviões você quer para realizar o registro? ")
         leia(qtd)
         para opc_aviao de 0 ate qtd -1 faca
            escreval("Qual avião o senhor deseja cadastrar para reserva?")
            escreval("Temos os aviões: 11. 22. 33. 44.")
            leia(opc_aviao)
            registrar_aviao()
            
            limpatela
         fimpara

      caso 6
         escreval("Obrigado Por usar nosso setor de Agendamento!")

      fimescolha


   ate opc = 6


Fimalgoritmo