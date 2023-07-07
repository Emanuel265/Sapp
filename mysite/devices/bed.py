from django.http import HttpResponse


def index(request, command: str):
    match command:
        case "Ein":
            print("Bed ON")
        case "Aus":
            print("Bed OFF")
    return HttpResponse(request)
