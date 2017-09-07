import re

from .models import Word, Verb

class VerbParser:
  MAP_VERB = {
    'al': {
      'Դերբայ': {
        'Անորոշ դերբայ': ['{}ալ'],
        'Ենթակայական դերբայ': ['{}ացող'],
        'Հարակատար դերբայ': ['{}ացած'],
        'Համակատար դերբայ':	['{}ալիս'],
        'Անկատար դերբայ': ['{}ում'],
        'Վաղակատար դերբայ': ['{}ացել'],
        'Ապակատար դերբայ': ['{}ալու'],
        'Ժխտական դերբայ': ['{}ա'],
      },
      'Սահմանական եղանակ': {
        'Անկատար ներկա':	['{}ում եմ',	'{}ում ես',	'{}ում է',	'{}ում ենք', '{}ում եք',	'{}ում են'],
        'Անկատար անցյալ': ['{}ում էի', '{}ում էիր', '{}ում էր', '{}ում էինք', '{}ում էիք', '{}ում էին'],
        'Ապակատար ներկա': ['{}ալու եմ', '{}ալու ես', '{}ալու է', '{}ալու ենք', '{}ալու եք', '{}ալու են'],
        'Ապակատար անցյալ': ['{}ալու էի', '{}ալու էիր', '{}ալու էր', '{}ալու էինք', '{}ալու էիք', '{}ալու էին'],
        'Վաղակատար ներկա': ['{}ացել եմ', '{}ացել ես', '{}ացել է', '{}ացել ենք', '{}ացել եք', '{}ացել են'],
        'Վաղակատար անցյալ': ['{}ացել էի', '{}ացել էիր', '{}ացել էր', '{}ացել էինք', '{}ացել էիք', '{}ացել էին'],
        'Անցյալ կատարյալ': ['{}ացի', '{}ացիր', '{}աց', '{}ացինք', '{}ացիք', '{}ացին'],
      },
      'Ըղձական եղանակ': {
        'Ապառնի': ['{}ամ', '{}աս', '{}ա', '{}անք', '{}աք', '{}ան'],
        'Անցյալի ապառնի': ['{}այի', '{}այիր', '{}ար', '{}այինք', '{}այիք', '{}ային'],
      },
      'Պայմանական եղանակ': {
        'Ապառնի': ['կ{}ամ', 'կ{}աս', 'կ{}ա', 'կ{}անք', 'կ{}աք', 'կ{}ան'],
        'Անցյալի ապառնի': ['կ{}այի', 'կ{}այիր', 'կ{}ար', 'կ{}այինք', 'կ{}այիք', 'կ{}ային'],
      },
      'Հարկադրական եղանակ': {
        'Ապառնի': ['պիտի {}ամ', 'պիտի {}աս', 'պիտի {}ա', 'պիտի {}անք', 'պիտի {}աք', 'պիտի {}ան'],
        'Անցյալի ապառնի': ['պիտի {}այի', 'պիտի {}այիր', 'պիտի {}ար', 'պիտի {}այինք', 'պիտի {}այիք', 'պիտի {}ային'],
      },
      'Հրամայական  եղանակ': {
        'Ապառնի': [	'{}ա՛', '{}ացե՛ք'],
      },
    },
    'el': {
      'Դերբայ': {
        'Անորոշ դերբայ': ['{}ել'],
        'Ենթակայական դերբայ': ['{}ող'],
        'Հարակատար դերբայ': ['{}ած'],
        'Համակատար դերբայ':	['{}ելիս'],
        'Անկատար դերբայ': ['{}ում'],
        'Վաղակատար դերբայ': ['{}ել'],
        'Ապակատար դերբայ': ['{}ելու'],
        'Ժխտական դերբայ': ['{}ի'],
      },
      'Սահմանական եղանակ': {
        'Անկատար ներկա':	['{}ում եմ',	'{}ում ես',	'{}ում է',	'{}ում ենք', '{}ում եք',	'{}ում են'],
        'Անկատար անցյալ': ['{}ում էի', '{}ում էիր', '{}ում էր', '{}ում էինք', '{}ում էիք', '{}ում էին'],
        'Ապակատար ներկա': ['{}ելու եմ', '{}ելու ես', '{}ելու է', '{}ելու ենք', '{}ելու եք', '{}ելու են'],
        'Ապակատար անցյալ': ['{}ելու էի', '{}ելու էիր', '{}ելու էր', '{}ելու էինք', '{}ելու էիք', '{}ելու էին'],
        'Վաղակատար ներկա': ['{}ել եմ', '{}ել ես', '{}ել է', '{}ել ենք', '{}ել եք', '{}ել են'],
        'Վաղակատար անցյալ': ['{}ել էի', '{}ել էիր', '{}ել էր', '{}ել էինք', '{}ել էիք', '{}ել էին'],
        'Անցյալ կատարյալ': ['{}եցի', '{}եցիր', '{}եց', '{}եցինք', '{}եցիք', '{}եցին'],
      },
      'Ըղձական եղանակ': {
        'Ապառնի': ['{}եմ', '{}ես', '{}ի', '{}ենք', '{}եք', '{}են'],
        'Անցյալի ապառնի': ['{}եի', '{}եիր', '{}եր', '{}եինք', '{}եիք', '{}եին'],
      },
      'Պայմանական եղանակ': {
        'Ապառնի': ['կ{}եմ', 'կ{}ես', 'կ{}ի', 'կ{}ենք', 'կ{}եք', 'կ{}են'],
        'Անցյալի ապառնի': ['կ{}եի', 'կ{}եիր', 'կ{}եր', 'կ{}եինք', 'կ{}եիք', 'կ{}եին'],
      },
      'Հարկադրական եղանակ': {
        'Ապառնի': ['պիտի {}եմ', 'պիտի {}ես', 'պիտի {}ի', 'պիտի {}ենք', 'պիտի {}եք', 'պիտի {}են'],
        'Անցյալի ապառնի': ['պիտի {}եի', 'պիտի {}եիր', 'պիտի {}եր', 'պիտի {}եինք', 'պիտի {}եիք', 'պիտի {}եին'],
      },
      'Հրամայական  եղանակ': {
        'Ապառնի': [	'{}ի՛ր', '{}ե՛ք'],
      },
    },
    'նալ': {
      'Դերբայ': {
        'Անորոշ դերբայ': ['{}նալ'],
        'Ենթակայական դերբայ': ['{}ցող'],
        'Հարակատար դերբայ': ['{}ցած'],
        'Համակատար դերբայ':	['{}նալիս'],
        'Անկատար դերբայ': ['{}նում'],
        'Վաղակատար դերբայ': ['{}ցել'],
        'Ապակատար դերբայ': ['{}նալու'],
        'Ժխտական դերբայ': ['{}նա'],
      },
      'Սահմանական եղանակ': {
        'Անկատար ներկա':	['{}նում եմ',	'{}նում ես',	'{}նում է',	'{}նում ենք', '{}նում եք',	'{}նում են'],
        'Անկատար անցյալ': ['{}նում էի', '{}նում էիր', '{}նում էր', '{}նում էինք', '{}նում էիք', '{}նում էին'],
        'Ապակատար ներկա': ['{}նալու եմ', '{}նալու ես', '{}նալու է', '{}նալու ենք', '{}նալու եք', '{}նալու են'],
        'Ապակատար անցյալ': ['{}նալու էի', '{}նալու էիր', '{}նալու էր', '{}նալու էինք', '{}նալու էիք', '{}նալու էին'],
        'Վաղակատար ներկա': ['{}ցել եմ', '{}ցել ես', '{}ցել է', '{}ցել ենք', '{}ցել եք', '{}ցել են'],
        'Վաղակատար անցյալ': ['{}ցել էի', '{}ցել էիր', '{}ցել էր', '{}ցել էինք', '{}ցել էիք', '{}ցել էին'],
        'Անցյալ կատարյալ': ['{}ցա', '{}ցար', '{}ցավ', '{}ցանք', '{}ցաք', '{}ցան'],
      },
      'Ըղձական եղանակ': {
        'Ապառնի': ['{}նամ', '{}նաս', '{}նա', '{}նանք', '{}նաք', '{}նան'],
        'Անցյալի ապառնի': ['{}նայի', '{}նայիր', '{}նար', '{}նայինք', '{}նայիք', '{}նային'],
      },
      'Պայմանական եղանակ': {
        'Ապառնի': ['կ{}նամ', 'կ{}նաս', 'կ{}նա', 'կ{}նանք', 'կ{}նաք', 'կ{}նան'],
        'Անցյալի ապառնի': ['կ{}նայի', 'կ{}նայիր', 'կ{}նար', 'կ{}նայինք', 'կ{}նայիք', 'կ{}նային'],
      },
      'Հարկադրական եղանակ': {
        'Ապառնի': ['պիտի {}նամ', 'պիտի {}նաս', 'պիտի {}նա', 'պիտի {}նանք', 'պիտի {}նաք', 'պիտի {}նան'],
        'Անցյալի ապառնի': ['պիտի {}նայի', 'պիտի {}նայիր', 'պիտի {}նար', 'պիտի {}նայինք', 'պիտի {}նայիք', 'պիտի {}նային'],
      },
      'Հրամայական  եղանակ': {
        'Ապառնի': [	'{}ցի՛ր', '{}ցե՛ք'],
      },
    },
    'ցնել': {
      'Դերբայ': {
        'Անորոշ դերբայ': ['{}նել'],
        'Ենթակայական դերբայ': ['{}նող'],
        'Հարակատար դերբայ': ['{}րած'],
        'Համակատար դերբայ':	['{}նելիս'],
        'Անկատար դերբայ': ['{}նում'],
        'Վաղակատար դերբայ': ['{}րել'],
        'Ապակատար դերբայ': ['{}նելու'],
        'Ժխտական դերբայ': ['{}նի'],
      },
      'Սահմանական եղանակ': {
        'Անկատար ներկա':	['{}նում եմ',	'{}նում ես',	'{}նում է',	'{}նում ենք', '{}նում եք',	'{}նում են'],
        'Անկատար անցյալ': ['{}նում էի', '{}նում էիր', '{}նում էր', '{}նում էինք', '{}նում էիք', '{}նում էին'],
        'Ապակատար ներկա': ['{}նելու եմ', '{}նելու ես', '{}նելու է', '{}նելու ենք', '{}նելու եք', '{}նելու են'],
        'Ապակատար անցյալ': ['{}նելու էի', '{}նելու էիր', '{}նելու էր', '{}նելու էինք', '{}նելու էիք', '{}նելու էին'],
        'Վաղակատար ներկա': ['{}րել եմ', '{}րել ես', '{}րել է', '{}րել ենք', '{}րել եք', '{}րել են'],
        'Վաղակատար անցյալ': ['{}րել էի', '{}րել էիր', '{}րել էր', '{}րել էինք', '{}րել էիք', '{}րել էին'],
        'Անցյալ կատարյալ': ['{}րի', '{}րիր', '{}րեց', '{}րինք', '{}րիք', '{}րին'],
      },
      'Ըղձական եղանակ': {
        'Ապառնի': ['{}նեմ', '{}նես', '{}նի', '{}նենք', '{}նեք', '{}նեն'],
        'Անցյալի ապառնի': ['{}նեի', '{}նեիր', '{}ներ', '{}նեինք', '{}նեիք', '{}նեին'],
      },
      'Պայմանական եղանակ': {
        'Ապառնի': ['կ{}նեմ', 'կ{}նես', 'կ{}նի', 'կ{}նենք', 'կ{}նեք', 'կ{}նեն'],
        'Անցյալի ապառնի': ['կ{}նեի', 'կ{}նեիր', 'կ{}ներ', 'կ{}նեինք', 'կ{}նեիք', 'կ{}նեին'],
      },
      'Հարկադրական եղանակ': {
        'Ապառնի': ['պիտի {}նեմ', 'պիտի {}նես', 'պիտի {}նի', 'պիտի {}նենք', 'պիտի {}նեք', 'պիտի {}նեն'],
        'Անցյալի ապառնի': ['պիտի {}նեի', 'պիտի {}նեիր', 'պիտի {}ներ', 'պիտի {}նեինք', 'պիտի {}նեիք', 'պիտի {}նեին'],
      },
      'Հրամայական  եղանակ': {
        'Ապառնի': [	'{}րու՛', '{}րե՛ք'],
      },
    },
  }

  def __init__(self, tpl, word):
    self.tpl = tpl
    self.word = word
  
  def parse(self):
    attr = self.tpl.split('.')
    arr = []
    
    if len(attr) == 3:
      if '|' in attr[-1]:
        conj = attr[-1].split('|')[0]
        root = attr[-1].split('|')[-1]
        
        m_conj = self.MAP_VERB.get(conj)
        if m_conj:
          for i in m_conj:
            l = 0
            lemma = False
            form = i
            for j in m_conj[i]:
              type = j
              for k in range(len(m_conj[i][j])):
                c = m_conj[i][j][k]
                if len(m_conj[i][j]) == 6:
                  demq = k%3 + 1
                elif len(m_conj[i][j]) == 2:
                  demq = 2
                else:
                  demq = ''
                wrd = Word()
                wrd.pos = 'verb'
                wrd.word = c.format(root)
                if l == 1:
                  wrd.lemma = lemma
                wrd.save()
                verb = Verb()
                verb.parent = wrd
                verb.root = root
                verb.type = form
                verb.form = type
                verb.quantity = int(k / (len(m_conj[i][j]) / 2) ) + 1 if len(m_conj[i][j]) > 1 else ''
                verb.demq = demq
                verb.ending = conj
                verb.save()
                if l == 0:
                  lemma = wrd
                  l = 1