class StarWars():
    """ The functions within this class have similar functionality. Each function takes the input string and is concatenated with the introduction list to complete a sentence by the various Star Wars characters below.

    Parameters
    -----------
    content : String
        String as input from the user.

    Return
    --------
    [uniquecharacter]Talks : String
        Concatenated String of elements from list1 and predefined words to create unique Star Wars character quotations.
    """

    def yodaTranslator(self, content):
        introduction = 'How are you feeling today'
        list1 = introduction.split()
        yodaTalks = (content + ' ' + list1[2] + ' must feel ' + list1[-1] + '. Hmmm - Jedi Baby Yoda')
        print(yodaTalks)
        return yodaTalks


    def chewbaccaTranslator(self, content):
        introduction = 'How are you feeling today'
        list1 = introduction.split()
        chewbaccaTalks = ('Rrraagrghhh! Wookiee ' + list1[3] + ' ' + content + '. - Chewbacca')
        print(chewbaccaTalks)
        return chewbaccaTalks


    def darthvaderTranslator(self, content):
        introduction = 'How are you feeling today'
        list1 = introduction.split()
        darthvaderTalks = ('You must feel ' + content + ' because I am your father. - Darth Vader')
        print(darthvaderTalks)
        return darthvaderTalks


    def robotTranslator(self, content):
        introduction = 'How are you feeling today'
        list1 = introduction.split()
        robotTalks = ('Beebop boobeep. My signals inform me that you are ' + list1[3] + ' ' + content + '. - R2D2')
        print(robotTalks)
        return robotTalks


    def pikachuTranslator(self, content):
        introduction = 'How are you feeling today'
        list1 = introduction.split()
        pikachuTalks = ('Pika pika ' + list1[3] + ' ' + content + '. - Pikachu')
        print(pikachuTalks)
        return pikachuTalks
