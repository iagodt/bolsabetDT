import telebot

token = '6511952346:AAHQmU3DSG2tiB-VeDFvDB7XiIU8xHf-VTU'
chatid = '-1002082504631'
message = ''
mensageids = []

bot = telebot.TeleBot(token)

def formatarMensagem(textos = []):
    mensagemfinal = ''
    for i in textos:
        mensagemfinal += f'{i}'
    return(mensagemfinal)
def enviarMensagem(texto):
    try:
        message = bot.send_message(chatid,texto)
        mensageids.append(message.id)
    except:
        pass
    finally:
        pass
def deletarMensagens():
    
    global messageids
    if mensageids == []:
        return None
    try:
        bot.delete_messages(chatid,mensageids)
        mensageids.clear()
    except:
        pass
    finally:
        pass

