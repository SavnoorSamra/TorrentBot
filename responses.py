from random import choice, randint

def getResponse(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you are silent'
    elif 'hello' in lowered:
        return 'Hello World!'
    #raise NotImplementedError('Code is missing!')
