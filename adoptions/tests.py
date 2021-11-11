from django.test import TestCase
from selenium import webdriver
from .forms import HashForm
from django.core.exceptions import ValidationError
from .models import Hash
import time

class FunctionalTestCases(TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def testHomePageTitle(self):
        self.browser.get("http://localhost:8000")
        # assert self.browser.page_source.find("Wisdom")
        self.assertIn("Wisdom",self.browser.page_source)

    def test_hash_display(self) -> None:
        self.browser.get("http://localhost:8000/form")
        text = self.browser.find_element_by_id("id_text")
        text.send_keys("hello")
        self.browser.find_element_by_name("submit").click()
        self.assertIn("2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",self.browser.page_source)


    def test_ajax(self) -> None:
        self.browser.get("http://localhost:8000/form")
        text = self.browser.find_element_by_id("id_text")
        text.send_keys("hello")
        time.sleep(5)
        self.assertIn("2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824", self.browser.page_source)

    def tearDown(self) -> None:
        self.browser.quit()


class UnitTestCaase(TestCase):

    def test_homepage_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response,"home.html")

    def test_hash_form(self):
        form = HashForm(data={'text':'hello'})
        self.assertTrue(form.is_valid())

    def test_hash_works(self):
        hash = Hash()
        hash.text = 'hello'
        hash.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
        hash.save()
        hash_pulled = Hash.objects.get(hash='2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        self.assertEqual(hash.text,hash_pulled.text)

    def test_bad_data(self):
        def badHash():
            hash = Hash()
            hash.text = 'hello'
            hash.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824wer'
            hash.full_clean()

        self.assertRaises(ValidationError,badHash)