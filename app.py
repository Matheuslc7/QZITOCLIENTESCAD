from modelos.Clientes import Cliente

cliente_matheus = Cliente('matheus', 'maracanaú-Ce')
cliente_matheus.receber_avaliacao('Tayane', 300)
cliente_matheus.receber_avaliacao('Tayane', 70)
cliente_thayne = Cliente('Thayne', 'Caruaru-Pe')
cliente_thayne.receber_avaliacao('Tayane', 400)
cliente_thayne.receber_avaliacao('Tayane', 80)
cliente_aline = Cliente('Aline', 'Cajazeiras-Pb')
cliente_aline.receber_avaliacao('Tayane', 200)
cliente_aline.receber_avaliacao('Tayane', 70)
cliente_samuel = Cliente('Samuel', 'Mossoró-Rn')
cliente_samuel.receber_avaliacao('Tayane', 25)
cliente_samuel.receber_avaliacao('Tayane', 170)
cliente_thais = Cliente('Thais', 'Picos_Pi')
cliente_jessica = Cliente('jéssica', 'fortaleza-Ce')
cliente_jessica.receber_avaliacao('Tayane', 250)
cliente_jessica.receber_avaliacao('Tayane', 170)

cliente_matheus.alternar_status()
cliente_aline.alternar_status()
cliente_jessica.alternar_status()

def main():
    Cliente.listar_clientes()


if __name__ == '__main__':
    main()
