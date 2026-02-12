# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cta(models.Model):
    id = models.BigAutoField(primary_key=True)
    file = models.TextField(blank=True, null=True)
    index = models.SmallIntegerField(blank=True, null=True)
    font = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)  # This field type is a guess.
    number = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'CTA'


class CtaSubtitle(models.Model):
    id = models.BigAutoField(primary_key=True)
    cta = models.ForeignKey(Cta, models.DO_NOTHING, db_column='cta', blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CTA_subtitle'


class CtaTitle(models.Model):
    id = models.BigAutoField(primary_key=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)
    cta = models.ForeignKey(Cta, models.DO_NOTHING, db_column='cta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CTA_title'


class ServiceCard(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    service = models.ForeignKey('Services', models.DO_NOTHING, db_column='service', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Service_card'


class ServiceCardTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    service_card = models.ForeignKey(ServiceCard, models.DO_NOTHING, db_column='service_card', blank=True, null=True)
    label = models.TextField(blank=True, null=True)
    short_desc = models.TextField(blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Service_card_translations'


class Services(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Services'


class ServicesTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    service = models.ForeignKey(Services, models.DO_NOTHING, db_column='service', blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Services_translations'


class AboutPage(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'about_page'


class AboutPageBlock(models.Model):
    id = models.BigAutoField(primary_key=True)
    section = models.ForeignKey('AboutPageSection', models.DO_NOTHING, db_column='section', blank=True, null=True)
    index = models.SmallIntegerField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'about_page_block'


class AboutPageMedia(models.Model):
    id = models.BigAutoField(primary_key=True)
    about = models.ForeignKey(AboutPage, models.DO_NOTHING, db_column='about', blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    aspect_ratio = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'about_page_media'


class AboutPageSection(models.Model):
    id = models.BigAutoField(primary_key=True)
    page = models.ForeignKey(AboutPage, models.DO_NOTHING, db_column='page', blank=True, null=True)
    index = models.SmallIntegerField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'about_page_section'


class AboutPageSectionTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    section = models.ForeignKey(AboutPageSection, models.DO_NOTHING, db_column='section', blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)  # This field type is a guess.
    fontsize = models.TextField(blank=True, null=True)  # This field type is a guess.
    fontweight = models.TextField(blank=True, null=True)  # This field type is a guess.
    fontfamily = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'about_page_section_translations'


class AboutPageTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    block = models.ForeignKey(AboutPageBlock, models.DO_NOTHING, db_column='block', blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    fontcolor = models.TextField(blank=True, null=True)  # This field type is a guess.
    fontsize = models.TextField(blank=True, null=True)  # This field type is a guess.
    fontweight = models.TextField(blank=True, null=True)  # This field type is a guess.
    fontfamily = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'about_page_translations'


class AppDownload(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.TextField(blank=True, null=True)
    appstore = models.TextField(blank=True, null=True)
    playstore = models.TextField(blank=True, null=True)
    title_position = models.SmallIntegerField(blank=True, null=True)
    divide = models.SmallIntegerField(blank=True, null=True)
    font = models.TextField(blank=True, null=True)  # This field type is a guess.
    titlecolor = models.TextField(db_column='titleColor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fontcolor = models.TextField(db_column='fontColor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    listcolor = models.TextField(db_column='listColor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iconcolor = models.TextField(db_column='iconColor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buttonbgcolor = models.TextField(db_column='buttonBgColor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buttonfontcolor = models.TextField(db_column='buttonFontColor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'app_download'


class AppDownloadList(models.Model):
    id = models.BigAutoField(primary_key=True)
    app_download = models.ForeignKey(AppDownload, models.DO_NOTHING, db_column='app_download', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_download_list'


class AppDownloadListTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    app_download_list = models.ForeignKey(AppDownloadList, models.DO_NOTHING, db_column='app_download_list', blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_download_list_translation'


class AppDownloadTitle(models.Model):
    id = models.BigAutoField(primary_key=True)
    app_download = models.ForeignKey(AppDownload, models.DO_NOTHING, db_column='app_download', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_download_title'


class AppDownloadTitlePosition(models.Model):
    id = models.BigAutoField(primary_key=True)
    app_download_title = models.ForeignKey(AppDownloadTitle, models.DO_NOTHING, db_column='app_download_title', blank=True, null=True)
    top = models.SmallIntegerField(blank=True, null=True)
    left = models.SmallIntegerField(blank=True, null=True)
    rotate = models.SmallIntegerField(blank=True, null=True)
    size = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_download_title_position'


class AppDownloadTitleTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    app_download_title = models.ForeignKey(AppDownloadTitle, models.DO_NOTHING, db_column='app_download_title', blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_download_title_translation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BranchPhone(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.ForeignKey('Branches', models.DO_NOTHING, db_column='branch', blank=True, null=True)
    phone = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branch_phone'


class Branches(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    open = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    latitude = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branches'


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'category'


class CategoryTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_translations'


class Collateral(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'collateral'


class CollateralTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    collateral = models.ForeignKey(Collateral, models.DO_NOTHING, db_column='collateral', blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collateral_translation'


class ConditionTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)
    condition = models.ForeignKey('Conditions', models.DO_NOTHING, db_column='condition', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'condition_translations'


class Conditions(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'conditions'


class CoreValue(models.Model):
    id = models.BigAutoField(primary_key=True)
    index = models.BigIntegerField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_value'


class CoreValueDescTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    corevalue = models.ForeignKey(CoreValue, models.DO_NOTHING, db_column='corevalue', blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    fontcolor = models.TextField(blank=True, null=True)
    fontsize = models.SmallIntegerField(blank=True, null=True)
    fontweight = models.TextField(blank=True, null=True)  # This field type is a guess.
    fontfamily = models.TextField(blank=True, null=True)
    letterspace = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_value_desc_translations'


class CoreValueTitleTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    corevalue = models.ForeignKey(CoreValue, models.DO_NOTHING, db_column='corevalue', blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    fontcolor = models.TextField(blank=True, null=True)
    fontsize = models.SmallIntegerField(blank=True, null=True)
    fontweight = models.TextField(blank=True, null=True)
    fontfamily = models.TextField(blank=True, null=True)
    letterspace = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_value_title_translations'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Document(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'document'


class DocumentTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    document = models.ForeignKey(Document, models.DO_NOTHING, db_column='document', blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document_translation'


class FloatMenu(models.Model):
    id = models.BigAutoField(primary_key=True)
    iconcolor = models.TextField(blank=True, null=True)
    fontfamily = models.TextField(blank=True, null=True)
    bgcolor = models.TextField(blank=True, null=True)
    fontcolor = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    svg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'float_menu'


class FloatMenuSubmenus(models.Model):
    id = models.BigAutoField(primary_key=True)
    float_menu = models.ForeignKey(FloatMenu, models.DO_NOTHING, db_column='float_menu', blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    fontfamily = models.TextField(blank=True, null=True)
    bgcolor = models.TextField(blank=True, null=True)
    fontcolor = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'float_menu_submenus'


class FloatMenuSubmenusTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    float_menu_submenu = models.ForeignKey(FloatMenuSubmenus, models.DO_NOTHING, db_column='float_menu_submenu', blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    title = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'float_menu_submenus_translations'


class FloatMenuTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    float_menu = models.ForeignKey(FloatMenu, models.DO_NOTHING, db_column='float_menu', blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'float_menu_translations'


class Font(models.Model):
    id = models.BigIntegerField(primary_key=True)
    font = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'font'


class Footer(models.Model):
    id = models.BigAutoField(primary_key=True)
    logotext = models.TextField(blank=True, null=True)
    logo = models.TextField(blank=True, null=True)
    svg = models.TextField(blank=True, null=True)
    descmn = models.TextField(db_column='descMN', blank=True, null=True)  # Field name made lowercase.
    descen = models.TextField(db_column='descEN', blank=True, null=True)  # Field name made lowercase.
    locationmn = models.TextField(db_column='locationMN', blank=True, null=True)  # Field name made lowercase.
    locationen = models.TextField(db_column='locationEN', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    bgcolor = models.TextField(db_column='bgColor', blank=True, null=True)  # Field name made lowercase.
    fontcolor = models.TextField(blank=True, null=True)
    featurecolor = models.TextField(blank=True, null=True)
    socialiconcolor = models.TextField(db_column='socialIconColor', blank=True, null=True)  # Field name made lowercase.
    titlesize = models.TextField(db_column='titleSize', blank=True, null=True)  # Field name made lowercase.
    fontsize = models.TextField(blank=True, null=True)
    copyrighten = models.TextField(db_column='copyrightEN', blank=True, null=True)  # Field name made lowercase.
    copyrightmn = models.TextField(db_column='copyrightMN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'footer'


class FooterSocials(models.Model):
    id = models.BigAutoField(primary_key=True)
    footer = models.ForeignKey(Footer, models.DO_NOTHING, db_column='footer', blank=True, null=True)
    social = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    index = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'footer_socials'


class FooterUrls(models.Model):
    id = models.BigAutoField(primary_key=True)
    footer = models.ForeignKey(Footer, models.DO_NOTHING, db_column='footer', blank=True, null=True)
    nameen = models.TextField(db_column='nameEN', blank=True, null=True)  # Field name made lowercase.
    namemn = models.TextField(db_column='nameMN', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'footer_urls'


class Header(models.Model):
    id = models.BigAutoField(primary_key=True)
    logo = models.TextField(blank=True, null=True)
    active = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'header'
        db_table_comment = 'Headeer'


class HeaderMenu(models.Model):
    id = models.BigAutoField(primary_key=True)
    header = models.ForeignKey(Header, models.DO_NOTHING, db_column='header', blank=True, null=True)
    font = models.BigIntegerField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    index = models.SmallIntegerField(blank=True, null=True)
    visible = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'header_menu'


class HeaderMenuTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    menu = models.ForeignKey(HeaderMenu, models.DO_NOTHING, db_column='menu', blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'header_menu_translation'


class HeaderStyle(models.Model):
    id = models.BigAutoField(primary_key=True)
    header = models.ForeignKey(Header, models.DO_NOTHING, db_column='header', blank=True, null=True)
    bgcolor = models.TextField(db_column='bgColor', blank=True, null=True)  # Field name made lowercase.
    fontcolor = models.TextField(db_column='fontColor', blank=True, null=True)  # Field name made lowercase.
    hovercolor = models.TextField(db_column='hoverColor', blank=True, null=True)  # Field name made lowercase.
    height = models.SmallIntegerField(blank=True, null=True)
    sticky = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'header_style'


class HeaderSubmenu(models.Model):
    id = models.BigAutoField(primary_key=True)
    header_menu = models.ForeignKey(HeaderMenu, models.DO_NOTHING, db_column='header_menu', blank=True, null=True)
    font = models.BigIntegerField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    index = models.SmallIntegerField(blank=True, null=True)
    visible = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'header_submenu'


class HeaderSubmenuTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    submenu = models.ForeignKey(HeaderSubmenu, models.DO_NOTHING, db_column='submenu', blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'header_submenu_translation'


class HeaderTertiaryMenu(models.Model):
    id = models.BigAutoField(primary_key=True)
    header_submenu = models.ForeignKey(HeaderSubmenu, models.DO_NOTHING, db_column='header_submenu', blank=True, null=True)
    font = models.TextField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    index = models.SmallIntegerField(blank=True, null=True)
    visible = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'header_tertiary_menu'


class HeaderTertiaryMenuTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    tertiary_menu = models.ForeignKey(HeaderTertiaryMenu, models.DO_NOTHING, db_column='tertiary_menu', blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'header_tertiary_menu_translation'


class HeroSlider(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    file = models.TextField(blank=True, null=True)
    time = models.SmallIntegerField(blank=True, null=True)
    index = models.SmallIntegerField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hero_slider'


class HrPolicy(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.TextField(blank=True, null=True)
    visual_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    visual_preset = models.TextField(blank=True, null=True)  # This field type is a guess.
    font_color = models.TextField(blank=True, null=True)  # This field type is a guess.
    bg_color = models.TextField(blank=True, null=True)  # This field type is a guess.
    fontsize = models.TextField(blank=True, null=True)  # This field type is a guess.
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_policy'


class HrPolicyTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    policy = models.ForeignKey(HrPolicy, models.DO_NOTHING, db_column='policy', blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_policy_translations'


class JobTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    job = models.ForeignKey('Jobs', models.DO_NOTHING, db_column='job', blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='language', blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    department = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_translations'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.SmallIntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'


class Language(models.Model):
    id = models.BigAutoField(primary_key=True)
    lang_code = models.TextField(blank=True, null=True)
    lang_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'language'


class ManagementMember(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.TextField(blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'management_member'


class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey('NewsCategory', models.DO_NOTHING, db_column='category', blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    video = models.TextField(blank=True, null=True)
    feature = models.BooleanField(blank=True, null=True)
    render = models.BooleanField(blank=True, null=True)
    readtime = models.SmallIntegerField(blank=True, null=True)
    slug = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class NewsCategory(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'news_category'


class NewsCategoryTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(NewsCategory, models.DO_NOTHING, db_column='category', blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_category_translations'


class NewsContentTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    news = models.ForeignKey(News, models.DO_NOTHING, db_column='news', blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)
    font = models.TextField(blank=True, null=True)
    family = models.TextField(blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_content_translations'


class NewsImages(models.Model):
    id = models.BigAutoField(primary_key=True)
    news = models.ForeignKey(News, models.DO_NOTHING, db_column='news', blank=True, null=True)
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_images'


class NewsShortdescTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    news = models.ForeignKey(News, models.DO_NOTHING, db_column='news', blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)
    font = models.TextField(blank=True, null=True)
    family = models.TextField(blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_shortdesc_translations'


class NewsSocials(models.Model):
    id = models.BigAutoField(primary_key=True)
    news = models.ForeignKey(News, models.DO_NOTHING, db_column='news', blank=True, null=True)
    social = models.TextField(blank=True, null=True)
    icon = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_socials'


class NewsTitleTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    news = models.ForeignKey(News, models.DO_NOTHING, db_column='news', blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)
    font = models.TextField(blank=True, null=True)
    family = models.TextField(blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_title_translations'


class PageDescriptionTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    page = models.ForeignKey('Pages', models.DO_NOTHING, db_column='page', blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)
    font = models.TextField(blank=True, null=True)
    family = models.TextField(blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'page_description_translations'


class PageTitleTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    page = models.ForeignKey('Pages', models.DO_NOTHING, db_column='page', blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)
    font = models.TextField(blank=True, null=True)
    family = models.TextField(blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'page_title_translations'


class Pages(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    style = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages'


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_type = models.ForeignKey('ProductType', models.DO_NOTHING, db_column='product_type', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductCollaterial(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='product', blank=True, null=True)
    collateral = models.ForeignKey(Collateral, models.DO_NOTHING, db_column='collateral', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_collaterial'


class ProductCondition(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='product', blank=True, null=True)
    condition = models.ForeignKey(Conditions, models.DO_NOTHING, db_column='condition', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_condition'


class ProductDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='product', blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    min_fee_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    max_fee_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    min_interest_rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    max_interest_rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    term_months = models.SmallIntegerField(blank=True, null=True)
    min_processing_hours = models.SmallIntegerField(blank=True, null=True)
    max_processing_hoyrs = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_details'


class ProductDocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='product', blank=True, null=True)
    document = models.ForeignKey(Document, models.DO_NOTHING, db_column='document', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_document'


class ProductTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='product', blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_translations'


class ProductType(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_type'


class ProductTypeTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_type = models.ForeignKey(ProductType, models.DO_NOTHING, db_column='product_type', blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, db_column='language', blank=True, null=True)
    label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_type_translations'


class ServiceCollateral(models.Model):
    id = models.BigAutoField(primary_key=True)
    service = models.ForeignKey(Services, models.DO_NOTHING, db_column='service', blank=True, null=True)
    collateral = models.ForeignKey(Collateral, models.DO_NOTHING, db_column='collateral', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_collateral'


class ServiceCondition(models.Model):
    id = models.BigAutoField(primary_key=True)
    service = models.ForeignKey(Services, models.DO_NOTHING, db_column='service', blank=True, null=True)
    condition = models.ForeignKey(Conditions, models.DO_NOTHING, db_column='condition', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_condition'


class ServiceDocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    service = models.ForeignKey(Services, models.DO_NOTHING, db_column='service', blank=True, null=True)
    document = models.ForeignKey(Document, models.DO_NOTHING, db_column='document', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_document'


class Shareholder(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.TextField(blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shareholder'


class ShareholderTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    shareholder = models.ForeignKey(Shareholder, models.DO_NOTHING, db_column='shareholder', blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, db_column='language', blank=True, null=True)
    fullname = models.TextField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shareholder_translations'


class Timeline(models.Model):
    id = models.BigAutoField(primary_key=True)
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    order = models.BigIntegerField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timeline'


class TimelineTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    timeline = models.ForeignKey(Timeline, models.DO_NOTHING, db_column='timeline', blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, db_column='language', blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    title_color = models.TextField(blank=True, null=True)
    shortdesc = models.TextField(blank=True, null=True)
    shortdesc_color = models.TextField(blank=True, null=True)
    fulldesc = models.TextField(blank=True, null=True)
    fulldesc_color = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timeline_translations'


class VisionBlock(models.Model):
    id = models.BigAutoField(primary_key=True)
    file = models.TextField(blank=True, null=True)
    file_ratio = models.TextField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vision_block'


class VisionBlockDescTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    vision_block = models.ForeignKey(VisionBlock, models.DO_NOTHING, db_column='vision_block', blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, db_column='language', blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    fontcolor = models.TextField(blank=True, null=True)
    fontsize = models.BigIntegerField(blank=True, null=True)
    fontweight = models.TextField(blank=True, null=True)
    fontfamily = models.TextField(blank=True, null=True)
    letterspace = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vision_block_desc_translations'


class VisionBlockTitleTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    vision_block = models.ForeignKey(VisionBlock, models.DO_NOTHING, db_column='vision_block', blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, db_column='language', blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    fontcolor = models.TextField(blank=True, null=True)
    fontsize = models.BigIntegerField(blank=True, null=True)
    fontweight = models.SmallIntegerField(blank=True, null=True)
    fontfamily = models.TextField(blank=True, null=True)
    letterspace = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vision_block_title_translations'
