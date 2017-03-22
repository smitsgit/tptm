import pyramid_handlers
from Blue_Yellow.controllers.base_controller import BaseController
from Blue_Yellow.services.album_service import AlbumService


class AlbumController(BaseController):
    @pyramid_handlers.action(renderer="templates/albums/index.pt")
    def index(self):
        albums_data = AlbumService.get_albums()
        return {'albums': albums_data}
