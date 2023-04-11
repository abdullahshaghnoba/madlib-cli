import re

def read_template(path):
       if path!= "madlib_cli/assets/dark_and_stormy_night_template.txt" :
        if path != "madlib_cli/assets/output.txt":
         raise FileNotFoundError("Error : path is not correct")
       

    #    path1 = "madlib_cli/{p}"
    #    new_path=path1.format(p = path)
       with open(path) as file:
         opened_file =file.read()
         return(opened_file.strip())  
                 

def parse_template(str):
    
    result = re.findall(r'\{([^{}]+)\}', str)
    print(result)
    x = ()
    for item in result:    
     y = list(x)
     y.append( item)
     x = tuple(y)
     str = re.sub(r'\{([^{}]+)\}', '{}', str) 
    return str,x


def merge(str,tuple):
    y = list(tuple)
    txt = str.format(*y)
    return txt


if __name__ == "__main__":
    print("welcom to our game, play by entering what you are asked ;)")
    
    template = read_template("madlib_cli/assets/output.txt")
    stripped_template, parts = parse_template(template)

    user_inputs = []
    for part in parts:
        user_inputs.append(input(f"Enter a {part}: "))
    x = ()
    for item in user_inputs:    
     y = list(x)
     y.append( item)
     x = tuple(y)
    text = merge(stripped_template, x)
    print(text)
    with open("madlib_cli/assets/text.txt", "w") as file:
        opened_file =file.write(text)
