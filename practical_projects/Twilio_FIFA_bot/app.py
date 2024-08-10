import os
from flask import Flask, request
import requests
from dateutil import parser, tz
from twilio.twiml.messaging_response import MessagingResponse

"""
TODO change website for extracting information because ssl certificate 
    problems happens'

    .strftime('%I:%M %p on %d %b'):
        • %I gives us the hour in 12-hour format
        • %M gives us the minutes
        • %p gives us AM/PM
        • %d gives us the date
        • %b gives us the abbreviated month (e.g Jun)

"""

urls = {'group': 'https://worldcup.sfg.io/teams/group_results',
        'country': 'https://worldcup.sfg.io/matches/country?fifa_code=',
        'today': 'https://worldcup.sfg.io/matches/today',
        'tomorrow': 'https://worldcup.sfg.io/matches/tomorrow'
    }       

countries = ['KOR', 'PAN', 'MEX', 'ENG', 'COL', 'JPN', 'POL', 'SEN',
            'RUS', 'EGY', 'POR', 'MAR', 'URU', 'KSA', 'IRN', 'ESP',
            'DEN', 'AUS', 'FRA', 'PER', 'ARG', 'CRO', 'BRA', 'CRC',
            'NGA', 'ISL', 'SRB', 'SUI', 'BEL', 'TUN', 'GER', 'SWE']

html = requests.get(urls['today']).json()
data = requests.get(urls['country']+'ARG').json()


for match in html:
    print(match['home_team_country'], 'vs',
        match['away_team_country'], 'at',
        match['datetime'])
    
for match in data:
    if match['status'] == 'completed':
        print(match['home_team']['country'],
            match['home_team']['goals'],
            "vs", match['away_team']['country'],
            match['away_team']['goals'])
    if match['status'] == 'future':
        print(match['home_team']['country'], "vs",
            match['away_team']['country'],
            "at", match['datetime'])

data = requests.get(urls['group']).json()

for group in data:
    print("--- Group", group['letter'], "---")
    for team in group['ordered_teams']:
        print(team['country'], "Pts:",
        team['points'])
print('\n'.join(countries))




app = Flask(__name__)

# Despite i am living in Ukraine in that case i am prefer to use American time zone
to_zone = tz.gettz('America/New_York')


"""
whenever someone sends an SMS to your Twilio number, Twilio
will send a POST request to this webhook with the contents of that SMS. We will
respond to this POST request with a TwiML template, which will tell Twilio what
to send back to the SMS sender"""

@app.route('/', methods=['POST'])
def receive_sms():
    body = request.values.get('Body', '').lower().strip()
    resp = MessagingResponse()
    
    if body == 'today':
        data = requests.get(urls['today']).json()
        output = "\n"
        for match in data:
            output += match['home_team_country'] + ' vs ' + \
            match['away_team_country'] + " at " + \
            parser.parse(match['datetime']).astimezone(to_zone).strftime('%I:%M %p') + "\n"

        else:
            output += "No matches happening today"

    elif body == 'tomorrow':
        data = requests.get(urls['tomorrow']).json()
        output = "\n"

        for match in data:
            output += match['home_team_country'] + ' vs ' + \
            match['away_team_country'] + " at " + \
            parser.parse(match['datetime']).astimezone(to_zone).strftime('%I:%M %p') + "\n"

        else:
            output += "No matches happening tomorrow"

    elif body.upper() in countries:
        data = requests.get(urls['country']+body).json()
        output = "\n--- Past Matches ---\n"
        for match in data:
            if match['status'] == 'completed':
                output += match['home_team']['country'] + " " + \
                    str(match['home_team']['goals']) + " vs " + \
                    match['away_team']['country']+ " " + \
                    str(match['away_team']['goals']) + "\n"



        output += "\n\n--- Future Matches ---\n"
        for match in data:
            if match['status'] == 'future':
                output += match['home_team']['country'] + " vs " + \
                match['away_team']['country'] + " at " + \
                parser.parse(match['datetime']).astimezone(to_zone).strftime('%I:%M %p on %d %b') +"\n"
    elif body == 'complete':
        data = requests.get(urls['group']).json()
        output = ""
        for group in data:
            output += "\n\n--- Group " + group['letter'] + " ---\n"
            for team in group['ordered_teams']:
                output += team['country'] + " Pts: " + \
                str(team['points']) + "\n"

    elif body == 'list':
        output = '\n'.join(countries)

                
    resp.message(output)
    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)