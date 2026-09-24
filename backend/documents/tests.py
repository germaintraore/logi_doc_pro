
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Document, Template

User = get_user_model()


class TemplateModerationTests(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(username='Eline', password='password12345')
        self.admin = User.objects.create_user(
            username='boss', password='password12345', is_staff=True
        )
        self.intruder = User.objects.create_user(
            username='intruder', password='password12345'
        )

    def _draft(self):
        return Template.objects.create(name='CV Moderne', created_by=self.author)

    def test_default_status_is_draft(self):
        template = self._draft()
        self.assertEqual(template.status, Template.Status.DRAFT)

    def test_submit_then_approve_flow(self):
        template = self._draft()
        template.submit_for_review(self.author)
        self.assertEqual(template.status, Template.Status.PENDING_REVIEW)
        template.start_review(self.admin)
        self.assertEqual(template.status, Template.Status.UNDER_REVIEW)
        template.approve(self.admin, official=True)
        template.refresh_from_db()
        self.assertEqual(template.status, Template.Status.PUBLISHED)
        self.assertTrue(template.is_official)

    def test_reject_then_resubmit_flow(self):
        template = self._draft()
        template.submit_for_review(self.author)
        template.reject(self.admin, note='Manque la section de garde')
        self.assertEqual(template.status, Template.Status.REJECTED)
        self.assertEqual(template.review_note, 'Manque la section de garde')
        template.submit_for_review(self.author)
        self.assertEqual(template.status, Template.Status.PENDING_REVIEW)

    def test_withdraw_submission_returns_to_draft(self):
        """BR-TMP-02 : gel de la soumission, mais retirage par l'auteur tant que non publié."""
        template = self._draft()
        template.submit_for_review(self.author)
        template.withdraw_submission(self.author)
        self.assertEqual(template.status, Template.Status.DRAFT)

    def test_non_creator_cannot_submit(self):
        template = self._draft()
        with self.assertRaises(ValidationError):
            template.submit_for_review(self.intruder)

    def test_user_cannot_reject(self):
        template = self._draft()
        template.submit_for_review(self.author)
        with self.assertRaises(ValidationError):
            template.reject(self.intruder, note='x')

    def test_reject_requires_note(self):
        template = self._draft()
        template.submit_for_review(self.author)
        with self.assertRaises(ValidationError):
            template.reject(self.admin, note='')

    def test_archive_only_published(self):
        template = self._draft()
        with self.assertRaises(ValidationError):
            template.archive(self.admin)
        template.submit_for_review(self.author)
        template.start_review(self.admin)
        template.approve(self.admin)
        template.archive(self.admin)
        self.assertEqual(template.status, Template.Status.ARCHIVED)


class DocumentInstantiationTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username='owner', password='password12345')
        self.template = Template.objects.create(name='Rapport de stage', created_by=self.owner)

    def test_document_content_is_independent_json(self):
        """BR-TMP-05 : le contenu du document est une copie JSONB indépendante du modèle."""
        doc = Document.objects.create(
            title='Mon rapport',
            owner=self.owner,
            template=self.template,
            content={'blocks': [{'type': 'paragraph', 'text': 'Introduction'}]},
        )
        doc.content['blocks'][0]['text'] = 'Modifié localement'
        doc.save()
        self.assertEqual(self.template.structure, {})
        self.assertEqual(doc.content['blocks'][0]['text'], 'Modifié localement')

    def test_document_survives_template_deletion(self):
        doc = Document.objects.create(title='Doc', owner=self.owner, template=self.template)
        self.template.delete()
        doc.refresh_from_db()
        self.assertIsNone(doc.template)
