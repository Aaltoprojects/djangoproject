import pages.constants as constants
from pages.models import Filter
from pages.scripts.parse_util import format_qset

def get_filters():
        f1 = format_qset(Filter.filter_db.filter(category='Rakennustyyppi'))
        f2 = format_qset(Filter.filter_db.filter(category='Rakennusmateriaali'))
        f3 = format_qset(Filter.filter_db.filter(category='Palvelu'))
        f4 = format_qset(Filter.filter_db.filter(category='Rakennustoimenpide'))
        f5 = format_qset(Filter.filter_db.filter(category='Rakenneosa'))
        return f1,f2,f3,f4,f5