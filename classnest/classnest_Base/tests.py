from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from classnest_Base.models import Course
from classnest_Base.forms import CourseForm  # Ensure this import is correct
#from quiz_app.models import Quiz  # Update this import if Quiz is in a different app

class CourseModelTest(TestCase):

    def setUp(self):
        self.instructor = User.objects.create_user(
            username='testinstructor',
            email='instructor@example.com',
            password='password123'
        )
        self.course = Course.objects.create(
            title='Test Course',
            description='This is a test course.',
            instructor=self.instructor
        )

    def test_course_title(self):
        self.assertEqual(self.course.title, 'Test Course')

    def test_course_description(self):
        self.assertEqual(self.course.description, 'This is a test course.')

    def test_course_instructor(self):
        self.assertEqual(self.course.instructor.username, 'testinstructor')

class QuizModelTest(TestCase):

    def setUp(self):
        self.student = User.objects.create_user(
            username='teststudent',
            email='student@example.com',
            password='password123'
        )
        self.quiz = Quiz.objects.create(
            title='Sample Quiz',
            description='This is a sample quiz.',
            created_by=self.student
        )

    def test_quiz_creation(self):
        self.assertEqual(self.quiz.title, 'Sample Quiz')
        self.assertEqual(self.quiz.description, 'This is a sample quiz.')
        self.assertEqual(self.quiz.created_by.username, 'teststudent')

class UploadPDFViewTest(TestCase):

    def setUp(self):
        self.instructor = User.objects.create_user(
            username='testinstructor',
            email='instructor@example.com',
            password='password123'
        )
        self.client.login(username='testinstructor', password='password123')

    def test_upload_pdf_view_get(self):
        response = self.client.get(reverse('upload_pdf'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Quiz_Base/upload.html')

    def test_upload_pdf_view_post(self):
        with open('path/to/sample.pdf', 'rb') as pdf_file:
            response = self.client.post(reverse('upload_pdf'), {'pdf': pdf_file})
        self.assertEqual(response.status_code, 200)

class CourseFormTest(TestCase):

    def test_valid_course_form(self):
        form_data = {
            'title': 'New Course',
            'description': 'This is a new course.'
        }
        form = CourseForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_course_form(self):
        form_data = {
            'title': '',
            'description': 'This is an incomplete course.'
        }
        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())

class QuizIntegrationTest(TestCase):

    def setUp(self):
        self.instructor = User.objects.create_user(
            username='testinstructor',
            email='instructor@example.com',
            password='password123'
        )
        self.course = Course.objects.create(
            title='Sample Course',
            description='This is a sample course.',
            instructor=self.instructor
        )

    def test_full_quiz_flow(self):
        with open('path/to/sample.pdf', 'rb') as pdf_file:
            response = self.client.post(reverse('upload_pdf'), {'pdf': pdf_file})
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('quiz_page'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Question")

        response = self.client.post(reverse('submit_quiz'), {'question_1': 'A', 'question_2': 'B'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your score")

View Tests
class DashboardViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )
        self.client.login(username='testuser', password='password123')

    def test_dashboard_page_contents(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'classnest_Base/dashboard.html')
        self.assertContains(response, "Welcome to ClassNest")

class BrowseCoursesViewTest(TestCase):

    def setUp(self):
        self.student = User.objects.create_user(
            username='teststudent',
            email='student@example.com',
            password='password123'
        )
        self.client.login(username='teststudent', password='password123')

    def test_browse_offered_courses(self):
        response = self.client.get(reverse('browse_courses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'classnest_Base/courses.html')

class ViewCourseDetailsTest(TestCase):

    def setUp(self):
        self.student = User.objects.create_user(
            username='teststudent',
            email='student@example.com',
            password='password123'
        )
        self.course = Course.objects.create(
            title="Sample Course",
            description="This is a sample course.",
            instructor=self.student  # Assuming the student is also an instructor here
        )
        self.client.login(username='teststudent', password='password123')

    def test_view_course_details(self):
        response = self.client.get(reverse('course_detail', args=[self.course.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'classnest_Base/course_detail.html')

class UpdateCourseModuleTest(TestCase):

    def setUp(self):
        self.teacher = User.objects.create_user(
            username='testteacher',
            email='teacher@example.com',
            password='password123'
        )
        self.course = Course.objects.create(
            title="Sample Course",
            description="This is a sample course.",
            instructor=self.teacher
        )
        self.client.login(username='testteacher', password='password123')

    def test_update_course_module(self):
        response = self.client.post(reverse('update_module', args=[self.course.id]), {
            'module_title': 'Updated Module Title',
            'module_content': 'Updated module content.'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful update

class ApproveCourseOfferingTest(TestCase):

    def setUp(self):
        self.admin = User.objects.create_superuser(
            username='adminuser',
            email='admin@example.com',
            password='adminpassword'
        )
        
    def test_approve_course_offering(self):
        self.client.login(username='adminuser', password='adminpassword')
        response = self.client.post(reverse('approve_course', args=[1]), {
            'action': 'approve'
        })
        self.assertEqual(response.status_code, 302)

class SubmitAssignmentTest(TestCase):

    def setUp(self):
        self.student = User.objects.create_user(
            username='teststudent',
            email='student@example.com',
            password='password123'
        )
        
    def test_submit_assignment(self):
        with open('path/to/sample_assignment.pdf', 'rb') as assignment_file:
            response = self.client.post(reverse('submit_assignment'), {
                'assignment': assignment_file,
                'course_id': 1  # Assuming course ID is 1 for this test case.
            })
            self.assertEqual(response.status_code, 302)
