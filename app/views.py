from django.core.exceptions import ValidationError
from django.shortcuts import render


# Create your views here.

def xml_to_json(request):
    if request.method == 'POST':
        xml = request.FILES['xml']
        print(xml.content_type)
        print(xml.size)
        if xml.content_type != 'text/xml':
            raise ValidationError("File is not XML.")

    return render(request, 'index.html')
