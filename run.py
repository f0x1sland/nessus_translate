from app import app
import logging

logger = logging.getLogger('nest')
logger.info('App started')
app.run(host='0.0.0.0', port=5000, debug=False)
