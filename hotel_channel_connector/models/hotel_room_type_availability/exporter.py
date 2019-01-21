# Copyright 2018-2019 Alexandre Díaz <dev@redneboa.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.addons.component.core import Component


class HotelRoomTypeAvailabilityExporter(Component):
    _name = 'channel.hotel.room.type.availability.exporter'
    _inherit = 'hotel.channel.exporter'
    _apply_on = ['channel.hotel.room.type.availability']
    _usage = 'hotel.room.type.availability.exporter'

    def push_availability(self):
        raise NotImplementedError
