from rest_framework import viewsets, status
from rest_framework.response import Response
from app.models.models import NewsCategory, News
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from app.news.category.serializers.read import NewsCategoryReadSerializer
from app.news.category.serializers.write import NewsCategoryWriteSerializer
from app.news.news.serializers.read import NewsReadSerializer
from app.news.news.serializers.write import NewsWriteSerializer

class NewsCategoryViewSet(viewsets.ModelViewSet):
    queryset = NewsCategory.objects.all().prefetch_related(
        "newscategorytranslations_set",
        "newscategorytranslations_set__language"
    )

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return NewsCategoryReadSerializer
        return NewsCategoryWriteSerializer

    def create(self, request, *args, **kwargs):
        write_serializer = NewsCategoryWriteSerializer(data=request.data)
        write_serializer.is_valid(raise_exception=True)
        instance = write_serializer.save()
        
        read_serializer = NewsCategoryReadSerializer(instance)
        headers = self.get_success_headers(read_serializer.data)
        
        return Response(
            read_serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        write_serializer = NewsCategoryWriteSerializer(
            instance, 
            data=request.data, 
            partial=partial
        )
        write_serializer.is_valid(raise_exception=True)
        instance = write_serializer.save()
        
        read_serializer = NewsCategoryReadSerializer(instance)
        return Response(read_serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        read_serializer = NewsCategoryReadSerializer(instance)
        data = read_serializer.data
        
        instance.delete()
        
        return Response(
            {
                "message": "Амжилттай устгалаа.",
                "deleted_data": data
            },
            status=status.HTTP_200_OK
        )

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().prefetch_related(
        "newsimages_set",
        "newssocials_set",
        "newstitletranslations_set",
        "newstitletranslations_set__language",
        "newsshortdesctranslations_set",
        "newsshortdesctranslations_set__language",
        "newscontenttranslations_set",
        "newscontenttranslations_set__language"
    )
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return NewsReadSerializer
        return NewsWriteSerializer

    def create(self, request, *args, **kwargs):
        write_serializer = NewsWriteSerializer(data=request.data)
        write_serializer.is_valid(raise_exception=True)
        instance = write_serializer.save()
        
        read_serializer = NewsReadSerializer(instance)
        headers = self.get_success_headers(read_serializer.data)
        
        return Response(
            read_serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        write_serializer = NewsWriteSerializer(
            instance, 
            data=request.data, 
            partial=partial
        )
        write_serializer.is_valid(raise_exception=True)
        instance = write_serializer.save()
        
        read_serializer = NewsReadSerializer(instance)
        return Response(read_serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        read_serializer = NewsReadSerializer(instance)
        data = read_serializer.data
        
        if instance.image:
            clean_filename = instance.image.replace('media/', '').replace('news/', '')
            image_path = os.path.join(settings.MEDIA_ROOT, 'news', clean_filename)
            if os.path.exists(image_path):
                try:
                    os.remove(image_path)
                except Exception as e:
                    print(f"Алдаа гарлаа: {e}")
        
        instance.delete()
        
        return Response(
            {
                "message": "Амжилттай.",
                "deleted_data": data
            },
            status=status.HTTP_200_OK
        )