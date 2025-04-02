import os
import subprocess
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ResultItem import ResultItem


# Main extension class
class TerminatorExtension(Extension):
    def __init__(self):
        super().__init__()
        # Subscribe to events
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener)
        self.subscribe(ItemEnterEvent, ItemEnterEventListener)


# Listener for keyword query events
class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        # Get the folder path from the user's query
        query = event.get_argument() or ""
        base_path = os.path.expanduser(query) if query else os.getcwd()

        # List matching directories
        suggestions = []
        if os.path.isdir(base_path):
            for item in os.listdir(base_path):
                item_path = os.path.join(base_path, item)
                if os.path.isdir(item_path):
                    suggestions.append(
                        ResultItem(
                            title=item,
                            subtitle=f"Open Terminator in {item_path}",
                            on_enter=ItemEnterEvent(item_path),
                        )
                    )
        return suggestions


# Listener for item enter events
class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        # Get the folder path from the event data
        folder_path = event.get_data()
        if os.path.isdir(folder_path):
            # Open Terminator in the specified folder
            subprocess.Popen(
              ["terminator", "--working-directory", folder_path]
            )
        else:
            # Notify the user if the folder is invalid
            subprocess.Popen(
              [
                "notify-send",
                "Invalid folder",
                f"The folder '{folder_path}' does not exist.",
              ],
            )


# Entry point for the extension
if __name__ == "__main__":
    TerminatorExtension().run()
