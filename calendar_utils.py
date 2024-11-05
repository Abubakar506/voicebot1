# calendar_utils.py
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from aut import authenticate_google_calendar

def create_appointment(start_time, end_time, patient_email, clinic_email):
    creds = authenticate_google_calendar()
    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': 'Dental Appointment',
        'location': '123 Dental Way, Suite 456, Medical District, Springfield',
        'description': 'Dental appointment for patient.',
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'America/New_York',
        },
        'attendees': [
            {'email': patient_email},
            {'email': clinic_email},
        ],
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f'Appointment created: {event.get("htmlLink")}')
    return event
