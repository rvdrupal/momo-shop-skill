from mycroft import MycroftSkill, intent_file_handler


class MomoShop(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('shop.momo.intent')
    def handle_shop_momo(self, message):
        flavour = message.data.get('flavour')

        self.speak_dialog('shop.momo', data={
            'flavour': flavour
        })


def create_skill():
    return MomoShop()

