from app import app
import logging

logger = logging.getLogger('nest')
logger.info('App started')
app.run(host='127.0.0.1', port=5000, debug=False)
