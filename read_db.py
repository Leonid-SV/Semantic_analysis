# -*- coding: utf-8 -*-
# from webapp_f import create_app
from webapp.forms import db, ModelPosts, ModelComments, ModelTags
import re
from pprint import pprint

# app = create_app()
# from flask import current_app as app # вариант импорта app из запущенного instant

def text_clean(text):
    #''' функция очистки текста. Может принимать как текст, так и списко из текстовых значений '''

    # паттерны для очистки текста от ссылок и лишникх символов, переносов, скобок
    pattern_1 = re.compile(r'\bhttp\S*\b[,!?]*')
    pattern_2 = re.compile(r'[+=#$%(\n)\]\[]')
    patterns = [pattern_1, pattern_2]

    try:
        if type(text) == list:
            # try:
            for i in range(len(text)):
                for p in patterns:
                    text[i] = (re.sub(p, '', text[i]))
        else:
            for p in patterns:
                text = (re.sub(p, '', text))

        print(text)
        return text

    except:
        print('Input Error')
        return 'Error'


def get_data(inp):
    # функция извлечения данных из базы данных postgresql посредством Фласк-алхимии (SQLAlchemy)
    
    inputs = inp.split()

    result = []

    for inp in inputs:
        # добываем тэги по запросу из базы тэгов
        tags = db.session.query(ModelTags.tagname).filter(ModelTags.tagname.like(inp + '%')).all()
        tags_by_inp = [tag[0] for tag in tags]
        # добываем ID постов, соответствующие тэгам из базы постов
        postid = db.session.query(ModelPosts.id).filter(ModelPosts.tags.like('%<'+tags_by_inp[0]+'>%')).all()
        id_by_tags = [int(p_id[0]) for p_id in postid]
        # добываем комментарии по ID постов из базы комментариев
        comments = db.session.query(ModelComments.text).filter(ModelComments.postid.in_(id_by_tags)).all()

        comments_by_id = [text_clean(c[0]) for c in comments]

        # печать данных для отладки
        # print(tags_by_inp[0])
        # print('+' * 50)
        # pprint(tags_by_inp)
        # print('+' * 50)
        # pprint(id_by_tags)
        # print('+' * 50)
        # print(comments_by_id) # some p

        result.extend(comments_by_id)

    # print(result)

    return result

# with app.app_context():
#     get_data('pytho ruby', db)

# some_text = ['Realtime image processing using PyPy:http://morepypy.cessing-in-python.html hi there',
#              'Realtime image processing using PyPy:http://morepypy.blogsphtml, hi there',
#              'Realtime image processing using PyPy:http://morepypy.cessing-in-python.html hi there',
#              'Realtime image processing using PyPy:http://morepypy.blogsphtml, hi there'
#              ]
#
#
# # p = re.compile(r'\bhttp\S*\b[,!?]*')
#
# print('+'*100)
# print(text_clean('''Python is good http:\\someshit here is += all GooD''' ))