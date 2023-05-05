# Python
import os

# Local
from django.conf import settings

# Third-party
import openpyxl


def write_messages_to_excel(messages):
    filename = os.path.join(settings.BASE_DIR, 'messages.xlsx')

    try:
        workbook = openpyxl.load_workbook(filename)
    except (FileNotFoundError, KeyError):
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = 'Messages'
        worksheet.append(['Date', 'Sender', 'Chat_name', 'Text'])
    finally:
        worksheet = workbook['Messages']
    
    for message in messages:
        row = [
            message.datetime_send.replace(tzinfo=None),
            message.sender.username,
            message.to_send.name,
            message.text
        ]
        worksheet.append(row)
    
    workbook.save(filename)
    print('Ну шо народ погнали ...')
