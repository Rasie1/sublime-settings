import sublime, sublime_plugin, os
 
#requires trimmer plugin
class OnSaveActions(sublime_plugin.EventListener):
 
  def on_post_save(self, view):
 
    #let's see if project wants to be autobuilt.
    should_trim = view.settings().get('trim_space_on_save')
    if should_trim == 1:
      view.window().run_command('trimmer')
