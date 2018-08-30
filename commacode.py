def commaToAdd(list_name):
    spamString="'"
    if len(list_name) == 1:
        #print(str(list_name)) This prints ['apples']
        print(spamString + list_name[0] + spamString)
    else:
        for i in range(len(list_name)-2):
            spamString = spamString + list_name[i] + ', '
        spamString = spamString + list_name[-2] + ' and ' + list_name[-1]  + "'"
        #list_name = spamString You dont need this as you have already built spamString
        #print(list_name)
        print(spamString)

spam = ['apples']
commaToAdd(spam)
# 'apples'

spam2 = ['apples', 'oranges']
commaToAdd(spam2)
#'apples and oranges'

spam3 = ['apples', 'oranges', 'bananas', 'tofu', 'cat']
commaToAdd(spam3)
#'apples, oranges, bananas, tofu and cat'