from rest_framework.response import Response
from .models import Employee
# from .models import Profile
from .serializers import  *
from rest_framework.views import APIView


# Create your views here.




# class Getprofile(APIView):
#     def post(self,request):
#         data = request.data

#         serializer = ProfileSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()

#             return Response({"message": "employee added successfully!"})
#         return Response({"message": "invalid data"})
    
#     def get(self,request):
#         emp = Profile.objects.all()
#         serializer =  ProfileSerializer(emp, many= True)
        
#         return Response({"emp":serializer.data})
    
    
    
class profile(APIView):
    def post(self,request):
        data = request.data

        serializer = EmployeeSerializer(data = data)
        if serializer.is_valid():
            serializer.save()

            return Response({"message": " added successfully!"})
        return Response(serializer.errors)
        
    def get(self,request,pk=None):
        if pk:
            try:
                emp = Employee.objects.get(id= pk)
                serializer = EmployeeSerializer(emp, many = False)

                return Response({"emp": serializer.data})
            except:
                return Response({"message": "Employee not found"})
        else:
            emp = Employee.objects.all()
            serializer =  EmployeeSerializer(emp, many= True)
        
            return Response(serializer.data)
    
    def put(self,request,pk):
        try: 
            emp = Employee.objects.get(id = pk)
            serializer = EmployeeSerializer(emp, data = request.data )

            if serializer.is_valid():
                serializer.save()

                return Response({"message":"employee updated successfully!"})
            return Response({"message":"invalid data"})
        except:
            return Response({"message": "Employee not found"})
        
    def delete(self,request,pk):
        try:
            emp = Employee.objects.get(id = pk)
            emp.delete()
            return Response({"message": "employee deleted successfully!"})

        except:
            return Response({"message": "employee not found"})