from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class LocationTestClass(TestCase):
    #set up method
    def setUp(self):
        self.manow=Location(name='lankas')
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.manow,Location))    
    #testing save
    def test_save_method(self):
        self.manow.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
    #testing for deleting
    def test_delete_method(self):
        self.manow.save_location()
        self.manow.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0) 
    #testing display method
    def test_display_locations_methods(self):
        self.manow.save_location()
        self.manow.display_locations()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
    
#testing for Category
class CategoryTestClass(TestCase):
    #set up method
    def setUp(self):
        self.manow=Category(name="aurelia")
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.manow,Category))
    #testing save method
    def test_save_method(self):
        self.manow.save_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) > 0)
    #testing for deleting
    def test_delete_method(self):
        self.manow.save_category()
        self.manow.delete_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) == 0)
    #testing display method
    def test_display_categorys_methods(self):
        self.manow.save_category()
        self.manow.display_categorys()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) > 0)

#testing for Images
class ImageTestClass(TestCase):
    #set up method
    def setUp(self):
        #creating a new category and saving it
        self.manow=Category(name="lankas")
        self.manow.save_category()

        #creating a new insatance of location and saving it
        self.new_location=Location(name="japan")
        self.new_location.save()

        #creating a new instance of image and saving it
        self.new_image=Image(image_name="cubism",title="realism",location=self.new_location,category=self.manow)
        self.new_image.save_image()

    #testing instance
    def test_instance(self):
        self.assertFalse(isinstance(self.manow,Image))

    #testing for save functionality
    def test_save_method(self):
        self.new_image.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)
    #testing for deleting functionality
    def test_delete_method(self):
        self.new_image.save_image()
        self.new_image.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image) == 0)
    
    #testing display method
    def test_display_images_methods(self):
        self.new_image.save_image()
        self.new_image.display_images()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    
    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()    



