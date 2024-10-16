from django.shortcuts import render


def test(request):
    if request.mehtod == "GET":
        text = "This is for testing URL"
        print(text)
    return text
