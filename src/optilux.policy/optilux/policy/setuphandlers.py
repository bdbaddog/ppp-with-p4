from Products.CMFCore.utils import getToolByName

def loadRichDocument(portal):
    qi = getToolByName(portal, 'portal_quickinstaller')
    if not qi.isProductInstalled('Products.RichDocument'):
        qi.installProduct('Products.RichDocument')
 

def setupGroups(portal):
    acl_users=getToolByName(portal,'acl_users')
    if not acl_users.searchGroups(name='Staff'):
        gtool=getToolByName(portal,'portal_groups')
        gtool.addGroup('Staff',roles=['StaffMember'])


def renameRichDocument(portal):
    portal_types = getToolByName(portal,'portal_types')
    rich_document_fti = getattr(portal_types,'RichDocument')
    rich_document_fti.title = "Web Page"

def disableDocument(portal):
    portal_types = getToolByName(portal,'portal_types')
    document_fti = getattr(portal_types,'Document')
    document_fti.global_allow = False




def importVarious(context):
    """Miscellaneous steps import handler
    """
    if context.readDataFile('optilux.policy_various.txt') is None:
        return


    portal = context.getSite()
    loadRichDocument(portal)
    setupGroups(portal)
    renameRichDocument(portal)
    disableDocument(portal)
