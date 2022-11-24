import sys, os, json, requests, unidecode, asyncio
import asyncio
from importlib import resources
try:
    from rich import print
except Exception as e:
    print("[ERROR] no color print")


if __package__ != None:
	PATH = resources.path(__package__,'hashtag_list.json')
else:
	PATH = 'hashtag_list.json'




def update():
    print("update")
    result = requests.get( 
              "https://raw.githubusercontent.com/Qypol342/Hashtag/main/hashtag_list.json") 
    with open(PATH,'w') as reader:
        reader.write(result.text)
    


def log(text, debug=True):
	if debug:
		print(f"[bold green][INFO][/bold green]{text}")


def hashtag(text='',debug=False):

    log("Incoming request",debug)

    allow = [',','.',' ','!','?',"'",'"',":",";","(",")"]
    
    with open(PATH,'r') as reader:
 
        lib = json.loads(reader.read())
    

    log(len(lib), debug)
    for i, v in lib.items():

        if len(text) >= 280:
            log("[bold red][ERROR][/bold red] text to long to add hashtag",debug)
            break
        
        text_low = unidecode.unidecode(text).lower()
        
        
        if i in text_low :

            
            if text_low.index(i) == 0 or text[text_low.index(i)-1] != '#':

                if text_low.index(i) != 0:
                    log("cheking first char "+text[text_low.index(i)-1]+" in "+text[text_low.index(i)-1] not in allow,debug)


                if text_low.index(i) != 0 and text[text_low.index(i)-1] not in allow: 
                    """
                    arreter si le caractère devant fait pas parti de la liste autoriser
                    """
                    continue
                if text_low.index(i)+len(i)< len(text):

                    log("cheking last char "+text[text_low.index(i)+len(i)]+" in "+text[text_low.index(i)+len(i)] not in allow,debug)
                if text_low.index(i)+len(i)< len(text) and text[text_low.index(i)+len(i)] not in allow:
                    """
                    arreter si le caractère apres fait pas parti de la liste autoriser
                    """
                    continue


                else:
                    log("[bold green][INFO][/bold green] hashtag found : "+lib[i],debug)
                    inn = text_low.index(i)
                    
                    text = text[:inn] + lib[i] + text[inn + len(i):]

    
    
    
    #test = bytes(text,'UTF-8')
    log("Reply successfully",debug)

   
    return text






if __name__ == '__main__':
 
    
        print( "[bold green][INFO][/bold green] Starting...")
     	
        assert("test" == hashtag("test"))
        
        assert("#US" == hashtag("#US",debug=True))
       

    
