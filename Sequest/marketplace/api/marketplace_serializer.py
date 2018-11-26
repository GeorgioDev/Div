from rest_framework import serializers
from marketplace.models import Request, Offer, OfferMedia, Message, HiddenRequest


class RequestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class RequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
        read_only_fields = ('id', 'starter', 'request_slug', 'is_active', 'is_reported', 'last_update')

        def create(self, validated_data):
            subject = validated_data['subject']
            message = validated_data['message']

            # Get the requesting user
            user = None
            request = self.context.get("request")
            if request and hasattr(request, "user"):
                user = request.user
            else:
                raise serializers.ValidationError('Must be authenticated to create thread')

            # Create the thread
            request = Request(
                subject=subject,
                message=message,
                starter=user
            )
            request.save()
            return request


class RequestDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
        read_only_fields = ('id',)

    creator = CreatorSerializer(read_only=True)
    posts = ThreadPostSerializer(many=True, read_only=True)
    created_at = serializers.SerializerMethodField()


class RequestDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class RequestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class RequestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'











class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'



class OfferMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferMedia
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class HiddenRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HiddenRequest
        fields = '__all__'

