"""
import unidecode
import requests 
import json

try:
    from rich import print
except Exception as e:
    print("[yellow][ERROR][/yellow] no color print")


def get_lib():
    result = requests.get( 
              "https://raw.githubusercontent.com/Qypol342/Hashtag/main/hashtag_list.json") 
    return  json.loads(result.text)






def hashtag(text=''):
    print("[bold green][INFO][/bold green] Incoming request")

    allow = [',','.',' ','!','?',"'",'"',":",";","(",")"]
    
    try:   
        lib = get_lib()
    except Exception as e:
        print("could not reatch git:",e)
        f = open('hashtag_list.json')
        lib = json.load(f)
    
    for i, v in lib.items():

        if len(text) >= 280:
            print("[bold red][ERROR][/bold red] text to long to add hashtag")
            break
        
        text_low = unidecode.unidecode(text).lower()
        
        
        if i in text_low :

            
            if text_low.index(i) == 0 or text[text_low.index(i)-1] != '#':

                if text_low.index(i) != 0:
                    print("cheking first char",text[text_low.index(i)-1],"in",text[text_low.index(i)-1] not in allow)


                if text_low.index(i) != 0 and text[text_low.index(i)-1] not in allow: 
                    """
                    arreter si le caractère devant fait pas parti de la liste autoriser
                    """
                    continue
                if text_low.index(i)+len(i)< len(text):

                    print("cheking last char",text[text_low.index(i)+len(i)],"in",text[text_low.index(i)+len(i)] not in allow)
                if text_low.index(i)+len(i)< len(text) and text[text_low.index(i)+len(i)] not in allow:
                    """
                    arreter si le caractère apres fait pas parti de la liste autoriser
                    """
                    continue


                else:
                    print("[bold green][INFO][/bold green] hashtag found :",lib[i])
                    inn = text_low.index(i)
                    
                    text = text[:inn] + lib[i] + text[inn + len(i):]

    
    
    
    test = bytes(text,'UTF-8')

    res = {'hashtaged':text}
    print("[bold green][INFO][/bold green] Reply successfully")
  
    return jsonify(res)






if __name__ == '__main__':
 
    try:
        print( "[bold green][INFO][/bold green] Starting...")

        assert("test" == hashtag("test"))
       

    except Exception as e:
        print("[bold red][ERROR][/bold red] SERIOUS API ERROR",e)

"""