from blog import app
#from  import get_todays_recent_posts
import unittest


class BasicTestCase(unittest.TestCase):
	#ensure that flask was setup correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
	#posts = get_todays_recent_posts()
     #render_template('myhome.html', posts=posts)       
	#self.assertEqual(response.data, posts)
	#self.assertEqual(response.data,b'Hello World!')

    def test_that_something_works():
        with self.client:
        response = self.client.post('login', { username: 'James', password: '007' })

        # success
        assertEquals(current_user.username, 'James')

if __name__ == '__main__':
    unittest.main()
