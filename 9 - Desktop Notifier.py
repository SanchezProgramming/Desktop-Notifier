

from plyer import notification

title = "Hello! :D"

message = "THIS IS AN AWESOME PROJECT"


notification.notify(
    title = title,
    message = message,
    timeout = 20,
    toast = False
)