from app import app
from flask import jsonify, request, make_response, abort
from app import db_handler
import logging

logger = logging.getLogger('nest.app.endpoints')


@app.get('/')
def index():
    return jsonify({'restapi': 'True'})


@app.get('/getPlugin')
def get_plugin():

    plugin_id = request.args.get('plugin_id')
    lang = request.args.get('lang')
    # TODO: make param validation
    logger.info('Get plugin %s', plugin_id)
    result = {
        'plugin_id': '',
        'pluginName': '',
        'solution': '',
        'synopsis': '',
        'description': '',
        'language': '',
        'plugin_modification_date': ''
    }
    if plugin_id is not None:
        plugin = db_handler.get_translate_by_plugin(plugin_id=int(plugin_id), lang=lang)
        if plugin is not None:
            result['plugin_id'] = plugin.plugin_id
            result['pluginName'] = plugin.pluginName
            result['solution'] = plugin.solution
            result['synopsis'] = plugin.synopsis
            result['description'] = plugin.description
            result['language'] = plugin.language
            result['plugin_modification_date'] = plugin.plugin_modification_date

        return jsonify(result)
    else:
        logger.error('Try to get plugin')
        abort(500, description='Have to set a parameter: plugin_id')


@app.post('/updatePlugin')
def update_plugin():
    logger.info('updatePlugin')
    return jsonify({'status': 'access', 'text': 'updatePlugin'})


@app.route('/import', methods=['GET', 'POST'])
def import_translate():
    json_data = request.get_json()
    logger.info('Import translate')
    if json_data:
        result = db_handler.import_translate(json_data)
        if result:
            return make_response(jsonify({'status': 'access', 'code': 200, 'text': 'Import has done'}), 200)
        else:
            abort(500, description='Import has stopped')
    else:
        abort(400, description='JSON is bad')


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'status': 'error', 'code': error.code, 'text': error.description}), 404)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'status': 'error', 'code': error.code, 'text': error.description}), 404)


@app.errorhandler(500)
def internal_server_error(error):
    return make_response(jsonify({'status': 'error', 'code': error.code, 'text': error.description}), 500)
