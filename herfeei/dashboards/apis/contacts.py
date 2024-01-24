from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.dashboards.models import Contact
from herfeei.dashboards.selectors.contacts import get_contacts


class ContactView(APIView):

    class OutputContactSerializer(serializers.ModelSerializer):
        icon_url = serializers.SerializerMethodField("get_url")

        class Meta:
            model = Contact
            fields = ("id", "title", "slug", "icon_url", "content",
                      "created_at")

        def get_url(self, obj):
            if obj.icon:
                request = self.context.get("request")

                if request:
                    return request.build_absolute_uri(obj.icon.url)
            return None

    def get(self, request):
        return Response(
            self.OutputContactSerializer(get_contacts(),
                                         many=True,
                                         context={
                                             "request": request
                                         }).data)
