import cohere
import sys, os

sys.path.append(os.path.abspath(os.path.join('..')))
import config
api_key = config.cohere_api['api_key']
co = cohere.Client(api_key)
response = co.generate(
  model='large',
  prompt='This program will extract relevant entities from job decription. Here are some examples:\n\ndocument: Bachelor\'s degree in Mechanical Engineering or Physical Science 3+ years track record of developing or specifying fiber optic cables and connector related products Knowledge of fiber optic component, cabling, and interconnect products, technologies, and standards Experience in statistical data analysis Experience with product life cycle management (PLM) process Experience providing solutions to problems and meeting deadlines Experience engaging stakeholders PREFERRED Advanced degree Experience using a software tool for statistical data analysis such as JMP Experience using Agile as product life-cycle management tool Data center or other mission critical development experience\",\n  \n\nExtracted Text:\nDIPLOMA: Bachelor, \nEXPERIENCE: 3+ years\n--\ndocument: 10+ years of software engineering work experience. Technical experience in release automation engineering, CI/CD or related roles. Experience building and leading a software organization through product design, delivery and commercialization of consumer electronics devices. Experience recruiting and managing technical teams, including performance management. BS/MS in Computer Science. Experience in leading timeline, multi-partner initiatives. Organizational communication and coordination experience. PREFERRED 5+ years of experience with hands-on technical management, release engineering, tools engineering, DevOps, or related area.\",\n    \n\nExtracted Text:',
  max_tokens=20,
  temperature=0.5,
  k=0,
  p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=["--"],
  return_likelihoods='NONE')
print('Prediction: {}'.format(response.generations[0].text))