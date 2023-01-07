from rest_framework import generics, permissions
from . models import House
from . serializers import houseserializer, photoserializer

# list houses
class MainHouses(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = houseserializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs =qs.filter(public = True)
        return qs

#list houses that were created by the user

class Myhouses(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = houseserializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        qs = qs.filter(owner=user)
        return qs






class SearchHouse(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = houseserializer

    def get_queryset(self):
        qs = super().get_queryset()
        q= self.request.query_params.get('q')
        print (q)
        address_query = qs.filter(address__icontains=q, public = True)
        location_query = qs.filter(location__icontains = q , public = True)
        description_query = qs.filter(description__icontains=q, public = True)
        qs = [*address_query , *location_query, *description_query]
        return qs
        

# create a houes
class CreateHouse(generics.CreateAPIView):
    serializer_class = houseserializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)

# add the photos to the house
class CreatePhotos(generics.CreateAPIView):
    serializer_class = photoserializer


#house details view
class HouseDetails(generics.RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = houseserializer
    lookup_field = 'pk'


#update house view
class UpdateHouse(generics.UpdateAPIView):
    queryset =  House.objects.all()
    serializer_class = houseserializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        qs = qs.filter(owner=user)
        return qs

#destroy houes viwe
class DeleteHouse(generics.DestroyAPIView):
    queryset = House.objects.all()
    serializer_class = houseserializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        qs = qs.filter(owner=user)
        return qs




