from login import Login

log=Login()
log.login()
unread_count=log.switch_to_addressee()
if unread_count is not 0:
    log.dowlond_attach(unread_count,u"简历")

log.quit()


