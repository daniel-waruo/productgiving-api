import graphene
from django.db.models import Sum, Count
from graphene_django import DjangoObjectType
from graphene_django.converter import convert_django_field
from pyuploadcare.dj.models import ImageField

from campaigns.models import Campaign, CampaignProduct, CampaignProfile, ProductRequest
from cart.models import Cart
from donations.models import Donation, DonationProduct
from donations.schema.types import DonationType


@convert_django_field.register(ImageField)
def convert_field(field, registry=None):
    return graphene.String()


class DonationDateType(graphene.ObjectType):
    date = graphene.Date()
    number = graphene.Int()


class CampaignProductType(DjangoObjectType):
    class Meta:
        model = CampaignProduct

    in_cart = graphene.Boolean()

    def resolve_in_cart(self: CampaignProduct, info):
        cart = Cart.objects.get_from_request(info.context)
        return cart.products.filter(id=self.id).exists()

    number_donated = graphene.Int()

    def resolve_number_donated(self: CampaignProduct, info, **kwargs):
        donation_products = self.product.donation_products.filter(
            product=self
        ).distinct()
        number_donated = donation_products.aggregate(
            total_donated=Sum("quantity")
        )["total_donated"]
        return number_donated or 0


class CampaignType(DjangoObjectType):
    class Meta:
        model = Campaign

    donation_number = graphene.Int()

    def resolve_donation_number(self, info, **kwargs):
        return Donation.objects.filter(
            products__product__campaign=self,
            payment_status="success"
        ).distinct().count()

    progress = graphene.Float()

    def resolve_progress(self: Campaign, info, **kwargs):
        # get total target for all campaign products
        total_target = self.products.aggregate(
            total_target=Sum("target")
        )["total_target"]
        # get total donated for all campaign products
        total_donated = DonationProduct.objects.filter(
            product__campaign=self,
            donation__payment_status="success"
        ).distinct().aggregate(
            total_donated=Sum("quantity")
        )["total_donated"]
        if not total_donated:
            return 0
        progress = int((total_donated / total_target) * 100)
        return progress

    donations_by_date = graphene.List(DonationDateType)

    def resolve_donations_by_date(self: Campaign, info, **kwargs):
        donations = Donation.objects.filter(
            products__product__campaign=self,
            payment_status="success"
        ).extra({'date': "date(created_on)"}).values('date').annotate(number=Count('id'))
        return list(map(lambda x: DonationDateType(date=x["date"], number=x["number"]), donations))

    donations = graphene.List(DonationType)

    def resolve_donations(self: Campaign, info, **kwargs):
        return self.donations.filter(transaction__mpesa_code__isnull=False)

    products = graphene.List(CampaignProductType)

    def resolve_products(self: Campaign, info, **kwargs):
        return self.products.filter(deleted=False)

    deleted_products = graphene.List(CampaignProductType)

    def resolve_deleted_products(self: Campaign, info, **kwargs):
        return self.products.filter(deleted=True)


class CampaignProfileType(DjangoObjectType):
    class Meta:
        model = CampaignProfile


class ProductRequestType(DjangoObjectType):
    class Meta:
        model = ProductRequest


class CampaignCountType(graphene.ObjectType):
    all = graphene.Int()

    def resolve_all(self, info):
        campaigns = Campaign.objects.filter(
            deleted=False,
            is_active=True
        )
        return campaigns.count()

    un_approved = graphene.Int()

    def resolve_un_approved(self, info):
        campaigns = Campaign.objects.filter(
            deleted=False,
            is_active=True,
            is_approved=False,
        )
        return campaigns.count()

    approved = graphene.Int()

    def resolve_approved(self, info):
        campaigns = Campaign.objects.filter(
            deleted=False,
            is_active=True,
            is_approved=True
        )
        return campaigns.count()

    featured = graphene.Int()

    def resolve_featured(self, info):
        campaigns = Campaign.objects.filter(
            deleted=False,
            is_active=True,
            is_featured=True
        )
        return campaigns.count()
