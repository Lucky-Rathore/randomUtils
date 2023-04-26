import requests
import datetime
import json

courseDir = '/home/lucky/Desktop/course'

def createProblemXml(title, jsonData):
  for j, question in enumerate(jsonData):
    try:
      optionXml = []
      for option in question['options']:
        optionXml.append( '<choice correct="false">__option__</choice>'.replace('__option__', option) )
      i = question['correctAnswerIndex']
      optionXml[i] = optionXml[i].replace('false', 'true')
      questionXML = '''
      <problem display_name="Multiple Choice">
        <multiplechoiceresponse>  
          <question>__question__</question>
          <choicegroup type="MultipleChoice">
            __options__
          </choicegroup>
        </multiplechoiceresponse> 
      </problem>'''
      questionXML = questionXML.replace('__question__', question['question'])
      questionXML = questionXML.replace('__options__', '\n'.join(optionXml) )
      with open( courseDir + '/drafts/problem/' + title + str(j) + '.xml', 'w' ) as f:
        f.write(questionXML)
    except Exception as e:
      print('failed for', title, question, jsonData)
      print(e)#todo retry log ;) # 5 min

def createVertical(displayName, title, questionCount, childIndex):
  question = []
  for i in range(questionCount):
    question.append('<problem url_name="__url__"/>'.replace('__url__', title + str(i) ))
  verticalXml = '''
  <vertical display_name="__displayName__ quiz" parent_url="block-v1:getfreecertificate+PY101+2023_01+type@sequential+block@16aefc41a6384342bff96ee71aced473" index_in_children_list="__childIndex__">
    __question__
  </vertical>'''
  verticalXml = verticalXml.replace('__displayName__', displayName) 
  verticalXml = verticalXml.replace('__question__',  '\n'.join(question))
  verticalXml = verticalXml.replace('__childIndex__',   str(childIndex))
  with open( courseDir + '/drafts/vertical/' + title + '.xml', 'w') as f:
    f.write(verticalXml)

def getQuiz(topic):
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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',
  }

  json_data = {
      'model': 'text-davinci-003',
      'prompt': "rephrase the following text to be more readable: " + topic,
      'temperature': .7,
      'max_tokens': 500,
  }
  response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=json_data)
  article = response.json()

  with open('/home/lucky/Dropbox/quiz.txt', 'a') as f:
    f.write(str(article))
    f.write('\n')

  print('request: ' + topic)
  print('reponse: ' + article['choices'][0]['text'].strip())
  return article['choices'][0]['text'].strip()

def processQuery(i, title, quiz):
  quiz = json.loads(  getQuiz(quiz)) 
  displayName = title[:]
  title = title.replace('&', 'and').replace('/', '').replace(' ', '').lower()
  createVertical(displayName, title, len(quiz), i)
  createProblemXml(title, quiz)

a= [

'Introduction to python',
'Installing Python and PyCharm',
'Setup and Hello World',
'Drawing a Shape',
'Variables and Data Types',
'Working With Strings',
'Working With Numbers',
'Getting Input From Users',
'Building a Basic Calculator',
'Mad Libs Game',
'Lists',
'List Functions',
'Tuples',
'Functions',
'Return Statement',
'If Statements',
'If Statements and Comparisons',
'Building a better Calculator',
'Dictionaries',
'While Loop',
'Building a Guessing Game',
'For Loops',
'Exponent Function',
'2D Lists and Nested Loops',
'Building a Translator',
'Comments',
'Try  Except',
'Reading Files',
'Writing to Files',
'Modules and Pip',
'Classes and Objects',
'Building a Multiple Choice Quiz',
'Object Functions',
'Inheritance',
'Python Interpreter'

]

magiccc = 'provide 3 multiple choice question with answer as a JSON for "python: __topic__", Use JSON Format: [{ "question": "question text", "options": ["option1", "option2", "option3", "option4" ], "correctAnswerIndex": 2 }]'

print('total: ', len(a))

for i, q in enumerate(a):
  try:
    print('processing: ', q)
    query = magiccc.replace('__topic__', q)
    processQuery(i,  q,   query)
  except Exception as e :
    print('failed for: ' + q )
    print(e)

# processQuery(5, 'Variables and Data Types', '')