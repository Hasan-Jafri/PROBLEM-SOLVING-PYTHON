conversion_length = {
    'millimeter': 0.001,
    'centimeter': 0.01,
    'decimeter': 0.1,
    'meter': 1,
    'kilometer': 1000,
    'inch': 0.0254,
    'inche':0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.34,
}

conversion_weight = {
    'gram': 1,
    'kilogram': 1000,
    'tonne': 1000000,
    'ounce': 0.03527396,
    'pound': 0.00220462,
    'short ton': 0.000984207,
    'long ton': 0.000892857,
}

conversion_volume = {
    'cubic centimeter': 0.001,
    'liter': 1,
    'cubic meter': 1000,
    'fluid ounce': 0.0295735,
    'cup': 0.236588,
    'pint': 0.473176,
    'quart': 0.946353,
    'gallon': 3.78541,
    'cubic inch': 0.0163871,
    'cubic foot': 28.3168,
    'cubic yard': 764.555,
}

length = {

    'meter':{
        'inche': 39.3701 ,
        'inch': 39.3701 ,
        'feet':3.28084,
        'yard':1.09361,
        'mile':0.000621371,
    }
}
weight = {
    
    'gram':{
    'ounce':0.03527396,
    'pound':0.00220462
    }

}
volume = {

    'liter':{
    'quart':1.05668821,
    'cubic feet':0.035,
    'cubic yard':0.0000037,
    'gallon':0.264172
    }

}


def calculate_answer(string):
    string = string.strip().split()


    english = string[2]
    english = english.rstrip('s')
    amount = float(string[len(string)-2])
    metric = string[len(string)-1]
    metric = metric.rstrip('?')
    metric = metric.rstrip('s')

    answer = float(0)
    conversion = float(0)

    if(metric in conversion_length):
        conversion = float(amount*conversion_length[metric])
        if(english in length['meter']):
            answer = float((conversion*length['meter'][english])/conversion_length[metric])
        else:
            answer = -1
    elif(metric in conversion_weight):
        conversion = float(amount*conversion_weight[metric])
        if(english in weight['gram']):
            answer = float((conversion*weight['gram'][english])/conversion_weight[metric])
        else:
            answer = -1
    elif(metric in conversion_volume):
        conversion = float(amount*conversion_volume[metric])
        if(english in volume['liter']):
            answer = float((conversion*volume['liter'][english])/conversion_volume[metric])
        else:
            answer = -1
    else:
        answer = -1

    return answer

n = int(input())
result = []
for i in range(n):

    string = str(input())
    answer = calculate_answer(string=string)
    if(int(answer) == -1):
        result.append(-1)
    else:
        result.append(answer)
        
    

for i in result:
    print(i)






