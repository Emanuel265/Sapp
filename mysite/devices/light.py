from django.http import HttpResponse


def index(request, command: str):
    match command:
        case "Ein":
            print("Light ON")
        case "Aus":
            print("Light OFF")
    return HttpResponse(request)
