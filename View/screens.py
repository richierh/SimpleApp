# The screen's dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController
# from Model.mainapp_screen import MainappScreenModel
# from Controller.mainapp_screen import MainappScreenController

screens = {
    'main screen': {
        'model': MainScreenModel,
        'controller': MainScreenController,
    },
#     'mainapp screen': {
#         'model': MainappScreenModel,
#         'controller': MainappScreenController,
#     },
}