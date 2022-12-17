from View.base_screen import BaseScreenView


class MainScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def enter(self):
        # import pdb
        # pdb.set_trace()
        # self.manager_screens.current='mainapp screen'
        pass