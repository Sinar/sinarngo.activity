from collective.grok import gs
from sinarngo.activity import MessageFactory as _

@gs.importstep(
    name=u'sinarngo.activity', 
    title=_('sinarngo.activity import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sinarngo.activity.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
