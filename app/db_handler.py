from app import app
from app.models import Translate
from app import db
import logging

DEFAULT_LANG = app.config['DEFAULT_LANG']

logger = logging.getLogger('DataBaseHandler')


def import_translate(data):
    logger.info('Start import translate to database')

    lang: str = data[0].get('lang')
    plugins: dict = data[0].get('plugins')
    plugin_rows = []

    try:
        for plugin in plugins:
            plugin_row = {'synopsis': plugin.get(f'synopsis_{lang}'), 'description': plugin.get(f'description_{lang}'),
                          'pluginName': plugin.get('plugin_name'), 'plugin_id': plugin.get('id'),
                          'solution': plugin.get('solution'),
                          'plugin_modification_date': plugin.get('plugin_modification_date', ''), 'language': lang}
            plugin_rows.append(plugin_row)
        queries = [Translate(**row) for row in plugin_rows]
        db.session.add_all(queries)
    except Exception as e:
        print(e)
        db.session.rollback()
        return False
    else:
        db.session.commit()
    return True


def get_translate_by_plugin(plugin_id: int, lang=DEFAULT_LANG):
    translate = Translate.query.filter_by(plugin_id=plugin_id, language=lang).first()
    return translate
