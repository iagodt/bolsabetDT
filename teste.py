from chatbot import enviarMensagem, formatarMensagem
from surebet import backtoback


msgodds = ''
partida = 'teste x teste'
msgformat = []

msgodds+=backtoback(['1.1','24','60'],'MoneyLine (BACK)')
msgodds+=backtoback(['24','1.1','60'],'MoneyLine (BACK)')
msgodds+=backtoback(['60','24','1.1'],'MoneyLine (BACK)')
msgodds+=backtoback(['9','1.32','18.5'],'MoneyLine (BACK)')
msgodds+=backtoback(['3.55','2.1','4'],'MoneyLine (BACK)')
msgodds+=backtoback(['150','15.5','1.06'],'MoneyLine (BACK)')



msgformat.append(f'Surebet Bolsa x Bolsa AO VIVO\n\n')
msgformat.append(f'🟢Partida: {partida}\n\n')
msgformat.append(msgodds)
msgformat.append(f'\nlink do jogo ⬇️⬇️⬇️\n\n{'url'}\n')
enviarMensagem(formatarMensagem(msgformat))