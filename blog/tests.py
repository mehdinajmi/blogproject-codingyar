from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from . models import Post


class BlogPostTest(TestCase):
    @classmethod # # in this method we  use class method to create SetUp function
    def setUpTestData(cls):
        cls.user = User.objects.create(username='noshin')
        cls.post1 = Post.objects.create(
            author=cls.user,
            title='post1',
            text='This is descreption of psot1',
            status=Post.STATUS_CHOICES[0][0], )
        cls.post2 = Post.objects.create(
            author=cls.user,
            title='post2',
            text='This is descreption of psot2',
            status=Post.STATUS_CHOICES[1][0], )

    # def setUp(self): # in this methos we did not use class method to create SetUp function
    #     self.user=User.objects.create(username='noshin')
    #     self.post1= Post.objects.create(
    #         author=self.user,
    #         title='post1',
    #         text='This is descreption of psot1',
    #         status=Post.STATUS_CHOICES[0][0],)
    #     d.post2 = Post.objects.create(
    #         author=self.user,
    #         title='post2',
    #         text='This is descreption of psot2',
    #         status=Post.STATUS_CHOICES[1][0],)

    # def test_post_model_str(self):
    #     post = self.post1
    #     self.assertEqual(str(post), post.title)

    def test_post_detail(self):
        self.assertEqual(self.post1.title, 'post1')

    def test_post_list_url(self):
        response =self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_url_by_name(self):
        response =self.client.get(reverse('post_list_view'))
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_post_list(self):
        response = self.client.get(reverse('post_list_view'))
        self.assertContains(response, self.post1.title)

    def test_post_details__page_url(self):
        response =self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_details_url_by_name(self):
        response = self.client.get(reverse('post_detail_view', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_blog_list_page(self):
        response = self.client.get(reverse('post_detail_view', args=[self.post1.id]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_status_404_if_post_id_not_exist(self):
        response = self.client.get(reverse('post_detail_view', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_draft_post_not_shown_in_post_list(self):
        response = self.client.get(reverse('post_list_view'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_create_view(self):
        response = self.client.post(reverse('add_create'), {'title': ' some title','text': ' this is some text', 'status': 'PUB',
                                                           'author': self.user.id, })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'some title')
        self.assertEqual(Post.objects.last().text, 'this is some text')

    def test_post_update_view(self):
        response=self.client.post(reverse('post_update', args=[self.post2.id] ),{
            'title': ' post2 update', 'text':' this text is updated','status':'PUB','author':self.post2.author.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'post2 update')
        self.assertEqual(Post.objects.last().text, 'this text is updated')
    #
    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post2.id]), )
        self.assertEqual(response.status_code, 302)
    #
    #


# Create your tests here.
