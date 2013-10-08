
import logging

logger = logging.getLogger(__name__)

def dart_callback(tree):
    """ Tree is a ElementTree object. """

    tag_prefix = "{http://www.yale.edu/tp/cas}"

    findtext = lambda x: tree[0].findtext(tag_prefix + x)

    name = findtext('name')
    did = findtext('did')
    netid = findtext('netid')
    uid = findtext('uid')
    user = findtext('user')
    affil = findtext('affil')
    alumniid = findtext('alumniid')
    authtype = findtext('authType')
    
    
