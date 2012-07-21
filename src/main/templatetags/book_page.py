# -*- coding: utf-8 -*-
import re
from types import NoneType
from django import template

register = template.Library()


@register.inclusion_tag('main/_toc.html')
def toc(page):
    return {
        'toc': prepare_toc(page.book.get_toc(), page.chapter, page.section)
    }


@register.inclusion_tag('main/_main_page_toc.html')
def main_page_toc(book):
    if book:
        chapters = prepare_toc(book.get_toc())['chapters']
    else:
        chapters = []
    return {
        'chapters': chapters
    }


def prepare_toc(toc, chapter=None, section=None):
    chapters = []
    sections = []
    for item in toc.get('chapters'):
        # для каждой главы получаем её номер, её секции и генерируем url
        r = re.match(r'^.*\.chap(?P<number>\d+)$', item[0])
        try:
            url = '/ch%s.html' % (r.group('number'),)
            chapters.append([url, item[1]])  # id and title
        except NoneType:
            pass  # пропускаем ошибочную главу

        if chapter:
            if chapter != 'ap' and chapter == r.group('number'):
                # если это глава и её номер совпадает с выбранной, то сохраняем список секций
                for s in item[2]:
                    index = item[2].index(s) + 1
                    if index == 1:
                        sections.append(('/ch%s.html#%s' % (chapter, s[0]), s[1]))
                    else:
                        sections.append(('/ch%ss%02i.html' % (chapter, index), s[1]))

    for item in toc.get('appendixes'):
        # для каждого приложения получаем его букву и генерируем url
        r = re.match(r'^.*\.appendix_(?P<letter>[a-z])$', item[0])
        try:
            url = '/ap%s.html' % (r.group('letter'),)
            chapters.append([url, item[1]])  # id and title
        except NoneType:
            pass  # пропускаем ошибочную главу
    return {'chapters': chapters, 'sections': sections, 'url': url, 'chapter_url': 'ch%s.html' % (chapter,)}
