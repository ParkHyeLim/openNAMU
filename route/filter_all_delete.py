from .tool.func import *

def filter_all_delete(tool, name = 'Test'):
    with get_db_connect() as conn:
        curs = conn.cursor()
        
        if admin_check(None, 'del_' + tool) != 1:
            return re_error('/error/3')

        if tool == 'inter_wiki':
            curs.execute(db_change("delete from html_filter where html = ? and kind = 'inter_wiki'"), [name])
        elif tool == 'edit_filter':
            curs.execute(db_change("delete from html_filter where html = ? and kind = 'regex_filter'"), [name])
        elif tool == 'name_filter':
            curs.execute(db_change("delete from html_filter where html = ? and kind = 'name'"), [name])
        elif tool == 'file_filter':
            curs.execute(db_change("delete from html_filter where html = ? and kind = 'file'"), [name])
        elif tool == 'email_filter':
            curs.execute(db_change("delete from html_filter where html = ? and kind = 'email'"), [name])
        elif tool == 'image_license':
            curs.execute(db_change("delete from html_filter where html = ? and kind = 'image_license'"), [name])
        elif tool == 'extension_filter':
            curs.execute(db_change("delete from html_filter where html = ? and kind = 'extension'"), [name])
        elif tool == 'document':
            curs.execute(db_change("delete from html_filter where html = ? and kind = 'document'"), [name])
        else:
            curs.execute(db_change("delete from html_filter where html = ? and kind = 'edit_top'"), [name])

        conn.commit()

        return redirect('/filter/' + tool)