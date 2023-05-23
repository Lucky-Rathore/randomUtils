from bardapi import Bard
import os

os.environ['_BARD_API_KEY']="WgiKtatzTIt0BtqB5VLFPBuUj79XRx1DktKsY6_xMimax1fhQMaRHg7c6STkUj-9BI6ETw."
Bard().get_answer("provide 3 multiple choice question with answer as a JSON for "python: For Loops", Use JSON Format: [{ "question": "question text", "options": ["option1", "option2", "option3", "option4" ], "correctAnswerIndex": 2 }")['content']
