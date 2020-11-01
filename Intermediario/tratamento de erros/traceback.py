
#** mensagem de erros são importantes 
#** o traceback inclui a mensagem de erro, o numero da linha que causou o erro e a sequencia de funções que levaram ao erro. Essa sequencia é chamada de call stack

def spam():
    bacon()

def bacon():
    raise Exception('error')

spam()