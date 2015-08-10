import sublime, sublime_plugin

class RecolorOnSave(sublime_plugin.EventListener):

    def on_post_save(self, view):

        should_recolor = view.settings().get('recolor_on_save')

        if should_recolor == 1:
            view.window().run_command('auto_recolorer')
