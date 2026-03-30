# # Register your models here.
# import logging
#
# from django.contrib import admin
#
# from tv_and_film_buffAPI.models import Series, Episodes, Comments
#
#
# # Register your models here.
# class AdminSite(admin.AdminSite):
#     pass
#
#
# admin.site.login = AdminSite().login
# admin.autodiscover()
#
#
# logger = logging.getLogger(__name__)
#
#
# @admin.register(Molecule)
# class MessagesAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "zinc_id",
#         "smiles",
#         "molecular_weight",
#         "log_p",
#         "num_heavy_atoms",
#         "num_h_bond_acceptors",
#         "num_h_bond_donors",
#         "x",
#         "y",
#         "render_custom_data"
#     )
#     list_filter = (
#         "num_heavy_atoms",
#         "num_h_bond_acceptors",
#         "num_h_bond_donors",
#     )
#     ordering = [
#         "zinc_id",
#         "smiles",
#         "molecular_weight",
#         "log_p",
#         "num_heavy_atoms",
#         "num_h_bond_acceptors",
#         "num_h_bond_donors",
#         "x",
#         "y"
#     ]
#     search_fields = (
#         "zinc_id",
#         "smiles",
#         "molecular_weight",
#         "log_p",
#         "x",
#         "y",)
#
#     def render_custom_data(self, obj):
#         if not obj.custom_data:  # Handles None or empty dict
#             return None
#         return ", ".join([f"{key}: {value}" for key, value in obj.custom_data.items()])
#
#     render_custom_data.short_description = "Custom Data"