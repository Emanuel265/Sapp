from django.http import HttpResponse


def index(request, command: str):
    match command:
        case "Lauter":
            print("Radio ON")
        case "Leiser":
            print("Radio OFF")
    return HttpResponse(request)
