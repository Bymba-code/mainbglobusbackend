from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import os

from app.models.models import HeroSlider
from app.serializers.heroSlider import HeroSliderSerializer


class HeroSliderViewSet(ModelViewSet):
    queryset = HeroSlider.objects.all()
    serializer_class = HeroSliderSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        data = request.data.copy()  
        if file:
            save_path = self._save_file(file)
            # file path-г зөвхөн string болгож дамжуул
            mutable_data = data.copy()  # QueryDict-г copy хийж болно
            mutable_data['file'] = save_path
            serializer = self.get_serializer(data=mutable_data)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        file = request.FILES.get('file')

        data = request.data.copy()  # copy хийж болно, files объект биш бол аюулгүй
        if file:
            save_path = self._save_file(file)
            data['file'] = save_path
        else:
            data['file'] = instance.file

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def _save_file(self, file):
        """Файлыг хадгалах helper function"""
        save_folder = 'media/hero_sliders'
        os.makedirs(save_folder, exist_ok=True)
        save_path = os.path.join(save_folder, file.name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        # return relative path for Image URL
        return save_path.replace('\\', '/')  # Windows-д path засах
