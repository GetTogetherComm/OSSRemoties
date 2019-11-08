# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1573230512.2931592
_enable_loop = True
_template_filename = '/snap/nikola/1610/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper_isso.tmpl'
_template_uri = 'comments_helper_isso.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link_script', 'comment_link']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        isso_config = context.get('isso_config', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id:
            __M_writer('        <div data-title="')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('" id="isso-thread"></div>\n        <script src="')
            __M_writer(str(comment_system_id))
            __M_writer('js/embed.min.js" data-isso="')
            __M_writer(str(comment_system_id))
            __M_writer('" data-isso-lang="')
            __M_writer(str(lang))
            __M_writer('"\n')
            if isso_config:
                for k, v in isso_config.items():
                    __M_writer('        data-isso-')
                    __M_writer(str(k))
                    __M_writer('="')
                    __M_writer(str(v))
                    __M_writer('"\n')
            __M_writer('        ></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        pagekind = context.get('pagekind', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id and 'index' in pagekind:
            __M_writer('        <script src="')
            __M_writer(str(comment_system_id))
            __M_writer('js/count.min.js" data-isso="')
            __M_writer(str(comment_system_id))
            __M_writer('" data-isso-lang="')
            __M_writer(str(lang))
            __M_writer('"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id:
            __M_writer('        <a href="')
            __M_writer(str(link))
            __M_writer('#isso-thread">')
            __M_writer(str(messages("Comments")))
            __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "comments_helper_isso.tmpl", "line_map": {"67": 22, "68": 23, "69": 24, "70": 24, "71": 24, "72": 24, "73": 24, "74": 24, "75": 24, "16": 0, "81": 15, "93": 17, "21": 13, "22": 19, "23": 26, "88": 16, "89": 17, "90": 17, "91": 17, "92": 17, "29": 2, "99": 93, "36": 2, "37": 3, "38": 4, "39": 4, "40": 4, "41": 5, "42": 5, "43": 5, "44": 5, "45": 5, "46": 5, "47": 6, "48": 7, "49": 8, "50": 8, "51": 8, "52": 8, "53": 8, "54": 11, "87": 15, "60": 22}, "source_encoding": "utf-8", "filename": "/snap/nikola/1610/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper_isso.tmpl"}
__M_END_METADATA
"""