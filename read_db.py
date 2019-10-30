# from webapp_f import create_app
from webapp.forms import ModelPosts, ModelComments, ModelTags
# from pprint import pprint
#
# app = create_app()

def texts_loundary(text):
    import re
    try:
        pattern_1 = re.compile('http://\S*[\s, ]')
        pattern_2 = re.compile('[@"\[\]<>$#\n]')

        patterns = [pattern_1, pattern_2]
        for pattern in patterns:
            text = re.sub(pattern, ' ', text)

        return text

    except TypeError:
        return 'Error'

def get_data(inp, db):

    inputs = inp.split()

    result = []

    for inp in inputs:
        tags = db.session.query(ModelTags.tagname).filter(ModelTags.tagname.like(inp + '%')).all()
        tags_by_inp = [tag[0] for tag in tags]
        postid = db.session.query(ModelPosts.id).filter(ModelPosts.tags.like('%<'+tags_by_inp[0]+'>%')).limit(100).all()
        id_by_tags = [int(p_id[0]) for p_id in postid]
        comments = db.session.query(ModelComments.text).filter(ModelComments.postid.in_(id_by_tags)).all()

        comments_by_id = [texts_loundary(c[0]) for c in comments]

        # some prints

        # print(tags_by_inp[0])
        # print('+' * 50)
        # pprint(tags_by_inp)
        # print('+' * 50)
        # pprint(id_by_tags)
        # print('+' * 50)
        # print(comments_by_id) # some p

        result.extend(comments_by_id)

    print(result)

    return result
#
# with app.app_context():
#     get_data('pytho ruby', db)