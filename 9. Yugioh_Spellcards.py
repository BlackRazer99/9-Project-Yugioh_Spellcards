#klassen und objects #global vs locals #try and accept
#getting a general understanding on why classes are usefull using yugioh again
#in comparison to the last yugioh project, its easier to just have these different functions
#but I dont see the general efficiancy in classes with this example to just having one function
#considering that having to initialize everything before hand doesnt allow me to be flexible
#i.e I cannot ad a new parameter outside the init which makes it a worse function

class spell_cards(object):
    def __init__(self, name, effect, typ):
        self.name = name
        self.effect = effect
        self.typ = typ
        
    def show_card(self):
        print(self.name, self.typ, self.effect)

    #this woudln't work but it would be really helpfull if it would
    #def type_card(self, atk):
       # print(self.atk)


mystical_space_typhoon = spell_cards("Mystical space typhoon", "\ndestroy one spell and trap card", "quick")
heavy_storm = spell_cards("Heavy storm", "\ndestroy all spell and trap cards on the field", "normal")

mystical_space_typhoon.show_card()
heavy_storm.show_card()

