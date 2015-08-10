import sublime, sublime_plugin, os

class SwitchPairedMode(sublime_plugin.WindowCommand):
    def run(self):
        s = sublime.load_settings("Preferences.sublime-settings")
        current = s.get("paired_mode_enabled", 10)
        current = not current
        s.set("paired_mode_enabled", current)

        sublime.save_settings("Preferences.sublime-settings")

def lol(self):
    print ("tst")

class OpenPairInAnotherPanel(sublime_plugin.TextCommand):
    def run(self, srt):
        if (not self.view.settings().get("paired_mode_enabled")):
            return
        filename = self.view.file_name()
        if (filename[-2:] == ".h"):
            filename = filename.replace(".h", ".cpp")
        else:
            if (filename[-4:] == ".cpp"):
                filename = filename.replace(".cpp", ".h")
            else:
                return
        if (not os.path.isfile(filename)):
            return
        window = sublime.windows()[0]
        if (window.num_groups() == 2):
            prevGroup = window.active_group()
            i = 0
            if (i == prevGroup):
                i = 1
            window.focus_group(i)
            window.open_file(filename)
            window.focus_group(prevGroup)

class OnNextViewInStack(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("next_view_in_stack")
        self.window.run_command("open_pair_in_another_panel")

class OnPrevViewInStack(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("prev_view_in_stack")
        self.window.run_command("open_pair_in_another_panel")

class OnPrevView(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("prev_view")
        self.window.run_command("open_pair_in_another_panel")

class OnNextView(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("next_view")
        self.window.run_command("open_pair_in_another_panel")
