from chatbot import deletarMensagens, enviarMensagem


def percentProfit(odds=[], lucro = 0):
    lucroa = (((1/lucro) *100)-100)
    output = f'💰Lucro:{lucroa:.2f}%\n'
    return output
        
def backtoback(odds=[],text=''):
    res = 0
    ##print('btb',odds, text)
    if not '' in odds and len(odds)>0:
        
        for i in odds:
            
            try:
                if float(i) >= 1000:
                    return('')
                res += 1/float(i)            
            except:
                pass
            
        if res < 0.96780:
            return(f'➡Aposta: {text}\n{percentProfit(odds,res)}ODDS: {formatodds(odds)}\n\n')
        return('')
    return('')
            
    

def formatodds(odds=[]):
    texto = ''
    for i in odds:
        if texto == '':
            texto+= i
        else:
            texto+= f' - {i}'
    return texto