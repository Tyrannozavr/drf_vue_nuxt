def authenticate_user(request):
    email = request.data['email']
    password = request.data['password']
    user = User.objects.get(email=email, password=password)
    if user:
        payload = jwt_payload_handler(user)
        token = jwt.encode(payload, settings.SECRET_KEY)
        user_details = {'name': "%s %s" % (user.first_name, user.last_name), 'token': token}
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        return Response(user_details, status=status.HTTP_200_OK)

