from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserRegisterForm
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

@api_view(['POST'])
def register(request):
    try:
        if request.method != 'POST':
            raise ValidationError("Invalid request method")

        # Check if the request contains JSON data
        if request.content_type != 'application/json':
            raise ValidationError("Unsupported content type")

        form = UserRegisterForm(data=request.data)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return Response({"success": f'Account created for {username}!'})
        else:
            print(form)
            raise ValidationError("Invalid form data")

    except ValidationError as e:
        return Response({"error": str(e)}, status=400)

    except IntegrityError as e:
        # Handle integrity constraint violation (e.g., duplicate username)
        return Response({"error": "User with this username already exists"}, status=400)

    except Exception as e:
        # Handle other unexpected errors
        return Response({"error": "An unexpected error occurred"}, status=500)
