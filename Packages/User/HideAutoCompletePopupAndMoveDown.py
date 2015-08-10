import sublime, sublime_plugin

def move_down(self):
    self.window.run_command("move", {"by": "lines", "forward": True})

class HideAutoCompletePopupAndMoveDown(sublime_plugin.WindowCommand):
    def run(self):
        #print (self.window.settings().get('auto_complete_visible'))
        #if (move_second_time == False):
        #    print ("wtf")
        #self.window.run_command("hide_auto_complete")
            #self.set_timeout(move_down, 1000)
        move_down(self)
        #{ "key": "auto_complete_visible", "operator": "equal", "operand": true },