import re

class Punctuation:
  
  LINEAR_PUNCTUATION = {
    '0l': ('՚','\u055A',''),
    '1l': ('՛','\u055B',''),
    '2l': ('՜','\u055C','~'),
    '3l': ('՞','\u055E',''),
    '4l': ('՟','\u055F',''),
  }

  PUNCTUATION = {
    ':': ('։','\u0589',':'),
    4: ('\.\.\.\.','',''),
    3: ('\.\.\.','',''),
    'dot': ('.','\u002E','\.'),
    'comma': (',','\u002C',','),
    '`': ('՝','\u055D','`'),
    0: ('֊','\u058A',''),
    1: ('«','',''),
    2: ('»','',''),
    5: ('—','','_'),
    6: ('֊','','\-'),
    7: ('~','',''),
    8: ('”','',''),
    9: ('֏','\u058F',''),
    10: ('\(','',''),
    11: ('\)','',''),
    12: ('\{','',''),
    13: ('\}','',''),
    14: ('\[','',''),
    15: ('\]','',''),
    16: ('\/','',''),
  }
    
  INTERNATIONAL = [ '+', '-', '%', '°С', '$', '€', '₩', '¥', '₦', '₽', '£' ]
  METRIC = [ 'կմ', 'մ', 'ժ', 'վ', 'ր', 'կգ', 'գ', 'տ' ]
    
  def __init__(self, punct):
    if punct:
      if not isinstance(punct, list):
        self.punct = [punct]
      else:
        self.punct = punct
    else:
        raise KeyError('Please write punctuation symbol.')
  
  def regex(self):
    reg_arr = []
    if self.punct:
      for p in self.punct:
        if p in self.LINEAR_PUNCTUATION:
          reg_arr += [i for i in self.LINEAR_PUNCTUATION[p] if i]
        elif p in self.PUNCTUATION:
          reg_arr += [i for i in self.PUNCTUATION[p] if i]
    else:
      return ''
    return u'|'.join(reg_arr)

  @classmethod
  def all(cls, linear=False):
    reg_arr = []
    for i in (cls.PUNCTUATION.values() if linear == False else cls.LINEAR_PUNCTUATION.values()):
        for j in i:
            if j:
              reg_arr.append(j)
    return u'|'.join( reg_arr )

  @classmethod
  def inter(cls):
    return u'|'.join( cls.INTERNATIONAL )

  @classmethod
  def metric(cls, double):
    if double:
      return u'|'.join(['{}/{}'.format(i,j) for i in cls.METRIC for j in cls.METRIC])
    else:
      return u'|'.join(cls.METRIC)

class Tokenizer:
  
  SEGMENTATION_RULES = [
    (1, u'([' + Punctuation([':', 'dot', '`', 3, 4]).regex() + ']\s*[Ա-ՖևA-ZА-ЯЁ]+)'), #: Ա
    (2, u'([' + Punctuation([':', 'dot', '`', 3, 4]).regex() + ']\s*$)'), #:
    (3, u'([' + Punctuation(':').regex() + ']\s+[0-9]{1})'), #: 2016
    (4, u'([' + Punctuation.all() + ']\s*[' + Punctuation([5, 6]).regex() + ']+\s*[Ա-ֆևևA-zА-яЁё0-9]+)'), #, -
    (5, u'([' + Punctuation.all() + ']\s*[' + Punctuation(1).regex() + ']{1}\s*[Ա-ֆևևA-zА-яЁё0-9]+)'), #. <<
    (6, u'\.{1}\n'),
    (6, u'\S{1}\n'),
  ]
  
  TOKENIZATION_RULES = [
    (1, u'[' + Punctuation.inter() + ']'), # 5°С, $5, -5, +5
    (2, Punctuation.metric(double=True)), # 5կմ/ժ, 5մ/վ
    (3, u'[0-9]+-[ա-ֆԱ-Ֆևև]+'), #1-ին , 5-ական
    (4, u'թ[ա-ֆև]*\.*-[ա-ֆԱ-Ֆևև]+'), #1999թ.-ին
    (5, u'[0-9]+\s+[0-9]+'), #numbers 250 000
    (6, u'[0-9]+[\.|,|/]{1}[0-9]+'), #numbers 2.5 2,5 2/3
    (7, u'\.[0-9]+'), #numbers .5 , .08
    (7.1, u'[0-9]+'), #numbers 25
    (8, u'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'), #E-mail
    (9, u'@[a-z0-9_-]{3,}'), #nickname @gor_ar
    (10, u'[Ա-Ֆև]+[ա-ֆև]+-[Ա-Ֆև]+[ա-ֆև]+'), #Սայաթ-Նովա
    (11, u'[Ա-Ֆև]+-[ա-ֆև]+'), #ՀՀԿ-ական ( լավ չի, բայց ուրիշ օրինակ մտքիս չեկավ )
    (12, u'(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?'), #URL
    (13, u'[ա-ֆԱ-Ֆևև]+'), #simple word
    (14, u'[a-zA-Z]+'), #english word 
    (15, u'[а-яА-ЯЁё]+'), #russian word
    (16, u'\.{3,4}'), #.... , ...
    (17, u'([' + Punctuation.all() + ']{1})'), #all punctuations
    (18, u'([' + Punctuation.all(linear=True) + ']{1})'), #all punctuations
  ]
  
  SPECIAL_RULES = {
    'segment': [
      ( '__all__', False, u'[' + Punctuation(1).regex() + ']\s*[ա-ֆևa-zа-яё]{1}[A-zА-яЁёԱ-ֆևև\s։]+[^' + Punctuation(2).regex() + ']$' ), #<<bla bla: bla>> is not a segment
      ( [4], False, u'[0-9]{1}թ$' ), #1999թ.-ին is not a segment
    ],
    'token': [
      ( [4], True, u'[0-9]{1}$' ),
    ]
  }
  
  PURIFICATION_RULES = [
    ('<<', '«'),
    ('>>', '»'),
    ('(?P<w_beg>[ա-ֆԱ-Ֆևև]+)(?P<symbol>[' + Punctuation.all(linear=True) + ']){1}(?P<w_end>[ա-ֆԱ-Ֆևև]*)', '\g<w_beg>\g<w_end>\g<symbol>'), #LINEAR_PUNCTUATION
    ('(?P<day>[0-9]{1,4})(?P<symbol1>[' + Punctuation(['dot', 6, 16]).regex() + '])(?P<month>[0-9]{1,4})(?P<symbol2>[' + Punctuation(['dot', 6, 16]).regex() + '])(?P<year>[0-9]{1,4})',
      '\g<day> \g<symbol1> \g<month> \g<symbol2> \g<year>'), #Ամսաթվեր 20.12.2015
  ]
  
  def __init__(self, text):
    self.text = text
    self.text_length = len(text)
    self.segments = []
   
  def __str__(self):
    return self.print_()
    
  def print_(self):
    output = ''
    for s in self.segments:
      output += '{num}. {string}\n{line}\n'.format(num=s['id'], string=s['segment'], line='-' * 50)
      for t in s['tokens']:
        output += '{token}\n'.format(token=t)
      
      output += '\n'
    return output
    
  def output(self):
    return self.segments
  
  @classmethod
  def is_segment(cls, text, pointer):
    for index, r in cls.SEGMENTATION_RULES:
      if re.match(r, text[pointer:]):
        for s_r in cls.SPECIAL_RULES['segment']:
          if (isinstance(s_r[0], list) and index in s_r[0] ) or s_r[0] == '__all__':
            if not (( re.findall(s_r[2], text[:pointer]) and s_r[1] ) or ( not re.findall(s_r[2], text[:pointer]) and not s_r[1] )):
              return False
        return True
    return False

  @classmethod
  def find_token(cls, text, pointer):
    for index, r in cls.TOKENIZATION_RULES:
      token = re.match(r, text[pointer:])
      if token:
        for t_r in cls.SPECIAL_RULES['token']:
          if (isinstance(t_r[0], list) and index in t_r[0] ) or t_r[0] == '__all__':
            if not (( re.findall(t_r[2], text[:pointer]) and t_r[1] ) or ( not re.findall(t_r[2], text[:pointer]) and not t_r[1] )):
              return False
        return token
    return False

  def purification(self):
    for r in self.PURIFICATION_RULES:
      self.text = re.sub(r[0], r[1], self.text)
      
    self.text_length = len(self.text)
    return self
    
  def segmentation(self):
    self.purification()
    checkpoint = 0
    
    for l in range(self.text_length):
      if self.is_segment(self.text[checkpoint:], l-checkpoint):
        
        new_segment = self.text[checkpoint:l+1]
        clean_segment = new_segment.rstrip().lstrip()
        self.segments.append({
          'segment': clean_segment,
          'id': len(self.segments)+1,
          'tokens': []
        })
        
        checkpoint = l + 1
        
    return self

  def tokenization(self):
    for s in self.segments:
      l = 0
      
      while l < len(s['segment']):
        token = self.find_token(s['segment'], l)
        if token:
          l += token.end()
          new_token = token.group(0)
          clean_token = new_token.rstrip().lstrip()
          s['tokens'].append((len(s['tokens'])+1, clean_token))
        else:
          l += 1
          
    return self