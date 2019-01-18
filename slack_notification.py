import slackweb

# IncomingWebhookのURLにPostする
URL = "IncomingWebhook URL"

# Line notification 
def notify( msg):
    slack = slackweb.Slack(url = URL)
    slack.notify(text=msg)
