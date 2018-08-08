morse_decode = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '...---...': 'SOS'}



def decode_morse(input_str):


    # >>>> show me the code <<<<
    
    output_str=input_str.lstrip()
    output_str=output_str.rstrip()
    print(output_str)
    output_lst=output_str.split(' ')
    print(output_lst)
    outcome_lst=[]
    for i in output_lst:
        if i == '':
            outcome_lst.append(' ')
        else:
            outcome_lst.append(morse_decode[i])
            
    print(outcome_lst)
    outcome_str=''.join(outcome_lst)
    print(outcome_str)
    outcome_str=outcome_str.strip()
    outcome_str=outcome_str.lstrip()
    outcome_str=outcome_str.rstrip()
    return outcome_str

    # >>>> show me the code <<<<

print(decode_morse('      - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --.      '))