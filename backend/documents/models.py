from django.db import models
from django.conf import settings

from django.core.exceptions import ValidationError

# Create your models here.
class Template(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DRAFT', 'Brouillon'
        PENDING_REVIEW = 'PENDING_REVIEW', 'En attente de revue'
        UNDER_REVIEW = 'UNDER_REVIEW', 'En cours de revue'
        REJECTED = 'REJECTED', 'Rejeté'
        PUBLISHED = 'PUBLISHED', 'Publié'
        ARCHIVED = 'ARCHIVED', 'Archivé'

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    structure = models.JSONField(default=dict, blank=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='templates_created',
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    review_note = models.TextField(blank=True)

    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='templates_reviewed',
    )

    is_official = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

# ---------- Gardes transverses ----------
    def _assert_is_creator(self, user):
        if user != self.created_by:
            raise ValidationError("Seul l'auteur du modèle peut effectuer cette action.")

    def _assert_is_admin(self, user):
        if not (user.is_staff or user.is_superuser):
            raise ValidationError("Seul un administrateur peut effectuer cette action.")


# ---------- Transitions d'état ----------
    def submit_for_review(self, user):
        """DRAFT ou REJECTED -> PENDING_REVIEW (acteur : l'auteur)."""
        self._assert_is_creator(user)
        if self.status not in (self.Status.DRAFT, self.Status.REJECTED):
            raise ValidationError(
                "Un modèle ne peut être soumis qu'en statut Brouillon ou Rejeté."
            )
        self.status = self.Status.PENDING_REVIEW
        self.review_note = ''
        self.save(update_fields=['status', 'review_note', 'updated_at'])

    def withdraw_submission(self, user):
        """PENDING_REVIEW/UNDER_REVIEW -> DRAFT (acteur : l'auteur).
        BR-TMP-02 : l'auteur peut retirer sa soumission tant qu'elle n'est pas publiée."""
        self._assert_is_creator(user)
        if self.status not in (self.Status.PENDING_REVIEW, self.Status.UNDER_REVIEW):
            raise ValidationError(
                "Une soumission ne peut être retirée qu'en attente ou en cours de revue."
            )
        self.status = self.Status.DRAFT
        self.save(update_fields=['status', 'updated_at'])


    def start_review(self, user):
        """PENDING_REVIEW -> UNDER_REVIEW (acteur : l'admin)."""
        self._assert_is_admin(user)
        if self.status != self.Status.PENDING_REVIEW:
            raise ValidationError("Seul un modèle en attente peut passer en revue.")
        self.status = self.Status.UNDER_REVIEW
        self.reviewed_by = user
        self.save(update_fields=['status', 'reviewed_by', 'updated_at'])



    def approve(self, user, official=False):
        """PENDING_REVIEW/UNDER_REVIEW -> PUBLISHED (acteur : l'admin)."""
        self._assert_is_admin(user)
        if self.status not in (self.Status.PENDING_REVIEW, self.Status.UNDER_REVIEW):
            raise ValidationError(
                "Seul un modèle en attente ou en revue peut être publié."
            )
        self.status = self.Status.PUBLISHED
        self.reviewed_by = user
        self.review_note = ''
        self.is_official = bool(official)
        self.save(update_fields=[
            'status', 'reviewed_by', 'review_note', 'is_official', 'updated_at',
        ])

    def reject(self, user, note):
        """PENDING_REVIEW/UNDER_REVIEW -> REJECTED (acteur : l'admin)."""
        self._assert_is_admin(user)
        if self.status not in (self.Status.PENDING_REVIEW, self.Status.UNDER_REVIEW):
            raise ValidationError(
                "Seul un modèle en attente ou en revue peut être rejeté."
            )
        if not note:
            raise ValidationError("Le motif de rejet est obligatoire.")
        self.status = self.Status.REJECTED
        self.reviewed_by = user
        self.review_note = note
        self.save(update_fields=['status', 'reviewed_by', 'review_note', 'updated_at'])

    def archive(self, user):
        """PUBLISHED -> ARCHIVED (acteur : l'admin)."""
        self._assert_is_admin(user)
        if self.status != self.Status.PUBLISHED:
            raise ValidationError("Seul un modèle publié peut être archivé.")
        self.status = self.Status.ARCHIVED
        self.save(update_fields=['status', 'updated_at'])

    def __str__(self):
        return f"{self.name} ({self.status})"


class Document(models.Model):
    """Instance de document créée par un utilisateur, copie JSONB indépendante."""

    title = models.CharField(max_length=200)
    template = models.ForeignKey(
        Template,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='documents',
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='documents',
    )
    content = models.JSONField(default=dict, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} — {self.owner.username}"
