from mycroft import MycroftSkill, intent_file_handler


class Meteoalert(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('meteoalert.intent')
    def handle_meteoalert(self, message):
        self.speak_dialog('meteoalert')


def create_skill():
    return Meteoalert()

