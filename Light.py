# -*- coding: utf-8-*-
import re
import subprocess
import os

WORDS = ["RIGHT"]
user = os.environ["USER"]
script = "/home/" + user + "/bin/jlight-helper.sh"

def isValid(text):
  """
    Returns True if the text is related to Jasper's status.

    Arguments:
    text -- user-input, typically transcribed speech
  """
  return bool(re.search(r'\b(right)\b', text, re.IGNORECASE))

def handle(text, mic, profile):
  response = "Okay"
  subprocess.call([ script ])
  mic.say(response)
