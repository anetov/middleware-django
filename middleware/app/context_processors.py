from .models import IceCream


def icecream_context(request):
    icecreams = IceCream.objects.all()
    return {'icecreams':icecreams}